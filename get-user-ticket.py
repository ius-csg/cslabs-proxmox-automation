import sys
import re
import urllib.parse
from proxmoxer import ProxmoxAPI

proxmox_host = sys.argv[1]
proxmox_user = sys.argv[2]
proxmox_password = sys.argv[3]
proxmox_node = sys.argv[4]
configuration_path = sys.argv[5]

proxmox = ProxmoxAPI(proxmox_host, user=proxmox_user, password=proxmox_password, verify_ssl=False)


resp = proxmox.access.ticket.post(username=proxmox_user, password=proxmox_password)

ticket = resp['ticket']
url_encoded_ticket = urllib.parse.quote(ticket)

with open(configuration_path, 'r') as f:
    content = f.read()

content_new = re.sub('(proxy_set_header Cookie "PVEAuthCookie=)(.*?)(";)', r'\1[TICKET]\3', content, flags=re.M)
content_new = content_new.replace('[TICKET]', ticket)
f = open(configuration_path, "w")
f.write(content_new)
f.close()
