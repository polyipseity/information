#!/usr/bin/env sh
# scripts/prepare-commit-msg.sh
# Wrapper for the prepare-commit-msg hook.
# Checks for bun availability and runs the mjs script if available.
# If bun is not available, prints a warning but does not block the commit.

set -e

BUN_CMD=bun

# If bun isn't available, print a clear warning but allow the
# commit/merge to continue (do not block developer workflows).
if ! command -v "$BUN_CMD" >/dev/null 2>&1; then
  cat <<'EOF' >&2
========================================
WARNING: bun is not installed or not on PATH.
The prepare-commit-msg hook was skipped; merge commit messages will not be
standardized by this hook. To enable it, install bun and run 'bun install'.
========================================
EOF
  exit 0
fi

SCRIPT_DIR=$(dirname "$0")
if ! "$BUN_CMD" "$SCRIPT_DIR/prepare-commit-msg.mjs" "$@" 2>&1; then
  cat <<'EOF' >&2
========================================
WARNING: prepare-commit-msg hook failed to set a standardized commit message.
You can still proceed with the merge; manually adjust the merge commit message
if you want. Check the hook output above for details.
========================================
EOF
fi

exit 0
