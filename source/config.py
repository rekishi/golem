import json
import pprint
class Config:
    def __init__(self):
        self.load_from_file('/home/sean/golem/config/config.json')
    def get_commands(self):
        return self.commands 
    def get_token(self):
        return self.token
    def load_from_file(self,filename):
        json_data = open(filename).read()
        data = json.loads(json_data)
        if 'token' in data.keys():
            self.token = data.get('token')
        else:
            raise ValueError('No token specified in configuration')
        if 'commands' in data.keys():
            self.commands = data.get('commands')
        else:
            self.all_commands = True
        if 'prefix' in data.keys():
            self.prefix = data.get('prefix')
        else:
            self.prefix = '!'
        if 'google api key' in data.keys():
            self.g_token = data.get('google api key')
        else:
            self.g_token = ""
    def get_prefix(self):
        return self.prefix
    def add_command(self,command):
        self.commands.append(command)
    def get_gkey(self):
        return self.g_token
    def check_command(self,command):
        if self.all_commands or command in self.commands:
            return True
        else:
            return False

