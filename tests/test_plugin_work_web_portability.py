import json
import unittest
from pathlib import Path

from scripts.audit_skill_portability import audit_text


ROOT = Path(__file__).resolve().parents[1]


class PluginWorkWebPortabilityTests(unittest.TestCase):
    def load_catalog(self) -> dict:
        return json.loads((ROOT / "plugin-catalog.json").read_text(encoding="utf-8"))

    def test_catalog_remains_private_but_declares_work_web_target(self):
        catalog = self.load_catalog()
        self.assertEqual(catalog["distribution_mode"], "local-only")
        self.assertFalse(catalog["universal_publication"])
        self.assertIn("chatgpt-work-workspace-private", catalog["future_distribution_targets"])

    def test_writing_plugin_has_expected_editorial_composition(self):
        catalog = self.load_catalog()
        writing = next(item for item in catalog["plugins"] if item["name"] == "guedesle-writing")
        self.assertEqual(writing["version"], "1.0.0")
        self.assertEqual(
            writing["skills"],
            [
                "writing-workflow",
                "plan-content",
                "architect-text",
                "design-paragraphs",
                "write-with-evidence",
                "write-technical-content",
                "calibrate-rhetoric",
                "improve-accessible-writing",
                "review-editorial-quality",
                "assess-editorial-alignment",
            ],
        )

    def test_writing_skill_contracts_have_no_local_portability_blockers(self):
        catalog = self.load_catalog()
        writing = next(item for item in catalog["plugins"] if item["name"] == "guedesle-writing")
        for skill_name in writing["skills"]:
            text = (ROOT / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
            result = audit_text(text)
            self.assertNotEqual(
                result["classification"],
                "PROJECT_ONLY",
                msg=f"{skill_name}: {result}",
            )
            self.assertEqual(result["blockers"], [], msg=f"{skill_name}: {result}")


if __name__ == "__main__":
    unittest.main()
