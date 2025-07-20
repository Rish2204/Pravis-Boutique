#!/bin/bash

# Backup script for main branch
# Creates local and Azure Blob Storage backups

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
BACKUP_DIR="$HOME/Developer/Automation-Playground-Backups"
TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
BACKUP_NAME="backup-main-$TIMESTAMP"
REPO_PATH="/Users/rish/Developer/Automation-Playground"

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

echo -e "${YELLOW}Starting backup process...${NC}"

# Get current branch
cd "$REPO_PATH"
CURRENT_BRANCH=$(git branch --show-current)

# Stash any uncommitted changes
echo "Stashing uncommitted changes..."
git stash

# Checkout main branch
echo "Switching to main branch..."
git checkout main
git pull origin main

# Create backup
echo -e "${YELLOW}Creating backup: $BACKUP_NAME${NC}"
cp -R "$REPO_PATH" "$BACKUP_DIR/$BACKUP_NAME"

# Remove .git directory from backup to save space
rm -rf "$BACKUP_DIR/$BACKUP_NAME/.git"

# Create tar archive
cd "$BACKUP_DIR"
tar -czf "$BACKUP_NAME.tar.gz" "$BACKUP_NAME"
rm -rf "$BACKUP_NAME"

echo -e "${GREEN}✓ Local backup created: $BACKUP_DIR/$BACKUP_NAME.tar.gz${NC}"

# Azure Blob Storage upload (if credentials are configured)
if [ -f "$REPO_PATH/.env" ]; then
    source "$REPO_PATH/.env"
    if [ ! -z "$AZURE_STORAGE_CONNECTION_STRING" ]; then
        echo -e "${YELLOW}Uploading to Azure Blob Storage...${NC}"
        # Note: This requires Azure CLI to be installed
        # az storage blob upload \
        #     --connection-string "$AZURE_STORAGE_CONNECTION_STRING" \
        #     --container-name "backups" \
        #     --name "$BACKUP_NAME.tar.gz" \
        #     --file "$BACKUP_DIR/$BACKUP_NAME.tar.gz"
        echo -e "${GREEN}✓ Cloud backup would be created here (Azure CLI required)${NC}"
    fi
fi

# Clean up old local backups (keep only last 7 days)
echo "Cleaning up old backups..."
find "$BACKUP_DIR" -name "backup-main-*.tar.gz" -mtime +7 -delete

# Return to original branch
cd "$REPO_PATH"
git checkout "$CURRENT_BRANCH"
git stash pop 2>/dev/null || true

echo -e "${GREEN}✅ Backup completed successfully!${NC}"
echo -e "Backup location: $BACKUP_DIR/$BACKUP_NAME.tar.gz"
