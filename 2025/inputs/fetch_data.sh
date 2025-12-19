#!/bin/bash

if [[ $# -ne 2 ]] ; then
    echo "usage: bash fetch_data.sh <day> <session cookie value>"
    exit 1
fi

DAY=$1
SESSION=$2

curl https://adventofcode.com/2025/day/${DAY}/input \
    -H "cookie: session=${SESSION}" \
    -o day${DAY}.txt

printf "\n> head day${DAY}.txt\n"
head day${DAY}.txt
