#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 T-Systems Multimedia Solutions GmbH
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: icinga_host_template
short_description: Manage host templates in Icinga2
description:
   - Add or remove a host template to Icinga2 through the director API.
author: Michaela Mattes (@michaelamattes)
extends_documentation_fragment:
  - ansible.builtin.url
  - t_systems_mms.icinga_director.common_options
version_added: '1.2.0'
notes:
  - This module supports check mode.
options:
  state:
    description:
      - Apply feature state.
    choices: [ "present", "absent" ]
    default: present
    type: str
  object_name:
    description:
      - Icinga object name for this host template.
      - This is usually a fully qualified host name but it could basically be any kind of string.
      - To make things easier for your users we strongly suggest to use meaningful names for templates.
      - For example "generic-host" is ugly, "Standard Linux Server" is easier to understand.
    aliases: ['name']
    required: true
    type: str
  display_name:
    description:
      - Alternative name for this host.
      - Might be a host alias or and kind of string helping your users to identify this host.
    type: str
  address:
    description:
      - Host address. Usually an IPv4 address, but may be any kind of address your check plugin is able to deal with.
    type: str
  address6:
    description:
      - Host IPv6 address. Usually an IPv64 address, but may be any kind of address your check plugin is able to deal with.
    type: str
  groups:
    description:
      - Hostgroups that should be directly assigned to this node. Hostgroups can be useful for various reasons.
      - You might assign service checks based on assigned hostgroup. They are also often used as an instrument to enforce restricted views in Icinga Web 2.
      - Hostgroups can be directly assigned to single hosts or to host templates.
      - You might also want to consider assigning hostgroups using apply rules.
    type: list
    elements: str
    default: []
  check_command:
    description:
      - The name of the check command.
      - Though this is not required to be defined in the director, you still have to supply a check_command in a host or host-template.
    type: str
  event_command:
    description:
      - Event command for host which gets called on every check execution if one of these conditions matches
      - The host is in a soft state
      - The host state changes into a hard state
      - The host state recovers from a soft or hard state to OK/Up
    type: str
  check_interval:
    description:
      - Your regular check interval.
    type: str
  retry_interval:
    description:
      - Retry interval, will be applied after a state change unless the next hard state is reached.
    type: str
  disabled:
    description:
      - Disabled objects will not be deployed.
    default: False
    type: bool
    choices: [True, False]
  imports:
    description:
      - Choose a host-template.
    type: list
    elements: str
  max_check_attempts:
    description:
      - Defines after how many check attempts a new hard state is reached.
    type: str
  zone:
    description:
      - Set the zone.
    type: str
  vars:
    description:
      - Custom properties of the host.
    type: "dict"
  notes:
    description:
      - Additional notes for this object.
    type: str
    version_added: '1.8.0'
  notes_url:
    description:
      - An URL pointing to additional notes for this object.
      - Separate multiple urls like this "'http://url1' 'http://url2'".
      - Maximum length is 255 characters.
    type: str
    version_added: '1.8.0'
  has_agent:
    description:
      - Whether this host has the Icinga 2 Agent installed.
    type: bool
    choices: [True, False]
    version_added: '1.9.0'
  master_should_connect:
    description:
      - Whether the parent (master) node should actively try to connect to this agent.
    type: bool
    choices: [True, False]
    version_added: '1.9.0'
  accept_config:
    description:
      - Whether the agent is configured to accept config.
    type: bool
    choices: [True, False]
    version_added: '1.9.0'
  command_endpoint:
    description:
      - The endpoint where commands are executed on.
    type: str
  append:
    description:
      - Do not overwrite the whole object but instead append the defined properties.
      - Note - Appending to existing vars, imports or any other list/dict is not possible. You have to overwrite the complete list/dict.
      - Note - Variables that are set by default will also be applied, even if not set.
    type: bool
    choices: [True, False]
    version_added: '1.25.0'
  enable_notifications:
    description:
      - Whether to send notifications for this object.
    type: bool
    choices: [True, False]
  enable_active_checks:
    description:
      - Whether to actively check this object.
    type: bool
    choices: [True, False]
  enable_passive_checks:
    description:
      - Whether to accept passive check results for this object.
    type: bool
    choices: [True, False]
  enable_event_handler:
    description:
      - Whether to enable event handlers this object.
    type: bool
    choices: [True, False]
  enable_flapping:
    description:
      - Whether flap detection is enabled on this object.
    type: bool
    choices: [True, False]
  enable_perfdata:
    description:
      - Whether to process performance data provided by this object.
    type: bool
    choices: [True, False]
  volatile:
    description:
      - Whether this check is volatile.
    type: bool
    choices: [True, False]
  check_period:
    description:
      - The name of a time period which determines when this object should be monitored. Not limited by default.
    type: str
  check_timeout:
    description:
      - Check command timeout in seconds. Overrides the CheckCommand's timeout attribute
    type: str
  flapping_threshold_high:
    description:
      - Flapping upper bound in percent for a service to be considered flapping
    type: str
  flapping_threshold_low:
    description:
      - Flapping lower bound in percent for a service to be considered not flapping
    type: str
  icon_image:
    description:
      - An URL pointing to an icon for this object. Try "tux.png" for icons relative to public/img/icons or "cloud" (no extension) for items from the Icinga icon font
    type: str
  icon_image_alt
    description:
      - Alternative text to be shown in case above icon is missing
    type: str
