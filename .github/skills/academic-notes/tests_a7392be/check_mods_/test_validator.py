"""Tests for validator module behaviour related to registries."""

from check_mods.rules import RULE_REGISTRY as rules_registry
from check_mods.validator import RULE_REGISTRY as validator_registry

__all__ = ()


def test_validator_registry_contains_rules():
    """The registry built by the validator should include rules from rules.py."""
    ids = [rid for rid, _ in validator_registry.items()]
    assert "metadata_aliases_present" in ids
    # ensure registry is a separate object from the rules module's own
    assert validator_registry is not rules_registry
