#!/bin/bash
set -eo pipefail

command="$@"

make install

exec $command
