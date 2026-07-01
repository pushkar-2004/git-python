import os
import hashlib
import zlib

def hash_object(dir_name,file_name,args_len):

    #dir_name = os.getcwd()
    # file_name = sys.argv[-1]
    
    path = f'{dir_name}/{file_name}'
    
    with open(path,'rb') as f:
        content = f.read()
    
    content_size_in_bytes = len(content)
    
    header = "blob "+str(content_size_in_bytes)+"\0"
    header=header.encode()
    
    final_content = header+content
    hash_val = hashlib.sha1(final_content)
    # print('hash value is : \n' + hash_val)
    
    hash_value_hex = hash_val.hexdigest()
    
    # -w flag
    if args_len==4:

        obj_dir_name = hash_value_hex[:2]
        obj_file_name = hash_value_hex[2:]

        obj_path = f'{dir_name}/.git/objects/{obj_dir_name}'

        compressed_content = zlib.compress(final_content)
        os.makedirs(obj_path,exist_ok=True)
        
        with open(f'{obj_path}/{obj_file_name}','wb') as f:
            f.write(compressed_content)

        print("file compressed and written successfully")

    return hash_val