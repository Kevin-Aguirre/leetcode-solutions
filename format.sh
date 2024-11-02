#!/bin/bash

# Get the input as a single argument
title="$1"

# Extract the problem number and remove any trailing period
problem_number=$(echo "$title" | awk '{print $1}' | tr -d '.')

# Extract and format the title by converting to lowercase and replacing spaces with hyphens
formatted_title=$(echo "$title" | cut -d' ' -f2- | tr '[:upper:]' '[:lower:]' | tr ' ' '-')

# Combine to form the filename
filename="${problem_number}-${formatted_title}.py"

# Output the result
echo "$filename"
