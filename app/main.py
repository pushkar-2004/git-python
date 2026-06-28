import sys
import os
import zlib

def main():
    print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    # print(command)
    # print(len(sys.argv))

    if command == "init":
        
        os.makedirs(".git",exist_ok=True)
        os.makedirs(".git/objects",exist_ok=True)
        os.makedirs(".git/refs",exist_ok=True)
        with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
        print("Initialized git directory")

    elif command == "cat-file":

        file_hash = sys.argv[3]
        dir_name = file_hash[:2]
        file_name = file_hash[2:]
        # print(dir_name)
        # print(file_name)
        path = f'.git/objects/{dir_name}/{file_name}'

        with open(path, 'rb') as f:
            compressed = f.read()

        decompressed = zlib.decompress(compressed)

        header, content = decompressed.split(b'\x00', 1)

        print(content.decode(), end="")

    else:

        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
