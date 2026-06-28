import sys
import os
import zlib
import hashlib

def main():
    #print("Logs from your program will appear here!", file=sys.stderr)

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

    elif command == "hash-object":

        dir_name = os.getcwd()
        file_name = sys.argv[-1]
        # print(dir_name)
        # print(file_name)
        path = f'{dir_name}/{file_name}'
        # print(path)
        with open(path,'r') as f:
            content = f.read()
        # print(content)
        content_size_in_bytes = len(content.encode())
        #content to be stored in .git/object
        content = "blob "+str(content_size_in_bytes)+"\0"+content
        # print(content)
        bytes_content = content.encode()
        hash_val = hashlib.sha1(bytes_content).hexdigest()
        print('hash value is : \n' + hash_val)
        # print(type(hash_val))

        if len(sys.argv)==4:
            #we also need to save the file in .git/object
            obj_dir_name = hash_val[:2]
            obj_file_name = hash_val[2:]
            obj_path = f'{dir_name}/.git/objects/{obj_dir_name}'
            compressed_content = zlib.compress(bytes_content)
            os.makedirs(obj_path,exist_ok=True)
            with open(f'{obj_path}/{obj_file_name}','wb') as f:
                f.write(compressed_content)

            print("file compressed and written successfully")
        
    else:

        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
