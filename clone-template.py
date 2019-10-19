import sys
from proxmoxer import ProxmoxAPI

proxmox_host = sys.argv[1]
proxmox_user = sys.argv[2]
proxmox_password = sys.argv[3]
template_vm_id = sys.argv[4]

proxmox = ProxmoxAPI(proxmox_host, user=proxmox_user, password=proxmox_password, verify_ssl=False)

vm_ids = []

for node in proxmox.nodes.get():
    print(node['node'])
    for vm in proxmox.nodes(node['node']).qemu.get():
        vm_ids.append(vm['vmid'])

max_id = int(max(vm_ids))
new_id = max_id + 1
proxmox.nodes('pve').qemu().post(template_vm_id + '/clone', newid=new_id)



