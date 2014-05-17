#!/bin/bash
#
# Setup a development repo
#

set -e

repo_name=working/repo
./bin/git-doc-new $repo_name

pushd $repo_name
virtualenv .venv
source .venv/bin/activate
pip install -e ../..
deactivate
popd

cp -r ./dev/template/* $repo_name
