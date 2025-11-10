#!/bin/bash

cd src
for filename in *; do
    if ! grep -xqF "$filename" .ampyignore; then
        echo "Copy $filename"
        ampy put $filename
    fi
done
