#!/bin/bash
# Auto-update Regular Meetup dates in signup2.html and push to GitHub
# Runs every Friday

REPO_DIR="/tmp/symphony"
WORKSPACE_DIR="$HOME/.openclaw/workspaces/ansonlo"

cd "$REPO_DIR" || exit 1

# Pull latest changes
git pull origin main

# Run the update script
python3 update-dates.py

# Check if there are changes
if git diff --quiet signup2.html; then
    echo "No changes to signup2.html dates"
    exit 0
fi

# Commit and push
git config user.email "openclaw-bot@symphony.dev"
git config user.name "OpenClaw Bot"
git add signup2.html
git commit -m "Auto-update: Refresh Regular Meetup dates ($(date +%Y-%m-%d))"

# Get token and push
TOKEN=$(cat "$WORKSPACE_DIR/.github-credentials.json" | grep -o '"token": *"[^"]*"' | cut -d'"' -f4)
git push https://x-access-token:$TOKEN@github.com/kingfungleung-cylinderBear/symphony.git main

echo "✅ Regular Meetup dates updated and pushed"
