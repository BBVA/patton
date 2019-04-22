#!/usr/bin/env bash

# Create job
echo "[*] Building crontab"
echo "40 */4 * * * /usr/local/bin/update_vulns.sh >> /var/log/cron.log 2>&1" > /etc/crontabs/update-patton
chmod +x /etc/crontabs/update-patton
crontab /etc/crontabs/update-patton

# Run in foreground
touch /var/log/cron.log
echo "[*] Launching cron tasks"
crond && exec gosu 1000:1 tail -f /var/log/cron.log