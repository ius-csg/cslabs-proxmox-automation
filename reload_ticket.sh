#!/bin/bash
source /root/cslabs-proxmox-automation/env.sh
python3 /root/cslabs-proxmox-automation/get-user-ticket.py $PROXMOX_HOST $PROXMOX_USER $PROXMOX_PASSWORD $PROXMOX_NODE $NGINX_CONF
echo "Configuration Updated"
/usr/sbin/nginx -t
systemctl reload nginx
echo "Configuration Reloaded"
