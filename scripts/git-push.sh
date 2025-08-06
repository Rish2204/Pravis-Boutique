#!/bin/bash

# Git push helper for Pravis Boutique
echo "🚀 Pushing to GitHub..."

# Add all changes
git add .

# Commit with message
echo "Enter commit message: "
read commit_msg
git commit -m "$commit_msg"

# Push to current branch
current_branch=$(git branch --show-current)
echo "Pushing to branch: $current_branch"
git push origin $current_branch

echo "✅ Push complete!"
echo "View at: https://github.com/Rish2204/Pravis-Boutique"
