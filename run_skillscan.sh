#!/usr/bin/env bash
set -e

# go to the folder where the script is (project root)
cd "$(dirname "$0")"

# activate the venv, if it exists
if [ -d ".venv" ]; then
  source .venv/bin/activate
fi

# run SkillScan with the example files
skillscan run \
  --jd ./src/samples/jd.txt \
  --profile ./src/samples/profile.json \
  --out ./reports \
  --verbose
