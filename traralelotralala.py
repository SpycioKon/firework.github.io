import hashlib

def file_hash(filepath, chunk_size=8192):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()
import os

def find_duplicates(folder):
    hashes = {}
    duplicates = []

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            try:
                filehash = file_hash(path)
                if filehash in hashes:
                    duplicates.append((path, hashes[filehash]))
                else:
                    hashes[filehash] = path
            except Exception as e:
                print(f"Skipped {path}: {e}")

    return duplicates
if __name__ == "__main__":
    folder_to_scan = os.path.expanduser("~/Documents")
    dupes = find_duplicates(folder_to_scan)

    if dupes:
        print("Found duplicates:")
        for dup, original in dupes:
            print(f"{dup} == {original}")
    else:
        print("No duplicates found!")

