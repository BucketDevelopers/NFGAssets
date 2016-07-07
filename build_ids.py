import json

def generate_ids(fname, idKey):
    config_file = open(fname, 'r')
    config_file_raw = config_file.read()
    config_file.close()
    config_file_json = json.loads(config_file_raw)
    files = config_file_json['files']
    i = 0
    for ef in files:
        ef.update({'id': idKey + str(i)})
        i = i + 1
    new_config_file_json = json.dumps(config_file_json, indent=2)
    new_config_file = open((fname), 'w')
    new_config_file.write(new_config_file_json)
    new_config_file.close()

index_file = open('index.json', 'r')
index_json_raw = index_file.read()
index_file.close()
index_json = json.loads(index_json_raw)
base_path = index_json['basePath']
configs = index_json['configs']

for config in configs:
    generate_ids((base_path + config['file']), config['name'])
