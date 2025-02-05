#!/usr/bin/env bash

set -eux

# delete hosts and groups in icinga
ansible-playbook playbooks/teardown.yml "$@"

# ensure test config is empty
ansible-playbook playbooks/empty_inventory_config.yml "$@"

export ANSIBLE_INVENTORY_ENABLED="t_systems_mms.icinga_director.icinga_director_inventory"

# test with default inventory file
ansible-playbook playbooks/test_invalid_inventory_config.yml "$@"

export ANSIBLE_INVENTORY=test.icinga_director_inventory.yaml

# test empty inventory config
ansible-playbook playbooks/test_invalid_inventory_config.yml "$@"

# generate inventory config and test using it
ansible-playbook playbooks/create_inventory_config.yml "$@"
ansible-playbook playbooks/test_populating_inventory.yml "$@"

# delete hosts and groups in icinga
ansible-playbook playbooks/teardown.yml "$@"

# generate inventory config with constructed features and test using it
ansible-playbook playbooks/create_inventory_config.yml -e "template='inventory_with_constructed.yml.j2'" "$@"
ansible-playbook playbooks/test_populating_inventory_with_constructed.yml "$@"

# delete hosts and groups in icinga
ansible-playbook playbooks/teardown.yml "$@"

# cleanup inventory config
ansible-playbook playbooks/empty_inventory_config.yml "$@"
