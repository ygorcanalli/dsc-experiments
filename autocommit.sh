#!/bin/bash

# Directory to monitor
MONITOR_DIR="raw_results"

# Function to add and commit files to Git
commit_changes() {
    cd "$MONITOR_DIR"
    git add .
    git commit -m "Auto-commit raw_results $(date)"
    git push
    cd -
}

# Monitor directory for changes and commit
inotifywait -m -e create -e modify -r "$MONITOR_DIR" --format '%w%f' | while read file
do
    echo "Detected change in $file"
    commit_changes
done
