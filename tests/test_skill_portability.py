import unittest

from scripts.audit_skill_portability import audit_text


class PortabilityTests(unittest.TestCase):
    def test_windows_absolute_path_blocks_global_ready(self):
        result = audit_text(r"Use C:\projetos\siedoe\schema.json sempre.")
        self.assertNotEqual(result["classification"], "GLOBAL_READY")
        self.assertTrue(result["blockers"])

    def test_generic_contract_is_global_ready(self):
        result = audit_text("Validate a canonical skill directory and its declared metadata.")
        self.assertEqual(result["classification"], "GLOBAL_READY")

    def test_generic_discussion_of_adapter_does_not_require_adapter(self):
        result = audit_text("A promotion workflow may preserve a local adapter when a project needs one.")
        self.assertEqual(result["classification"], "GLOBAL_READY")


if __name__ == "__main__":
    unittest.main()
