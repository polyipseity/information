import { FILE_GLOBS as MD_FILE_GLOBS } from './.markdownlint-cli2.mjs';

/**
 * Convert `FILE_GLOBS` into a brace-style combined pattern.
 */
const MD_GLOB_KEY = `**/*.{${MD_FILE_GLOBS.map(g => g.replace('**/*.', '')).join(',')}}`;

/**
 * @type {import('lint-staged').Configuration}
 *
 * Note: lint-staged appends staged file paths to the configured command.
 * Prefer invoking the underlying CLI directly (not an npm/pnpm script wrapper)
 * so those file paths are forwarded to the tool (e.g., "markdownlint-cli2 --fix").
 */
export default {
  [MD_GLOB_KEY]: [
    "markdownlint-cli2 --fix",
  ],
};
