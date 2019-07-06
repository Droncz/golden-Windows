#!/usr/local/bin/zsh
source /home/psvika/ansible/bin/activate && ANSIBLE_FORCE_COLOR=1 PYTHONUNBUFFERED=1 /home/psvika/ansible/bin/ansible-playbook "$@"
