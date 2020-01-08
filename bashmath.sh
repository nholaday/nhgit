#!/bin/bash

# You can run any command from a script like this
echo df
df -h
echo wc -l vimdict.py
wc -l vimdict.py
echo ""

# You can also do math
echo "3 + 4"
expr 3 + 4
echo "3 \* 4"
expr 3 \* 4

# Variables
MYVAR=12
echo $MYVAR
expr $MYVAR \* $MYVAR

# For loops
for number in {1..10}
do
    echo "$number"
done

for number in {0..100..10}
do
    echo "$number"
done
#exit 0

# Using | (STDIN and STOUT)

