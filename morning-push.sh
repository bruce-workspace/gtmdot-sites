#!/bin/bash
# Morning push — runs all unpushed intake branches at once.
# Jesse, this is what I built overnight while git push was blocked.
# Run this from the gtmdot-sites directory.
#
# Usage: ./morning-push.sh
#
# This will push every local intake/* branch to origin.

set -e
cd "$(dirname "$0")"

echo "=== Pushing all unpushed intake branches ==="

UNPUSHED=$(git branch --list "intake/*" --format="%(refname:short) %(upstream:short)" | awk '$2 == "" {print $1}')
ALREADY_PUSHED=$(git branch --list "intake/*" --format="%(refname:short) %(upstream:short)" | awk '$2 != "" {print $1}')

if [ -z "$UNPUSHED" ]; then
  echo "No unpushed intake branches. Everything is already on origin."
  # But still push main in case there are messages/ updates
  git checkout main
  git push origin main
  echo "Pushed main (in case of message/proposal updates)."
  exit 0
fi

echo ""
echo "Unpushed branches:"
echo "$UNPUSHED"
echo ""
echo "Already pushed branches:"
echo "$ALREADY_PUSHED"
echo ""

read -p "Push all unpushed branches? (y/n): " confirm
if [ "$confirm" != "y" ]; then
  echo "Aborted."
  exit 1
fi

# Push each unpushed branch
echo "$UNPUSHED" | while read -r branch; do
  if [ -n "$branch" ]; then
    echo "--- Pushing $branch ---"
    git push -u origin "$branch"
  fi
done

# Also push main so any new messages/ commits go up
echo "--- Pushing main (messages + briefs) ---"
git checkout main
git push origin main

echo ""
echo "=== DONE ==="
echo "All intake branches + main pushed."
echo "Mac Mini will pick up on next cron run (within 10 min)."
