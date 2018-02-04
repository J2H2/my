#!/bin/bash

check_command="mysqladmin ping -h mariadb --port=3306 -u root -proot"
command="$@"

while true; do
    $check_command &> /dev/null
    if [ $? -eq 0 ]; then
        break
    fi
    echo "Waiting."
    sleep 1
done

exec $command
