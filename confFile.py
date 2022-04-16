import os
import os.path
import sys
import json
import logging

class ConfFile:
    args = []
    config = None
    config_dir = ''
    config_file = ''

    config_dirname = ''
    config_fname = ''


    def load_paths(self):
        ''' Configure path variables for this app
        '''
        __platform__ = sys.platform
        if __platform__ == 'win32':
            HOME = os.environ.get('HOMEPATH')
            self.config_dir = os.path.join(HOME, r'AppData\Roaming', self.config_dirname)
            self.config_file = os.path.join(self.config_dir, self.config_fname)

        elif __platform__ == 'linux':
            HOME = os.environ.get('HOME')
            self.config_dir = os.path.join(HOME, '.config', self.config_dirname)
            self.config_file = os.path.join(self.config_dir, self.config_fname)

        else:
            print(f'Platform {__platform__} not supported')


    def load_config(self):
        ''' Load from Config file onto global object: config
        '''
        self.load_paths()

        # try to load config
        try:
            with open(self.config_file, mode='r') as file:
                self.config = json.load(file)
        except FileNotFoundError:
            self.config = {}
            self.create_config()
            print('config file did not exist')

    def save_config(self):
        ''' Write data present on global object: config, back to config file
        '''
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir, exist_ok=True)

        with open(self.config_file, mode='w') as file:
            json.dump(self.config, file, indent=2)

    def config_exists(self):
        ''' Write data present on global object: config, back to config file
        '''
        if not os.path.exists(self.config_dir):
            return False

        if not os.path.exists(self.config_file):
            return False

        return True


    def create_config(self):
        ''' Create Brand-new config. this is destructive.
        '''
        # self.config['current_game_ver'] = '1.17.1'
        # self.config['dest_dir'] = 'your_install_destination'
        # self.config['mods'] = {}
        # self.config['mods']['P7dR8mSH'] = {}
        self.save_config()

    def read(self, key):
        assert type(self.config) is dict
        return self.config[key]

    def try_read(self, key):
        assert type(self.config) is dict
        try:
            return self.config[key]
        except BaseException as e:
            print(e.__class__.__name__)
            print(e.__traceback__)
            return None

    def pend_write(self, key, value):
        assert type(self.config) is dict
        self.config[key] = value


    def __init__(self, dirname, fname):
        ''' Check existance of config file
        should also check format to some extent
        '''

        self.config_dirname = dirname
        self.config_fname = fname
        self.load_config()
        self.save_config()
