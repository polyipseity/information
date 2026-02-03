import { FILE_GLOBS } from './.markdownlint-cli2.mjs';

/**
 * Convert `FILE_GLOBS` into a brace-style combined pattern.
 */
const MD_GLOB_KEY = `**/*.{${FILE_GLOBS.map(g => g.replace('**/*.', '')).join(',')}}`;

/**
 * @type {import('lint-staged').Configuration}
 */
export default {
  [MD_GLOB_KEY]: [
    "pnpm run format:md",
  ],
};
