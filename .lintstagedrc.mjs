import { FILE_GLOBS as MD_FILE_GLOBS } from "./.markdownlint-cli2.mjs";

/**
 * Convert `FILE_GLOBS` into a brace-style combined pattern.
 */
const MD_GLOB_KEY = `**/*.{${MD_FILE_GLOBS.map((g) => g.replace("**/*.", "")).join(",")}}`;

/**
 * Lint-staged configuration.
 *
 * Note: lint-staged appends the list of staged file paths to the command it runs.
 * For commands that must receive that file list (formatters or linters that
 * operate on provided files), prefer invoking the underlying CLI directly so
 * lint-staged's file arguments are forwarded. Examples: `prettier --write`,
 * `markdownlint-cli2 --fix`, `python -m scripts.format`, `python -m ruff check --fix`.
 * Avoid `pnpm run <script>` for commands that must operate on the staged file
 * list because `pnpm run` may not reliably forward arbitrary file arguments.
 *
 * @type {import('lint-staged').Configuration}
 */
export default {
  [MD_GLOB_KEY]: ["markdownlint-cli2 --fix"],
  "**/*.{astro,cjs,css,csv,gql,graphql,hbs,html,js,jsx,json,json5,jsonc,jsonl,less,mjs,pcss,sass,scss,svelte,styl,ts,tsx,vue,xml,yaml,yml}":
    ["prettier --write"],
  "**/*.{py,pyi,pyw,pyx}": [
    // Run pyright and each Python formatter as its own command so lint-staged appends
    // the staged file list to each invocation (pyright, ruff, isort, black).
    "pyright",
    "python -m ruff check --fix",
    "python -m isort",
    "python -m black",
  ],
};
