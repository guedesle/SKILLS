import tempfile
import unittest
from pathlib import Path

from scripts.validate_skill_evals import validate_eval_document, validate_repository


class SkillEvalTests(unittest.TestCase):
    def test_duplicate_case_ids_fail(self):
        body = """schema_version: 1
skill: sample
kind: trigger_positive
cases:
  - id: same
    input: first
  - id: same
    input: second
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "trigger-positive.yaml"
            path.write_text(body, encoding="utf-8")
            errors = validate_eval_document(path, "trigger_positive")
            self.assertTrue(any("duplicado" in error for error in errors))

    def test_wrong_kind_fails(self):
        body = """schema_version: 1
skill: sample
kind: behavior
cases:
  - id: one
    input: do it
    expect: preserve scope
"""
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "trigger-positive.yaml"
            path.write_text(body, encoding="utf-8")
            errors = validate_eval_document(path, "trigger_positive")
            self.assertTrue(any("kind" in error for error in errors))


class EvalRepositoryTests(unittest.TestCase):
    def test_eval_directory_requires_skill_file_and_core_eval_set(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            eval_dir = root / "skills" / "sample" / "evals"
            eval_dir.mkdir(parents=True)
            (eval_dir / "trigger-positive.yaml").write_text(
                """schema_version: 1
skill: sample
kind: trigger_positive
cases:
  - id: one
    input: build a sample skill
""",
                encoding="utf-8",
            )
            errors = validate_repository(root, {"sample"})
            self.assertTrue(any("SKILL.md" in error for error in errors))
            self.assertTrue(any("trigger-negative.yaml" in error for error in errors))
            self.assertTrue(any("behavior.yaml" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
