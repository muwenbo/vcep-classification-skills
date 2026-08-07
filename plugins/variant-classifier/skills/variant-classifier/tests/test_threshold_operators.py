"""
Regression tests for threshold comparator handling in classify_variant.py.

VCEPs differ on whether a frequency threshold is inclusive. GALT states
BA1/BS1/PM2 as >= / <=, and SLC6A8 v2.1 explicitly flipped strict to inclusive.
Before these tests the comparators were hardcoded strict, so a variant whose
allele frequency sat exactly on a VCEP boundary took the wrong branch with no
diagnostic.
"""

import importlib.util
import json
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "classify_variant.py"
SPEC = importlib.util.spec_from_file_location("classify_variant", SCRIPT)
classify_variant = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(classify_variant)

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def evaluate(af, vcep_spec=None, acmg_criteria=None):
    """Evaluate population-frequency criteria and return {criterion: evaluation}."""
    classifier = classify_variant.VariantClassifier(
        acmg_criteria=acmg_criteria, vcep_spec=vcep_spec
    )
    return {e.criterion: e for e in classifier.evaluate_population_frequency(af)}


class ResolveThresholdTests(unittest.TestCase):
    def test_bare_number_takes_the_default_operator(self):
        self.assertEqual(
            classify_variant.resolve_threshold(0.02, 0.05, ">"), (0.02, ">")
        )

    def test_dict_operator_overrides_the_default(self):
        self.assertEqual(
            classify_variant.resolve_threshold({"threshold": 0.02, "op": ">="}, 0.05, ">"),
            (0.02, ">="),
        )

    def test_dict_without_operator_keeps_the_default(self):
        self.assertEqual(
            classify_variant.resolve_threshold({"threshold": 0.02}, 0.05, ">"),
            (0.02, ">"),
        )

    def test_missing_spec_returns_defaults(self):
        self.assertEqual(
            classify_variant.resolve_threshold(None, 0.05, ">"), (0.05, ">")
        )

    def test_unknown_operator_raises_rather_than_falling_back(self):
        with self.assertRaises(ValueError):
            classify_variant.resolve_threshold({"threshold": 0.05, "op": "=>"}, 0.05, ">")


class BoundaryTests(unittest.TestCase):
    """A variant sitting exactly on the threshold is the case that used to break."""

    def test_strict_default_excludes_ba1_on_the_boundary(self):
        self.assertFalse(evaluate(0.05)["BA1"].met)

    def test_inclusive_vcep_override_includes_ba1_on_the_boundary(self):
        vcep = {"BA1_threshold": {"threshold": 0.05, "op": ">="}}
        self.assertTrue(evaluate(0.05, vcep_spec=vcep)["BA1"].met)

    def test_strict_default_excludes_pm2_on_the_boundary(self):
        self.assertFalse(evaluate(0.0001)["PM2"].met)

    def test_inclusive_vcep_override_includes_pm2_on_the_boundary(self):
        vcep = {"PM2_threshold": {"threshold": 0.0001, "op": "<="}}
        self.assertTrue(evaluate(0.0001, vcep_spec=vcep)["PM2"].met)

    def test_inclusive_vcep_override_includes_bs1_on_the_boundary(self):
        vcep = {"BS1_threshold": {"threshold": 0.01, "op": ">="}}
        result = evaluate(0.01, vcep_spec=vcep)
        self.assertTrue(result["BS1"].met)
        self.assertFalse(result["BA1"].met)

    def test_values_away_from_the_boundary_are_unaffected_by_the_operator(self):
        for op in (">", ">="):
            vcep = {"BA1_threshold": {"threshold": 0.05, "op": op}}
            self.assertTrue(evaluate(0.06, vcep_spec=vcep)["BA1"].met)
            self.assertFalse(evaluate(0.04, vcep_spec=vcep)["BA1"].met)


class BackwardCompatibilityTests(unittest.TestCase):
    def test_scalar_vcep_override_still_works(self):
        """VCEP specs written before 'op' existed pass a bare number."""
        result = evaluate(0.002, vcep_spec={"BS1_threshold": 0.001})
        self.assertTrue(result["BS1"].met)
        self.assertTrue(result["BS1"].vcep_modified)

    def test_scalar_vcep_override_keeps_strict_semantics(self):
        self.assertFalse(evaluate(0.001, vcep_spec={"BS1_threshold": 0.001})["BS1"].met)


class EvidenceReportingTests(unittest.TestCase):
    def test_evidence_states_the_rule_actually_applied(self):
        vcep = {"BA1_threshold": {"threshold": 0.05, "op": ">="}}
        self.assertIn("AF >= 0.05", evaluate(0.05, vcep_spec=vcep)["BA1"].evidence)

    def test_zero_frequency_is_reported_not_treated_as_missing(self):
        """0.0 is falsy; it used to render as 'AF: N/A'."""
        self.assertNotIn("N/A", evaluate(0.0)["BA1"].evidence)


class ShippedCriteriaFileTests(unittest.TestCase):
    def test_every_shipped_frequency_threshold_declares_an_operator(self):
        criteria = json.loads((DATA_DIR / "acmg_criteria.json").read_text())
        for name, spec in criteria["population_frequency"].items():
            if not isinstance(spec, dict) or "threshold" not in spec:
                continue
            with self.subTest(criterion=name):
                self.assertIn("op", spec)
                self.assertIn(spec["op"], classify_variant.COMPARATORS)

    def test_defaults_match_the_shipped_file(self):
        criteria = json.loads((DATA_DIR / "acmg_criteria.json").read_text())
        defaults = classify_variant.get_default_acmg_criteria()["population_frequency"]
        for name, spec in defaults.items():
            with self.subTest(criterion=name):
                self.assertEqual(
                    spec["threshold"], criteria["population_frequency"][name]["threshold"]
                )


if __name__ == "__main__":
    unittest.main()
