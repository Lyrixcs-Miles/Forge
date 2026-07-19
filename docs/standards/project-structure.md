# Project Structure Standard

Version: 1.0

---

# Purpose

This document defines the standard directory structure for every project created inside Forge.

The goal is consistency.

Every project should feel familiar regardless of language, framework, or size.

---

# Standard Structure

```
project-name/

├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore

├── docs/
├── src/
├── tests/

├── assets/
├── scripts/

├── configs/

└── .github/
```

---

# Directory Purpose

## src/

Contains the project's source code.

---

## docs/

Documentation related specifically to this project.

Examples:

- Architecture
- API documentation
- Design decisions
- User guides

---

## tests/

Automated tests.

Every production project should contain tests.

---

## assets/

Images, icons, diagrams, and other static resources.

---

## scripts/

Automation scripts.

Examples:

- build
- deploy
- setup
- backup

---

## configs/

Configuration files that don't belong in the project root.

---

## .github/

GitHub workflows, issue templates, pull request templates.

---

# Root Files

README.md

Required.

Explains:

- what the project is
- why it exists
- how to install
- how to use it

---

CHANGELOG.md

Tracks notable changes.

---

LICENSE

Defines usage rights.

---

.gitignore

Prevents unnecessary files from entering version control.

---

# Naming Rules

Folders use:

kebab-case

Example:

```
my-project
```

Never:

```
My Project
```

or

```
My_Project
```

---

# Exceptions

Very small utilities may omit:

- docs/
- assets/
- scripts/

Everything else should follow the standard.

---

# Principle

Consistency is more valuable than perfection.

A familiar structure reduces cognitive load and improves maintainability.
