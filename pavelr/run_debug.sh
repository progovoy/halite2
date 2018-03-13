#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

${DIR}/halite -r -t -d "240 160" "python3 ${DIR}/botproxy.py 1337" "python3 ${DIR}/MyBot.py NODEBUG"
