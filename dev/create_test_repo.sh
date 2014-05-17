#!/bin/bash
#
# Setup a development repo
#

set -e

repo_name=working/repo
./bin/git-doc-new $repo_name

cd $repo_name
virtualenv .venv
source .venv/bin/activate
pip install -e ../..
deactivate


