import sys
import os
import zlib
import hashlib

from init import init
from cat_file import cat_file
from hash_object import hash_object
from ls_tree import ls_tree
from write_tree import write_tree

def main():
    #print("Logs from your program will appear here!", file=sys.stderr)

    command = sys.argv[1]
    dir_path = os.getcwd()
    # print(command)
    # print(len(sys.argv))

    if command == "init":
        init()
    elif command == "cat-file":
        cat_file(sys)
    elif command == "hash-object":
        file_name = sys.argv[-1]
        # path = f'{dir_name}/{file_name}'
        hash_val = hash_object(dir_path,file_name,len(sys.argv))
        print(hash_val)
    elif command == "ls-tree":
        ls_tree(sys)
    elif command == "write-tree":

        hash_value,tree_object_content=write_tree(dir_path)

        print(hash_value)

        dir_path = hash_value[:2]
        file_path = hash_value[2:]

        cwd = os.getcwd()
        final_path = f'{cwd}/.git/objects/{dir_path}'

        os.makedirs(final_path,exist_ok=True)
        comprs_tree_content = zlib.compress(tree_object_content)

        with open(f'{final_path}/{file_path}','wb') as f:
            f.write(comprs_tree_content)

        print("tree file write successfull")

    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()
