#!/bin/bash

# Script to decrypt MCP architecture document
# Password is required to decrypt

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# File paths
ENCRYPTED_FILE="MCP_ARCHITECTURE.md.enc"
DECRYPTED_FILE="MCP_ARCHITECTURE.md"

# Check if encrypted file exists
if [ ! -f "$ENCRYPTED_FILE" ]; then
    echo -e "${RED}Error: Encrypted file not found: $ENCRYPTED_FILE${NC}"
    exit 1
fi

# Prompt for password
echo -e "${YELLOW}Enter password to decrypt MCP architecture document:${NC}"
read -s PASSWORD

# Decrypt the file
echo -e "${YELLOW}Decrypting...${NC}"
openssl enc -aes-256-cbc -d -in "$ENCRYPTED_FILE" -out "$DECRYPTED_FILE" -pass pass:$PASSWORD

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Successfully decrypted to: $DECRYPTED_FILE${NC}"
    echo -e "${YELLOW}Remember to delete the decrypted file when done!${NC}"
    echo ""
    echo "To delete: rm $DECRYPTED_FILE"
else
    echo -e "${RED}✗ Decryption failed. Wrong password?${NC}"
    exit 1
fi
