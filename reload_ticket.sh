#!/bin/bash

python3 /root/cslabs-proxmox-automation/get-user-ticket.py ***REMOVED*** ***REMOVED*** ***REMOVED*** a1 100 /etc/nginx/nginx.conf
echo "Configuration Updated"
/usr/sbin/nginx -t
systemctl reload nginx
echo "Configuration Reloaded"
