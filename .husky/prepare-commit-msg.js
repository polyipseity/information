#!/usr/bin/env node
'use strict';
/*
 * .husky/prepare-commit-msg.js
 * Sets a standardized commit message when merging into branches matching `forks/*`.
 * Usage: node .husky/prepare-commit-msg.js <commitMsgFile> <commitSource>
 *
 * Cross-platform notes:
 * - Runs with Node (works on Linux/macOS and Windows PowerShell/CMD/Git Bash)
 * - Enable debug output with: HUSKY_DEBUG=1
 */

const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

const [,, commitMsgFile, commitSource] = process.argv;

function debug(msg) {
  if (process.env.HUSKY_DEBUG === '1') console.error(`[prepare-commit-msg] ${msg}`);
}

if (commitSource !== 'merge') {
  debug(`commit source is '${commitSource}', not 'merge' - exiting`);
  process.exit(0);
}

function git(cmd) {
  try {
    return execSync(`git ${cmd}`, { encoding: 'utf8', stdio: ['pipe','pipe','ignore'] }).trim();
  } catch (e) {
    return '';
  }
}

const branch = git('rev-parse --abbrev-ref HEAD');
debug(`current branch: ${branch || '<unknown>'}`);
if (!branch || !branch.startsWith('forks/')) {
  debug('branch does not match forks/* - exiting');
  process.exit(0);
}

let src = 'main';
const gitdir = git('rev-parse --git-dir');
if (gitdir) {
  try {
    const mergeHeadPath = path.join(gitdir, 'MERGE_HEAD');
    const mergeSha = fs.readFileSync(mergeHeadPath, 'utf8').split(/\r?\n/)[0].trim();
    if (mergeSha) {
      debug(`merge SHA: ${mergeSha}`);
      const refList = git(`for-each-ref --format='%(refname:short)' --contains ${mergeSha} refs/remotes refs/heads`);
      if (refList) {
        const ref = refList.split(/\r?\n/).find(Boolean);
        if (ref) {
          src = ref.replace(/^remotes\//, '');
          debug(`detected source ref: ${src}`);
        }
      }
    }
  } catch (err) {
    debug(`error reading MERGE_HEAD or resolving ref: ${err && err.message ? err.message : String(err)}`);
  }
}

try {
  fs.writeFileSync(commitMsgFile, `chore(sync); merge from \`${src}\`\n`, 'utf8');
  debug(`wrote standardized commit message to ${commitMsgFile}`);
} catch (err) {
  // Prominent warning but allow the merge/commit to continue
  console.error('\n========================================');
  console.error('WARNING: prepare-commit-msg could not write the standardized commit message.');
  console.error('You can continue the merge, but the commit message will not be automatically updated.');
  console.error('Suggested fixes: ensure repository files are writable or run:');
  console.error("  git commit --amend -m \"chore(sync); merge from '<branch>'\"");
  console.error('========================================\n');
  debug(`failed to write commit message: ${err && err.message ? err.message : String(err)}`);
}

process.exit(0);
