ansible-dconf-centos
====================

This Ansible role is just an example to reproduce an issue with Ansible dconf module on CentOS 7.

The dconf module requires the dbus-run-session binary.
It comes with dbus >= 1.8 but CentOS 7 comes with dbus 1.6.

The example runs fine on Debian.

License
-------

BSD
