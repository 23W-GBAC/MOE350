#!/bin/bash

# Input directory containing your BMW images
input_dir="Images/BMW_images"

# Output directory for resized images
output_dir="resized_images"

# Desired size for the images
desired_size="600x600"  # Change this to your preferred size (e.g., 600x600)

# Check if the output directory exists; if not, create it
if [ ! -d "$output_dir" ]; then
    echo "Creating output directory: $output_dir"
    mkdir -p "$output_dir"
else
    echo "Output directory '$output_dir' already exists."
fi

# Loop through each image in the input directory and resize
for file in "$input_dir"/*.{jpg,jpeg,png,gif,JPG,JPEG}; do
    filename=$(basename "$file")
    convert "$file" -resize "$desired_size>" "$output_dir/$filename"
    echo "Resized $filename"
done
