import os
import shutil
import argparse


def parse_arguments():
    # Create an argument parser to handle command-line arguments
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension."
    )
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument(
        "destination_dir",
        nargs="?",
        default="dist",
        help="Path to the destination directory. Defaults to 'dist'.",
    )
    return parser.parse_args()


def copy_and_sort_files(source_dir, destination_dir):
    # Create the destination directory if it does not exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    # Iterate over all items in the source directory
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        if os.path.isdir(source_item):
            # Recursively process the directory
            copy_and_sort_files(source_item, destination_dir)
        elif os.path.isfile(source_item):
            try:
                # Process the file
                file_extension = os.path.splitext(item)[1].lstrip(".").lower()
                if not file_extension:
                    file_extension = "no_extension"
                destination_path = os.path.join(destination_dir, file_extension)

                # Create the subdirectory for the file extension if it does not exist
                if not os.path.exists(destination_path):
                    os.makedirs(destination_path)

                # Copy the file to the appropriate subdirectory
                shutil.copy2(source_item, destination_path)
            except Exception as e:
                print(f"Failed to copy {source_item}: {e}")


def main():
    # Parse the command-line arguments
    args = parse_arguments()
    source_dir = args.source_dir
    destination_dir = args.destination_dir

    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Start the file copying and sorting process
    copy_and_sort_files(source_dir, destination_dir)
    print(f"Files have been copied and sorted into '{destination_dir}'")


if __name__ == "__main__":
    main()