#!/usr/bin/env bash
set -euo pipefail

skill_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
state_dir="$skill_dir/state"

mkdir -p "$state_dir/clikernel" "$state_dir/ipython" "$state_dir/matplotlib"

export CLIKERNEL_STATE_DIR="$state_dir/clikernel"
export IPYTHONDIR="$state_dir/ipython"
export MPLCONFIGDIR="$state_dir/matplotlib"
export MPLBACKEND="${MPLBACKEND:-Agg}"

exec clikernel "$@"
