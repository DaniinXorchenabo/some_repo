from os.path import dirname, abspath, join, exists
import sys
from configparser import ConfigParser




base_path = dirname(abspath(__file__))
# dirname(dirname(__file__))
file_name = "settings.ini"
config_path = join(base_path, file_name)
if exists(config_path):
    cfg = ConfigParser(allow_no_value=True, converters={'list': lambda x: [i.strip() for i in x.split(',')]})
    cfg.read(config_path)
else:
    print("Config not found! Exiting!")
    print(f"You can try cloning {base_path}/example_{file_name} to {config_path} and edit params into this")
    sys.exit(1)

def save_change_in_cinfig_file():
    with open(config_path, "w") as config_file:
        cfg.write(config_file)