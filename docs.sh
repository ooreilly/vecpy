#!/bin/bash

root=vecpy_tmp/vecpy/api
for file in ${root}/*.py
do
        file_name=$(basename $file)
        function_name=${file_name%.py}

        if [[ ${function_name} == "__init__" ]]
        then
                continue
        fi

        echo "Generating docs for ${function_name}"
        mydocstring $file $function_name -m -T=template.md > docs/api/$function_name.md
done
