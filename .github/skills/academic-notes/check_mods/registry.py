"""Rule registration and lookup for the academic-notes validator.

This module provides :class:`RuleRegistry`, a simple container that maps
string identifiers to rule functions.  Clients create instances and register
rules via the ``register`` decorator, and registries may be merged using
``include_registry``.  ``get_rule_id`` allows reverse lookups and is used
in the test suite.
"""

import re
from collections.abc import Callable, Sequence

from .models import ValidationContext, ValidationMessage

__all__ = ("RuleRegistry",)


class RuleRegistry:
    """Container holding id→callable mappings for validation rules.

    Usage::

        registry = RuleRegistry()

        @registry.register(id="foo")
        def foo(ctx: ValidationContext) -> list[ValidationMessage]:
            ...
    """

    def __init__(self) -> None:
        """Initialize an empty registry mapping identifiers to rule callables.

        The internal dictionary ``_rules`` stores the associations and is
        keyed by the rule id string supplied to the ``register`` decorator.
        """
        self._rules: dict[
            str, Callable[[ValidationContext], Sequence[ValidationMessage]]
        ] = {}

    def register(
        self, *, id: str | None = None
    ) -> Callable[
        [Callable[[ValidationContext], Sequence[ValidationMessage]]],
        Callable[[ValidationContext], Sequence[ValidationMessage]],
    ]:
        """Decorator that registers the wrapped function under *id*.

        If *id* is omitted the decorated function's name is used as the
        identifier after normalizing it to a lowercase, underscore-separated
        form.  This helps keep rule IDs consistent without requiring the
        caller to repeat the name manually.

        The identifier must be unique; attempting to register a second rule
        with the same id raises ``RuntimeError``.
        """

        def _decorate(
            func: Callable[[ValidationContext], Sequence[ValidationMessage]],
        ) -> Callable[[ValidationContext], Sequence[ValidationMessage]]:
            """Actual decorator applied to the user-defined rule function.

            If the caller did not supply an explicit *id*, derive one from the
            function name.  The normalization step simply lowercases and
            replaces any non-alphanumeric characters with underscores; this
            matches the convention used throughout the package.  The resulting
            identifier is guaranteed to be unique within this registry.
            """
            nonlocal id
            if id is None:
                # derive from func name and normalise
                derived = func.__name__
                # replace any characters other than lowercase alphanumerics with underscore
                id_norm = re.sub(r"[^0-9a-z]+", "_", derived.lower())
                id = id_norm
            else:
                # explicit id supplied; verify it already follows the rules
                if not re.fullmatch(r"[0-9a-z]+(?:_[0-9a-z]+)*", id):
                    raise ValueError(
                        f"explicit rule id {id!r} does not follow naming convention"
                    )
                # keep the string as‑is (no normalization)

            if id in self._rules:
                raise RuntimeError(f"rule id {id!r} already registered")
            self._rules[id] = func
            return func

        return _decorate

    def items(
        self,
    ) -> list[tuple[str, Callable[[ValidationContext], Sequence[ValidationMessage]]]]:
        """Return a list of ``(id, function)`` pairs for all registered rules."""
        return list(self._rules.items())

    def values(
        self,
    ) -> list[Callable[[ValidationContext], Sequence[ValidationMessage]]]:
        """Return the rule callables in registration order."""
        return list(self._rules.values())

    def get_rule_id(
        self, func: Callable[[ValidationContext], Sequence[ValidationMessage]]
    ) -> str:
        """Return the identifier for a registered rule by reverse lookup.

        Returns an empty string if the function is not found.
        """
        for key, value in self._rules.items():
            if value is func:
                return key
        return ""

    # new functionality -----------------------------------------------------
    def include_registry(self, other: "RuleRegistry") -> None:
        """Merge another :class:`RuleRegistry` into this one.

        Each rule from *other* is copied into the current registry.  If a
        rule identifier already exists in the destination registry a
        :class:`RuntimeError` is raised to avoid accidental overwrites.  This
        helper makes it easy for higher‑level code (such as the validator)
        to compose multiple sets of rules without having to manage the
        internal ``_rules`` dict directly.
        """
        for rid, func in other.items():
            if rid in self._rules:
                raise RuntimeError(
                    f"rule id {rid!r} already registered in target registry"
                )
            self._rules[rid] = func
