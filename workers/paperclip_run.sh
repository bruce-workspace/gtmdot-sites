#!/bin/zsh
set -euo pipefail

export PAPERCLIP_HOME="/Users/bruce/.openclaw/workspace/paperclip-sandbox-home"
export PAPERCLIP_INSTANCE_ID="gtmdot-sandbox"
export PORT="3199"
export PAPERCLIP_OPEN_ON_LISTEN="false"

INSTANCE_DIR="$PAPERCLIP_HOME/instances/$PAPERCLIP_INSTANCE_ID"
ENV_FILE="$INSTANCE_DIR/.env"
PAPERCLIP_BIN="$PAPERCLIP_HOME/.npm/_npx/43414d9b790239bb/node_modules/paperclipai/dist/index.js"
NODE_BIN="/opt/homebrew/opt/node/bin/node"

if [[ -f "$ENV_FILE" ]]; then
  set -a
  source "$ENV_FILE"
  set +a
fi

exec "$NODE_BIN" "$PAPERCLIP_BIN" run --bind loopback
