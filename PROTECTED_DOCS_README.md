# Protected Documents

This repository contains encrypted strategic documents that outline our MCP (Model Context Protocol) architecture and future plans.

## Encrypted Files

- `MCP_ARCHITECTURE.md.enc` - Detailed MCP server architecture and implementation plan

## How to Access

To decrypt and read the protected documents:

```bash
# Decrypt the MCP architecture document
./scripts/decrypt-mcp-doc.sh
```

You will be prompted for the password. Contact the repository owner for access.

## Security Notes

1. **Never commit decrypted files** - The `.gitignore` is configured to prevent this
2. **Delete after reading** - Remove decrypted files when done: `rm MCP_ARCHITECTURE.md`
3. **Password protection** - Do not share passwords in plain text or commit them

## Why These Are Protected

These documents contain:
- Strategic business plans
- API integration strategies
- Competitive advantage information
- Implementation roadmaps

Keeping them encrypted ensures our plans remain confidential while still being version controlled.
