import sys
from proxmoxer import ProxmoxAPI

proxmox_host = sys.argv[1]
proxmox_user = sys.argv[2]
proxmox_password = sys.argv[3]

proxmox = ProxmoxAPI(proxmox_host, user=proxmox_user, password=proxmox_password, verify_ssl=False)

for node in proxmox.nodes.get():
    print(node['node'])
    for vm in proxmox.nodes(node['node']).qemu.get():
        print("{0}. {1} => {2}".format(vm['vmid'], vm['name'], vm['status']))





