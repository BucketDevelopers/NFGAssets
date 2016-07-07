import json
import hashlib

def calc_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

index_file = open('index.json', 'r')
index_json_raw = index_file.read()
index_file.close()

index_json = json.loads(index_json_raw)
base_path = index_json['basePath']
configs = index_json['configs']

for config in configs:
    md5 = calc_md5(base_path + config['file'])
    config.update({'md5': md5})
    print("updating md5 for ", config['file'], md5)
x = json.dumps(index_json, indent=2)
index_file = open('index.json', 'w')
index_file.write(x)
index_file.close()
