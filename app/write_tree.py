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

    for item in os.listdir(folder):
        #exclude .git from tree object
        if item==".git":
            continue

        path = os.path.join(folder,item)

        if os.path.isfile(path):
            mode = '100644'
            name = item
            hash_val = hash_object(folder,item,3)
            content = f'{mode} {name}\0{hash_val}'
            # content = content.encode()
            child_info.append(content)
        else:
            
            mode = "040000"
            name = item
            dir_path = os.path.join(folder,item)
            hash_val,_ = write_tree(dir_path)
            if hash_val == -1:
                continue
            content = f'{mode} {name}\0{hash_val}'
            # content = content.encode()
            child_info.append(content)
        
    print(child_info)
    if len(child_info) == 0:
        return -1
    tree_object_content = ""
    for item in child_info:
        tree_object_content+=item

    size = len(tree_object_content)
    tree_object_content = ("tree "+str(size)+"\0"+tree_object_content).encode()
    hash_value = hashlib.sha1(tree_object_content).hexdigest()
    return hash_value,tree_object_content
    


