import zlib

def ls_tree(sys):
    file_hash = sys.argv[2]
    dir_name = file_hash[:2]
    file_name = file_hash[2:]

    path = f'.git/objects/{dir_name}/{file_name}'

    with open(path, 'rb') as f:
        compressed = f.read()

    decompressed = zlib.decompress(compressed)

    # print(decompressed)

    header , body  = decompressed.split(b'\x00',1)
    # print(header)
    # print(body)

    length = int((header.split(b' ')[1]).decode())
    # print(length)
    # print(type(length))
    
    i=0
    token=b''
    while(i<length):

        val = body[i:i+1]

        if val==b' ':
            #before -> mode
            str_token=token.decode()
            token=b''
            if str_token=='40000':
                print('040000 tree ',end='')
            else:
                print('100644 blob ',end='')

        elif val==b'\x00':
            #before -> name
            str_token = token.decode()
            token=b''
            print(str_token,end=" ")
            hsh_len=20
            while(hsh_len):
                i+=1
                token+=body[i:i+1]
                # i+=1
                hsh_len-=1
            str_token=token.hex()
            token=b''
            print(str_token)

        else:
            token+=val
        i+=1

    # print("tree object read complete")

