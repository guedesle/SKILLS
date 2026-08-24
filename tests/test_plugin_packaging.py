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
            "schema_version": 1,
            "marketplace": {"name": "local-test", "display_name": "Local Test"},
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

    def test_unknown_skill_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            catalog["plugins"][0]["skills"] = ["missing"]
            errors = validate_catalog(root, registry, catalog)
            self.assertTrue(any("não registrada" in error for error in errors))

    def test_duplicate_skill_across_plugins_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            second = dict(catalog["plugins"][0])
            second["name"] = "second-plugin"
            catalog["plugins"].append(second)
            errors = validate_catalog(root, registry, catalog)
            self.assertTrue(any("outro plugin" in error for error in errors))

    def test_build_creates_manifest_marketplace_and_skill_zip(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            registry, catalog = self.make_repo(root)
            output = root / "dist"
            errors = validate_catalog(root, registry, catalog)
            self.assertEqual(errors, [])
            manifest = build(root, output, registry, catalog)

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


if __name__ == "__main__":
    unittest.main()
