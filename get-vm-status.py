import sys
import json
from proxmoxer import ProxmoxAPI

proxmox_host = sys.argv[1]
proxmox_user = sys.argv[2]
proxmox_password = sys.argv[3]
proxmox_node = sys.argv[4]
vm_id = sys.argv[5]

proxmox = ProxmoxAPI(proxmox_host, user=proxmox_user, password=proxmox_password, verify_ssl=False)


resp = proxmox.nodes(proxmox_node).qemu().get('%s/status/current' % vm_id)

print(json.dumps(resp))



