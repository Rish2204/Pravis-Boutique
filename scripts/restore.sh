#!/bin/bash

# Restore script for repository backups

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
BACKUP_DIR="$HOME/Developer/Automation-Playground-Backups"
REPO_PATH="/Users/rish/Developer/Automation-Playground"

# Check if backup name provided
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: Please provide backup name${NC}"
    echo "Usage: ./restore.sh backup-main-YYYY-MM-DD-HH-MM-SS"
    echo ""
    echo "Available backups:"
    ls -la "$BACKUP_DIR" | grep "backup-main-"
    exit 1
fi

BACKUP_NAME="$1"
BACKUP_FILE="$BACKUP_DIR/$BACKUP_NAME.tar.gz"

# Check if backup exists
if [ ! -f "$BACKUP_FILE" ]; then
    echo -e "${RED}Error: Backup file not found: $BACKUP_FILE${NC}"
    echo ""
    echo "Available backups:"
    ls -la "$BACKUP_DIR" | grep "backup-main-"
    exit 1
fi

# Confirm restore
echo -e "${YELLOW}⚠️  WARNING: This will restore the repository to a previous state!${NC}"
echo -e "Backup to restore: ${YELLOW}$BACKUP_NAME${NC}"
echo ""
read -p "Are you sure you want to continue? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Restore cancelled."
    exit 0
fi

# Create emergency backup of current state
echo -e "${YELLOW}Creating emergency backup of current state...${NC}"
EMERGENCY_BACKUP="emergency-backup-$(date +%Y-%m-%d-%H-%M-%S)"
cp -R "$REPO_PATH" "$BACKUP_DIR/$EMERGENCY_BACKUP"

# Save current git directory
echo "Saving current git history..."
cp -R "$REPO_PATH/.git" "$BACKUP_DIR/$EMERGENCY_BACKUP-git"

# Extract backup
echo -e "${YELLOW}Extracting backup...${NC}"
cd "$BACKUP_DIR"
tar -xzf "$BACKUP_FILE"

# Restore files (keeping .git directory)
echo -e "${YELLOW}Restoring files...${NC}"
rsync -av --exclude='.git' "$BACKUP_DIR/$BACKUP_NAME/" "$REPO_PATH/"

# Clean up extracted backup
rm -rf "$BACKUP_DIR/$BACKUP_NAME"

# Show what changed
cd "$REPO_PATH"
echo ""
echo -e "${YELLOW}Changes from restore:${NC}"
git status

echo ""
echo -e "${GREEN}✅ Restore completed successfully!${NC}"
echo -e "Emergency backup saved at: $BACKUP_DIR/$EMERGENCY_BACKUP"
echo ""
echo "Next steps:"
echo "1. Review the changes with: git status"
echo "2. Commit the restore: git commit -am \"Restored from $BACKUP_NAME\""
echo "3. If needed, recover emergency backup from: $BACKUP_DIR/$EMERGENCY_BACKUP"
