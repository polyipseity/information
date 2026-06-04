#!/usr/bin/env bun
/**
 * scripts/standardize-fork-merge-message.mjs
 * ---------------------------------
 * Standardize merge commit messages when merging into a `forks/*` branch.
 *
 * Usage:
 *   bun scripts/standardize-fork-merge-message.mjs <commitMsgFile>
 *
 * Arguments / environment:
 * - commitMsgFile (argv[2]): path to the file containing the current commit
 *   message (always passed by Git / prek).
 * - PRE_COMMIT_COMMIT_MSG_SOURCE: the Git commit source string (`merge`,
 *   `template`, etc.), set by prek for `prepare-commit-msg` stage hooks.
 *
 * Behavior:
 * - If `commitSource !== 'merge'` the hook exits with code 0 (no-op).
 * - If the current branch does not start with `forks/`, the hook exits no-op.
 * - Attempts to detect the source ref by reading `.git/MERGE_HEAD` and
 *   resolving refs that contain that SHA. If a ref is found, it is used
 *   as the branch name in the standardized commit message; otherwise `main`
 *   is used as a sensible default.
 *
 * Environment:
 * - PRE_COMMIT_COMMIT_MSG_SOURCE: commit source string, set by prek for
 *   `prepare-commit-msg` stage hooks.
 * - Set `DEBUG=1` to enable debug logging to stderr.
 *
 * Implementation notes:
 * - Functions are small and exported for easier unit testing and maintenance.
 * - Keeps synchronous operations for git hook predictability.
 */

import { execSync } from "child_process";
import { readFileSync, writeFileSync } from "fs";
import path from "path";

const [, , commitMsgFile] = process.argv;
// prek passes the Git commit-source arg exclusively via the env var for
// `prepare-commit-msg` stage hooks — never as a positional argument.
const commitSource = process.env.PRE_COMMIT_COMMIT_MSG_SOURCE ?? "";

function debug(msg) {
  if (process.env.DEBUG === "1")
    console.error(`[standardize-fork-merge-message] ${msg}`);
}

/**
 * Run a git command and return stdout trimmed, or an empty string on error.
 * @param {string} cmd - git command without leading 'git '.
 * @returns {string}
 */
function git(cmd) {
  try {
    return execSync(`git ${cmd}`, {
      encoding: "utf8",
      stdio: ["pipe", "pipe", "ignore"],
    })
      .toString()
      .trim();
  } catch (e) {
    debug(
      `git command failed: git ${cmd} -> ${e && e.message ? e.message : String(e)}`,
    );
    return "";
  }
}

/**
 * Read the MERGE_HEAD file and return the SHA (first line), or an empty string.
 * @param {string} gitDir - path to the .git directory
 * @returns {string}
 */
function readMergeHeadSha(gitDir) {
  try {
    const mergeHeadPath = path.join(gitDir, "MERGE_HEAD");
    const mergeSha = readFileSync(mergeHeadPath, "utf8")
      .split(/\r?\n/)[0]
      .trim();
    debug(`read MERGE_HEAD: ${mergeSha || "<empty>"}`);
    return mergeSha || "";
  } catch (err) {
    debug(
      `error reading MERGE_HEAD: ${err && err.message ? err.message : String(err)}`,
    );
    return "";
  }
}

/**
 * Given a commit SHA, try to find a human-readable ref (branch or remote ref)
 * that contains it. Returns the first ref found or empty string.
 * @param {string} sha
 * @returns {string}
 */
function detectSourceRef(sha) {
  if (!sha) return "";
  const refList = git(
    `for-each-ref --format='%(refname:short)' --contains ${sha} refs/remotes refs/heads`,
  );
  if (!refList) return "";
  const ref = refList.split(/\r?\n/).find(Boolean);
  if (!ref) return "";
  const src = ref.replace(/^remotes\//, "").replace(/^['"]|['"]$/g, "");
  debug(`detected source ref: ${src}`);
  return src;
}

/**
 * Write the standardized commit message to the given file.
 * If writing fails, print a prominent warning but do not abort the merge.
 * @param {string} filePath
 * @param {string} src
 */
function writeCommitMessage(filePath, src) {
  try {
    writeFileSync(filePath, `chore(sync): merge from \`${src}\`\n`, "utf8");
    debug(`wrote standardized commit message to ${filePath}`);
  } catch (err) {
    // Prominent warning but allow the merge/commit to continue
    console.error("\n========================================");
    console.error(
      "WARNING: prepare-commit-msg could not write the standardized commit message.",
    );
    console.error(
      "You can continue the merge, but the commit message will not be automatically updated.",
    );
    console.error(
      "Suggested fixes: ensure repository files are writable or run:",
    );
    console.error(
      '  git commit --amend -m "chore(sync): merge from `<branch>`"',
    );
    console.error("========================================\n");
    debug(
      `failed to write commit message: ${err && err.message ? err.message : String(err)}`,
    );
  }
}

/**
 * Main execution flow.
 */
function main() {
  if (commitSource !== "merge") {
    debug(`commit source is '${commitSource}', not 'merge' - exiting`);
    process.exit(0);
  }

  const branch = git("rev-parse --abbrev-ref HEAD");
  debug(`current branch: ${branch || "<unknown>"}`);
  if (!branch || !branch.startsWith("forks/")) {
    debug("branch does not match forks/* - exiting");
    process.exit(0);
  }

  let src = "main";
  const gitdir = git("rev-parse --git-dir");
  if (gitdir) {
    const mergeSha = readMergeHeadSha(gitdir);
    if (mergeSha) {
      const detected = detectSourceRef(mergeSha);
      if (detected) src = detected;
    }
  }

  writeCommitMessage(commitMsgFile, src);
  process.exit(0);
}

// When executed directly we run main(). Export helpers to make the module testable.
if (
  import.meta.url === `file://${process.argv[1]}` ||
  (process.argv[1] && process.argv[1].endsWith(".mjs"))
) {
  try {
    main();
  } catch (err) {
    console.error("\n========================================");
    console.error(
      "WARNING: prepare-commit-msg hook encountered an unexpected error.",
    );
    console.error(
      "The merge/commit will continue but the message may not be standardized.",
    );
    console.error(`Error: ${err && err.message ? err.message : String(err)}`);
    console.error("========================================\n");
    process.exit(0);
  }
}

export {
  debug,
  detectSourceRef,
  git,
  main,
  readMergeHeadSha,
  writeCommitMessage,
};
