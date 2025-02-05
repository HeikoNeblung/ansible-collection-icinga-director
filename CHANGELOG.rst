===========================================
T_Systems_Mms.Icinga_Director Release Notes
===========================================

.. contents:: Topics


v1.28.1
=======

Minor Changes
-------------

- Test more ansible versions (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/162)

v1.28.0
=======

Minor Changes
-------------

- Added missing fields to 'icinga_host' and 'icinga_host_template' (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/158)

Bugfixes
--------

- role: add check_command to icinga_service_apply (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/161)

v1.27.2
=======

v1.27.1
=======

v1.27.0
=======

Minor Changes
-------------

- Add possibility to use Compose and keyed groups in inventory-module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/155)

v1.26.0
=======

Minor Changes
-------------

- add option to append arguments to all modules (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/153)

v1.25.1
=======

v1.25.0
=======

Minor Changes
-------------

- Add Icinga scheduled downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/146)

Bugfixes
--------

- added a fix for the new scheduled_downtime module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/150)

v1.23.1
=======

Minor Changes
-------------

- add resolve option to inventory-plugin (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/147)

v1.23.0
=======

v1.22.1
=======

v1.22.0
=======

Minor Changes
-------------

- Add support for retry_interval and max_check_attempts to host template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/140)

v1.21.2
=======

v1.21.1
=======

Bugfixes
--------

- Changed place in the creation order of service object in ansible_icinga role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/135)

v1.21.0
=======

Minor Changes
-------------

- Add event_command parameter to icinga_service_apply module (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/132)
- Add event_command parameter to service apply playbook to enable usage (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/133)

v1.20.1
=======

v1.20.0
=======

Minor Changes
-------------

- Add some more documentation on command template (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/128)
- add "vars" variable to icinga_notification in the role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/129)

v1.19.0
=======

Minor Changes
-------------

- add notification_template to role (https://github.com/T-Systems-MMS/ansible-collection-icinga-director/pull/125)

v1.18.1
=======
