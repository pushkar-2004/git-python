import zlib

def cat_file(sys):
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

    print('decompress and print file content : \n')
    print(content.decode(), end="")