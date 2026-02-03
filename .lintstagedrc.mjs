/**
 * @type {import('lint-staged').Configuration}
 */
export default {
  "**/*.{md,markdown}": [
    "pnpm run format:md"
  ]
};
