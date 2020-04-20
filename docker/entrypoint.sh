#!/bin/bash
# required directory for enigma2
sudo mkdir -p /dev/input

# start web server
sudo service apache2 start

echo "start Xvfb"
test -z "$RESOLUTION" && RESOLUTION="1280x720x16"
Xvfb "$DISPLAY" -ac -screen 0 "$RESOLUTION" &
xvfb_pid=$!
echo "exec command $@"
exec "$@"
echo "terminate"
kill ${xvfb_pid}
