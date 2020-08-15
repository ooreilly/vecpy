#!/bin/bash
root=../vecpy
for func in elementwise sum
do
        mydocstring ${root}/api/$func.py $func -m -T=template.md > docs/$func.md
done
