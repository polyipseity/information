/**
 * @type {import('lint-staged').Configuration}
 */
export default {
  "**/*.{md,mdoc,mdown,mdx,mkd,mkdn,markdown,rmd}": [
    "pnpm run format:md",
  ],
};
