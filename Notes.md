# Git + Odoo Dev Cheat Sheet (Server Working Copy)

This project uses:
- Server as working copy
- GitHub as central repository
- VS Code Remote SSH as editor

---

## Where am I / current state

pwd
# Shows current directory (must be inside module folder)

git status
# Shows modified, staged, untracked files and branch

git branch
# Shows current branch

---

## Daily development workflow

git status
# Review what changed

git add .
# Stage all changes

git commit -m "CAPA: short description"
# Commit changes locally (small, descriptive commits)

git push
# Push commits to GitHub (central repo)

---

## Branching (lightweight)

git checkout dev
# Switch to dev branch for active work

git checkout main
# Switch to stable branch

git checkout -b dev
# Create dev branch (one time)

---

## Merge dev → main (when stable)

git checkout main
# Move to stable branch

git merge dev
# Bring in tested changes

git push
# Publish stable state to GitHub

git checkout dev
# Return to development

---

## Undo / recovery

git restore .
# Discard all uncommitted local changes

git reset --soft HEAD~1
# Undo last commit but keep changes staged

git reset --hard HEAD~1
# Undo last commit AND discard changes (dangerous)

---

## Safety snapshots (highly recommended)

git tag v0.1
# Create a tag at known-good state

git push --tags
# Push tags to GitHub

git checkout v0.1
# Roll back working tree to tagged version

---

## Odoo-specific actions

docker compose restart odoo
# Restart Odoo service (use when models, security, or manifest change)

docker compose logs odoo
# View Odoo logs (errors, module loading, tracebacks)

---

## When to restart Odoo

- New model or field            → YES
- Changed security rules        → YES
- Changed __manifest__.py       → YES
- Python logic behaving oddly   → YES
- XML view change only          → usually NO

---

## Install / update modules

Apps → Update Apps List
# Required after adding or changing addons

Apps → Search module → Upgrade
# Apply code changes to existing module

---

## Golden rules

- Always work inside the module directory
- Commit often, push when stable
- Never edit production this way
- GitHub is source of truth
