---
name: Config folders
description: Warn against editing .git, .obsidian, and .vscode unless explicitly requested
applyTo: ".git/**,.obsidian/**,.vscode/**"
---

# Config Folders Guidelines

- These folders contain auto-generated or sensitive configuration files. Do not edit them unless explicitly requested by the user.
- `.git/`: Git repository internals—editing may corrupt the repository.
- `.obsidian/`: Obsidian app settings, plugins, and workspace state—changes should be made in the Obsidian UI or after explicit user permission.
- `.vscode/`: VS Code workspace configuration—changes should be made in VS Code settings or after explicit user permission.
- If a task requires editing these folders, ask the user for explicit permission first.
