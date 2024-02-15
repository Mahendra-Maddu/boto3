def update_file(file_path,key,value):
    with open(file_path,'r') as file:
        lines = file.readlines()
    with open(file_path,'w') as file :
        for line in lines:
            if key in line:
                print(key)
                file.write(key +'=' + value+ '\n')
            else:
                file.write(line)
server_config_file = 'server.config'
key_to_update = 'MAX_CONNECTIONS'
value_to_replace = '400'
update_file(server_config_file,key_to_update,value_to_replace)
