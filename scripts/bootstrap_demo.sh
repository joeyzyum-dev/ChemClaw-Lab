#!/usr/bin/env bash
set -euo pipefail

python3 -m chemclaw_lab.cli init-db
python3 -m chemclaw_lab.cli seed-demo
python3 -m chemclaw_lab.cli status
