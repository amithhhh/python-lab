#!/bin/bash

COMMIT_MSG="Auto commit for all files"

for file in *; do
	git add "$file"
	git commit -m "Add/Updated file: $file"
done

echo "completed"
