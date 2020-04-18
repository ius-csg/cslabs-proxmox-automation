# CSLABS Proxmox Automation


This project contains a few scripts that provide useful commands for proxmox. The main use of this project is
to get a new user session from proxmox and cache it in the nginx config for the reverse proxy.

The get-user-ticket.py is responsible for replacing the ticket in the nginx configuration.


## Setup

Clone repository onto a webserver with nginx and with network access to proxmox. This server must also have python3 installed with the packages 
from the pipfile installed.
Clone it into the `/root/cslabs-proxmox-automation/` directory.
Copy env.example.sh to env.sh and change the credentials to match the proxmox server.

call `./reload_ticket.sh` as root to be sure it works.
Add this line to crontab and the automation should be ready to go.

```
*/30 * * * * /bin/bash /root/cslabs-proxmox-automation/reload_ticket.sh >/dev/null
```

## Requirements
This project is built using python 3 and pipenv to manage dependencies for local development.