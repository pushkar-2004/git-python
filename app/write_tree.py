import os
from hash_object import hash_object
import zlib
import hashlib

def write_tree(folder):
    ''''
    1. Iterate on directory
    2. If item is file then find its hash name mode and append it to the content of tree object
    3. If it is folder the make a call to the same function again
    '''
    child_info = []

    for item in sorted(os.listdir(folder)):
        #exclude .git from tree object
        if item==".git":
            continue

        path = os.path.join(folder,item)

        if os.path.isfile(path):
            mode = b'100644 '
            name = (item+'\0').encode()
            hash_val = hash_object(folder,item,3).digest()
            content = mode+name+hash_val
            # content = content.encode()
            child_info.append(content)
        else:
            
            mode = b"40000 "
            name = (item+'\0').encode()
            dir_path = os.path.join(folder,item)
            hash_val,_ = write_tree(dir_path)

            if hash_val == -1:
                continue

            hash_val=hash_val.digest()
            content = mode+name+hash_val
            # content = content.encode()
            child_info.append(content)
        
    print(child_info)
    if len(child_info) == 0:
        return -1,-1
    tree_object_content = b""
    for item in child_info:
        tree_object_content+=item

    size = str(len(tree_object_content)).encode()
    # tree_object_content = ("tree "+str(size)+"\0"+tree_object_content).encode()
    tree_object_content = b"tree "+size+b"\0"+tree_object_content
    hash_value = hashlib.sha1(tree_object_content)
    return hash_value,tree_object_content
    


