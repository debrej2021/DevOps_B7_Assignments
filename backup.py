import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Check if the destination directory exists, create it if it doesn't
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
            print(f"Created destination directory '{destination_dir}'.")
        except Exception as e:
            print(f"Error: Could not create destination directory '{destination_dir}'. {e}")
            return

    # Iterate over all files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        if os.path.isfile(source_file):
            destination_file = os.path.join(destination_dir, filename)

            # Check if the file already exists in the destination directory
            if os.path.exists(destination_file):
                # Append a timestamp to the filename
                base, ext = os.path.splitext(filename)
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                destination_file = os.path.join(destination_dir, f"{base}_{timestamp}{ext}")

            # Copy the file to the destination directory
            try:
                shutil.copy2(source_file, destination_file)
                print(f"Copied '{source_file}' to '{destination_file}'.")
            except Exception as e:
                print(f"Error: Could not copy '{source_file}' to '{destination_file}'. {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)
