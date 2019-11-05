import sys
from proxmoxer import ProxmoxAPI

proxmox_host = sys.argv[1]
proxmox_user = sys.argv[2]
proxmox_password = sys.argv[3]
vm_id = sys.argv[4]

proxmox = ProxmoxAPI(proxmox_host, user=proxmox_user, password=proxmox_password, verify_ssl=False)

proxmox.nodes('pve').qemu().post('%s/status/shutdown' % vm_id)

print("success")



