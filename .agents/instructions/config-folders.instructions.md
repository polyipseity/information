---
name: Config folders
description: Warn against editing .git, .obsidian, .vscode, and markdownlint configs unless explicitly requested
applyTo: ".git/**,.obsidian/**,.vscode/**,**/.markdownlint*"
---

# Config Folders Guidelines

- These folders and files contain auto-generated or sensitive configuration. Do not edit them unless explicitly requested by the user.
- `.git/`: Git repository internals—editing may corrupt the repository.
- `.markdownlint*` files: markdownlint configuration. Never add, remove, or modify rules in these files unless the user explicitly asks. This is a hard ban — markdownlint config is owned by the user.
- `.obsidian/`: Obsidian app settings, plugins, and workspace state—changes should be made in the Obsidian UI or after explicit user permission.
- `.vscode/`: VS Code workspace configuration—changes should be made in VS Code settings or after explicit user permission.
- If a task requires editing these folders, ask the user for explicit permission first.
