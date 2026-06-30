import zlib

def ls_tree(sys):
    file_hash = sys.argv[2]
    dir_name = file_hash[:2]
    file_name = file_hash[2:]

    path = f'.git/objects/{dir_name}/{file_name}'

    with open(path, 'rb') as f:
        compressed = f.read()

    decompressed = zlib.decompress(compressed)

    print(decompressed)