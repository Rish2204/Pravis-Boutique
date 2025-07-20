#!/bin/bash

# List available backups

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
BACKUP_DIR="$HOME/Developer/Automation-Playground-Backups"

echo -e "${CYAN}=== Available Backups ===${NC}"
echo ""

# Check if backup directory exists
if [ ! -d "$BACKUP_DIR" ]; then
    echo -e "${YELLOW}No backups found. Backup directory does not exist.${NC}"
    exit 0
fi

# List backups with size and date
echo -e "${GREEN}Local Backups:${NC}"
echo "------------------------"

# Find and list backup files
backup_count=0
while IFS= read -r backup_file; do
    if [ -f "$backup_file" ]; then
        backup_name=$(basename "$backup_file" .tar.gz)
        backup_size=$(du -h "$backup_file" | cut -f1)
        backup_date=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$backup_file" 2>/dev/null || stat -c "%y" "$backup_file" 2>/dev/null | cut -d' ' -f1,2)
        
        echo -e "${YELLOW}$backup_name${NC}"
        echo "  Size: $backup_size"
        echo "  Date: $backup_date"
        echo ""
        
        ((backup_count++))
    fi
done < <(find "$BACKUP_DIR" -name "backup-main-*.tar.gz" -type f | sort -r)

if [ $backup_count -eq 0 ]; then
    echo -e "${YELLOW}No backups found.${NC}"
else
    echo -e "${GREEN}Total backups: $backup_count${NC}"
fi

echo ""
echo "To restore a backup, use:"
echo "  ./scripts/restore.sh backup-main-YYYY-MM-DD-HH-MM-SS"
