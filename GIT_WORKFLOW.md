# Git Workflow Guide

## Branch Structure

### Protected Branches
- **main**: Production-ready code (protected)
- **develop**: Integration branch for features

### Feature Branches
- **feature/**: New features (e.g., `feature/product-gallery`)
- **bugfix/**: Bug fixes (e.g., `bugfix/cart-calculation`)
- **hotfix/**: Emergency fixes for production

## Workflow Rules

### 1. Never Push Directly to Main
```bash
# ❌ Never do this
git push origin main

# ✅ Always create a feature branch
git checkout -b feature/your-feature-name
```

### 2. Feature Development Flow
```bash
# 1. Start from develop
git checkout develop
git pull origin develop

# 2. Create feature branch
git checkout -b feature/instagram-integration

# 3. Work on your feature
# ... make changes ...

# 4. Commit changes
git add .
git commit -m "feat: add Instagram feed integration"

# 5. Push to feature branch
git push origin feature/instagram-integration

# 6. Create Pull Request to develop (not main!)
```

### 3. Release Flow (develop → main)
```bash
# Only after testing in develop
# Create PR from develop to main
# Requires approval and passes all checks
```

## Branch Protection Rules (GitHub)

### For `main` branch:
1. Require pull request reviews (at least 1)
2. Dismiss stale pull request approvals
3. Require status checks to pass
4. Require branches to be up to date
5. Include administrators in restrictions
6. Restrict who can push to matching branches

### For `develop` branch:
1. Require pull request reviews
2. Require status checks to pass

## Backup Strategy

### Automated Backups
1. **Pre-merge to main**: Automatic backup created
2. **Storage**: Azure Blob Storage for long-term backups
3. **Retention**: 7 days local, 30 days cloud
4. **Naming**: `backup-main-YYYY-MM-DD-HH-mm-ss`

### Manual Backup Commands
```bash
# Create local backup before major changes
./scripts/backup.sh

# Restore from backup
./scripts/restore.sh backup-main-2024-01-20-14-30-00
```

## Commit Message Convention

Use conventional commits for clear history:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting)
- `refactor:` Code refactoring
- `test:` Test additions/changes
- `chore:` Maintenance tasks

### Examples:
```bash
git commit -m "feat: add WhatsApp integration for customer inquiries"
git commit -m "fix: resolve cart total calculation error"
git commit -m "docs: update API documentation for product endpoints"
```

## Emergency Procedures

### If You Accidentally Push to Main:
1. **Don't Panic!**
2. Contact team immediately
3. Run revert procedure:
   ```bash
   git revert HEAD
   git push origin main
   ```

### Restoring from Backup:
```bash
# List available backups
./scripts/list-backups.sh

# Restore specific backup
./scripts/restore.sh backup-main-2024-01-20-14-30-00
```

## Setup Instructions

### 1. Configure Git Hooks
```bash
# Install pre-push hook to prevent direct main pushes
cp scripts/git-hooks/pre-push .git/hooks/
chmod +x .git/hooks/pre-push
```

### 2. Set Up Branch Protection (GitHub)
1. Go to Settings → Branches
2. Add rule for `main` and `develop`
3. Configure protection rules as listed above

### 3. Configure Backup Automation
```bash
# Set up backup script
chmod +x scripts/backup.sh
chmod +x scripts/restore.sh

# Configure Azure credentials for cloud backup
cp .env.example .env
# Add your Azure Storage credentials
```

## Quick Reference

### Daily Development:
```bash
# Start your day
git checkout develop
git pull origin develop
git checkout -b feature/new-feature

# End your day
git add .
git commit -m "feat: description of changes"
git push origin feature/new-feature
```

### Before Creating PR:
1. ✅ All tests pass
2. ✅ Code is formatted
3. ✅ Documentation updated
4. ✅ Commit messages follow convention
5. ✅ Branch is up to date with develop

Remember: **Main branch is sacred. Always work in feature branches!**
