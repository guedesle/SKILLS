from pathlib import Path
import tempfile
import unittest

from scripts.skill_validation import extract_catalog_versions, load_frontmatter, validate_skill_record


class SkillValidationTests(unittest.TestCase):
    def test_invalid_yaml_raises_validation_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "SKILL.md"
            path.write_text("---\nname: sample\ndescription: broken: scalar\n---\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_frontmatter(path)

    def test_versions_are_bound_to_skill_rows(self):
        markdown = "| `alpha` | **1.0.0** | X |\n| `beta` | **2.0.0** | X |"
        versions = extract_catalog_versions(markdown)
        self.assertEqual(versions["alpha"], "1.0.0")
        self.assertEqual(versions["beta"], "2.0.0")

    def test_status_table_version_column_is_parsed(self):
        markdown = "| `alpha` | Gestão | 1.3.0 | Canônica |\n| `beta` | QA | 2.0.0 | Canônica |"
        versions = extract_catalog_versions(markdown)
        self.assertEqual(versions["alpha"], "1.3.0")
        self.assertEqual(versions["beta"], "2.0.0")


class SkillRecordTests(unittest.TestCase):
    def test_version_drift_is_reported_for_same_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "skills" / "alpha"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("---\nname: alpha\ndescription: Valid description\n---\n", encoding="utf-8")
            record = {"name": "alpha", "version": "1.1.0", "path": "skills/alpha/SKILL.md"}
            errors = validate_skill_record(root, record, {"alpha": "1.0.0"}, {"alpha": "1.1.0"})
            self.assertTrue(any("README" in error and "1.1.0" in error for error in errors))

    def test_valid_record_has_no_errors(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill_dir = root / "skills" / "alpha"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text("---\nname: alpha\ndescription: Valid description\n---\n", encoding="utf-8")
            record = {"name": "alpha", "version": "1.1.0", "path": "skills/alpha/SKILL.md"}
            errors = validate_skill_record(root, record, {"alpha": "1.1.0"}, {"alpha": "1.1.0"})
            self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
