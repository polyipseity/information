"""Tests for RuleRegistry behaviour in academic-notes.

Verifies registration semantics, duplicate detection, and lookup helpers.
"""

import pytest
from check_mods.models import ValidationContext
from check_mods.registry import RuleRegistry

__all__ = ()


def test_rule_registration():
    """RuleRegistry should register functions and prevent duplicates."""
    reg = RuleRegistry()

    @reg.register(id="foo")
    def foo(ctx: ValidationContext):
        """Dummy rule used for registration tests."""
        return []

    with pytest.raises(RuntimeError):

        @reg.register(id="foo")
        def foo2(ctx):
            """Second dummy rule to trigger duplicate id error."""
            return []

    assert reg.get_rule_id(foo) == "foo"
    assert reg.items() == [("foo", foo)]
    assert reg.values() == [foo]


def test_register_invalid_explicit_id():
    """Supplying a badly formatted id should raise ValueError."""
    reg = RuleRegistry()
    with pytest.raises(ValueError):

        @reg.register(id="Bad-ID!")
        def bad(ctx: ValidationContext):
            """dummy"""
            return []


def test_include_another_registry():
    """Including one registry into another should copy all rules.

    The destination must reject conflicting identifiers.
    """
    r1 = RuleRegistry()

    @r1.register(id="a")
    def a(ctx):
        """dummy rule a"""
        return []

    @r1.register(id="b")
    def b(ctx):
        """dummy rule b"""
        return []

    r2 = RuleRegistry()
    # start empty and then import r1
    r2.include_registry(r1)
    assert r2.items() == [("a", a), ("b", b)]

    # importing again should raise because identifiers already exist
    with pytest.raises(RuntimeError):
        r2.include_registry(r1)


def test_get_rule_id_not_found():
    """get_rule_id should return empty string for unknown functions."""

    reg = RuleRegistry()

    def dummy(ctx):
        """Simple placeholder rule for id lookup tests."""
        return []

    assert reg.get_rule_id(dummy) == ""


def test_items_ordering():
    """Registry should preserve insertion order in items() and values()."""

    reg = RuleRegistry()

    @reg.register(id="first")
    def f1(ctx):
        """first dummy rule for ordering check"""
        return []

    @reg.register(id="second")
    def f2(ctx):
        """second dummy rule for ordering check"""
        return []

    assert reg.items() == [("first", f1), ("second", f2)]
    assert reg.values() == [f1, f2]
