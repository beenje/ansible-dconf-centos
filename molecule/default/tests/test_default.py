import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cursor_size(host):
    cmd = host.run('dconf read /org/gnome/desktop/interface/cursor-size')
    assert cmd.stdout == "48"
