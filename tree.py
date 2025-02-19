import os


def print_directory_tree(startpath, indent=""):
    files = []
    directories = []

    try:
        # Sort directories first, then files
        for entry in sorted(os.listdir(startpath)):
            full_path = os.path.join(startpath, entry)
            if os.path.isdir(full_path):
                directories.append(entry)
            else:
                files.append(entry)

        # Print directories first
        for directory in directories:
            print(indent + "📁 " + directory)
            print_directory_tree(os.path.join(startpath, directory), indent + "    ")

        # Print files
        for file in files:
            print(indent + "📄 " + file)

    except PermissionError:
        print(indent + "❌ [Permission Denied]")


# Run from the current working directory
if __name__ == "__main__":
    print("📂 Project Directory Structure:\n")
    print_directory_tree(os.getcwd())  # Gets the current directory
