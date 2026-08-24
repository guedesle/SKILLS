import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.package_plugins import build, validate_catalog


class PluginPackagingTests(unittest.TestCase):
    def make_repo(self, root: Path) -> tuple[dict, dict]:
        skill_dir = root / "skills" / "sample"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            '---\nname: sample\ndescription: "Sample reusable workflow."\n---\n\n# Sample\n',
            encoding="utf-8",
        )
        registry = {
            "repository": "guedesle/SKILLS",
            "skills": [
                {"name": "sample", "version": "1.2.3", "path": "skills/sample/SKILL.md"}
            ],
        }
        catalog = {
            "schema_version": 2,
            "distribution_mode": "local-only",
            "marketplace": {"name": "local-test", "display_name": "Local Test"},
            "shared_skills": [],
            "plugins": [
                {
                    "name": "sample-plugin",
                    "version": "1.0.0",
                    "description": "Sample plugin",
                    "display_name": "Sample Plugin",
                    "short_description": "Sample workflows",
                    "long_description": "Sample reusable workflows.",
                    "category": "Productivity",
                    "default_prompts": ["Use Sample Plugin."],
                    "skills": ["sample"],
                }
            ],
        }
        return registry, catalog

    def add_second_plugin(self, catalog: dict) -> None:
        second = dict(catalog["plugins"][0])
        second["name"] = "second-plugin"
        second["display_name"] = "Second Plugin"
        catalog["plugins"].append(second)

    def test_unknown_skill_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            catalog["plugins"][0]["skills"] = ["missing"]
            errors = validate_catalog(root, registry, catalog)
            self.assertTrue(any("não registrada" in error for error in errors))

    def test_non_local_distribution_mode_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            catalog["distribution_mode"] = "public"
            errors = validate_catalog(root, registry, catalog)
            self.assertTrue(any("distribution_mode" in error for error in errors))

    def test_duplicate_skill_across_plugins_fails_without_explicit_share(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            self.add_second_plugin(catalog)
            errors = validate_catalog(root, registry, catalog)
            self.assertTrue(any("sem shared_skills" in error for error in errors))

    def test_duplicate_skill_across_plugins_passes_when_explicitly_shared(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            self.add_second_plugin(catalog)
            catalog["shared_skills"] = ["sample"]
            errors = validate_catalog(root, registry, catalog)
            self.assertEqual(errors, [])

    def test_declared_shared_skill_must_be_used_by_at_least_two_plugins(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            catalog["shared_skills"] = ["sample"]
            errors = validate_catalog(root, registry, catalog)
            self.assertTrue(any("pelo menos 2 plugins" in error for error in errors))

    def test_build_creates_manifest_marketplace_and_skill_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            output = root / "dist"
            errors = validate_catalog(root, registry, catalog)
            self.assertEqual(errors, [])
            manifest = build(root, output, registry, catalog)

            self.assertEqual(manifest["schema_version"], 2)
            self.assertEqual(manifest["distribution_mode"], "local-only")
            plugin_root = output / "marketplace" / "plugins" / "sample-plugin"
            plugin_manifest = json.loads(
                (plugin_root / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8")
            )
            self.assertEqual(plugin_manifest["skills"], "./skills/")
            self.assertTrue((plugin_root / "skills" / "sample" / "SKILL.md").is_file())

            marketplace = json.loads(
                (output / "marketplace" / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8")
            )
            self.assertEqual(marketplace["plugins"][0]["source"]["path"], "./plugins/sample-plugin")

            archive = output / manifest["plugins"][0]["archive"]
            with zipfile.ZipFile(archive) as zf:
                names = set(zf.namelist())
            self.assertIn(".codex-plugin/plugin.json", names)
            self.assertIn("skills/sample/SKILL.md", names)

    def test_build_supports_two_local_plugins_sharing_canonical_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            self.add_second_plugin(catalog)
            catalog["shared_skills"] = ["sample"]
            output = root / "dist"

            errors = validate_catalog(root, registry, catalog)
            self.assertEqual(errors, [])
            manifest = build(root, output, registry, catalog)

            self.assertEqual([item["name"] for item in manifest["plugins"]], ["sample-plugin", "second-plugin"])
            marketplace = json.loads(
                (output / "marketplace" / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8")
            )
            self.assertEqual(
                [item["name"] for item in marketplace["plugins"]],
                ["sample-plugin", "second-plugin"],
            )
            for plugin_name in ("sample-plugin", "second-plugin"):
                self.assertTrue(
                    (output / "marketplace" / "plugins" / plugin_name / "skills" / "sample" / "SKILL.md").is_file()
                )


if __name__ == "__main__":
    unittest.main()
