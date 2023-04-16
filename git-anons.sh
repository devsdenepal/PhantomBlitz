#!/bin/bash

# Set the path to the directory you want to monitor
DIRECTORY=$1

# Set the name of the remote repository and branch
REMOTE=origin
BRANCH=main

# Start monitoring the directory for changes
inotifywait -m -e modify --format %w%f "$DIRECTORY" | while read FILE; do

    # Get the name of the file that was modified
    FILENAME=$(basename "$FILE")

    # Get the difference in the file
    DIFF=$(git diff "$FILE")

    # Check if there are any changes
    if [ -n "$DIFF" ]; then
        echo 'change detected $DIFF in $FILENAME'
        # Commit the changes
        git add  *
        git commit -m "Updated $FILENAME: $DIFF"

        # Push the changes to the remote repository
        git push "$REMOTE" "$BRANCH"
    fi
done