"""

EXAMPLES = """
- name: Create host template
  t_systems_mms.icinga_director.icinga_host_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: foohosttemplate
    display_name: foohosttemplate
    disabled: false
    check_command: dummy
    check_interval: 90s
    retry_interval: 30s
    groups:
      - "foohostgroup"
    imports:
      - ''
    has_agent: true
    master_should_connect: true
    max_check_attempts: 3
    accept_config: true
    command_endpoint: fooendpoint
    enable_notifications: true
    enable_active_checks: true
    enable_passive_checks: false
    enable_event_handler: false
    enable_flapping: false
    enable_perfdata: false
    volatile: false
    check_period: "24x7"
    check_timeout: 60
    flapping_threshold_high: "30.0"
    flapping_threshold_low: "25.0"
    icon_image: "http://url1"
    icon_image_alt: "alt text"

- name: Update host template
  t_systems_mms.icinga_director.icinga_host_template:
    state: present
    url: "{{ icinga_url }}"
    url_username: "{{ icinga_user }}"
    url_password: "{{ icinga_pass }}"
    object_name: foohosttemplate
    notes: "example note"
    notes_url: "'http://url1' 'http://url2'"
    append: true
"""

RETURN = r""" # """

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import url_argument_spec
from ansible_collections.t_systems_mms.icinga_director.plugins.module_utils.icinga import (
    Icinga2APIObject,
)


# ===========================================
# Module execution.
#
def main():
    # use the predefined argument spec for url
    argument_spec = url_argument_spec()
    # add our own arguments
    argument_spec.update(
        state=dict(default="present", choices=["absent", "present"]),
        url=dict(required=True),
        append=dict(type="bool", choices=[True, False]),
        object_name=dict(required=True, aliases=["name"]),
        display_name=dict(required=False),
        groups=dict(type="list", elements="str", default=[], required=False),
        check_command=dict(required=False),
        check_interval=dict(required=False),
        retry_interval=dict(required=False),
        imports=dict(type="list", elements="str", required=False),
        disabled=dict(type="bool", default=False, choices=[True, False]),
        address=dict(required=False),
        address6=dict(required=False),
        zone=dict(required=False, default=None),
        vars=dict(type="dict", default=None),
        notes=dict(type="str", required=False),
        notes_url=dict(type="str", required=False),
        has_agent=dict(type="bool", choices=[True, False]),
        master_should_connect=dict(type="bool", choices=[True, False]),
        max_check_attempts=dict(required=False),
        accept_config=dict(type="bool", choices=[True, False]),
        event_command=dict(type="str", required=False),
        command_endpoint=dict(type="str", required=False),
        enable_notifications=dict(type="bool", choices=[True, False], required=False),
        enable_active_checks=dict(type="bool", choices=[True, False], required=False),
        enable_passive_checks=dict(type="bool", choices=[True, False], required=False),
        enable_event_handler=dict(type="bool", choices=[True, False], required=False),
        enable_flapping=dict(type="bool", choices=[True, False], required=False),
        enable_perfdata=dict(type="bool", choices=[True, False], required=False),
        volatile=dict(type="bool", choices=[True, False], required=False),
        check_period=dict(type="str", required=False),
        check_timeout=dict(type="str", required=False),
        flapping_threshold_high=dict(type="str", required=False),
        flapping_threshold_low=dict(type="str", required=False),
        icon_image=dict(type="str", required=False),
        icon_image_alt=dict(type="str", required=False),
    )

    # Define the main module
    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )

    data_keys = [
        "object_name",
        "display_name",
        "groups",
        "check_command",
        "check_interval",
        "retry_interval",
        "imports",
        "disabled",
        "address",
        "address6",
        "zone",
        "vars",
        "notes",
        "notes_url",
        "has_agent",
        "master_should_connect",
        "max_check_attempts",
        "accept_config",
        "event_command",
        "command_endpoint",
        "enable_notifications",
        "enable_active_checks",
        "enable_passive_checks",
        "enable_event_handler",
        "enable_flapping",
        "enable_perfdata",
        "volatile",
        "check_period",
        "check_timeout",
        "flapping_threshold_high",
        "flapping_threshold_low",
        "icon_image",
        "icon_image_alt",
    ]

    data = {}

    if module.params["append"]:
        for k in data_keys:
            if module.params[k]:
                data[k] = module.params[k]
    else:
        for k in data_keys:
            data[k] = module.params[k]

    data["object_type"] = "template"

    icinga_object = Icinga2APIObject(module=module, path="/host", data=data)

    changed, diff = icinga_object.update(module.params["state"])
    module.exit_json(
        changed=changed,
        diff=diff,
    )


# import module snippets
if __name__ == "__main__":
    main()
