#!/usr/bin/env bash
export WORKON_HOME=~/.virtualenvs
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
workon webhooks
python run.py
deactivate