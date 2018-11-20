import os
import argparse
import functools

from resource_manager import read_config

#MODULES_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#SHORTCUTS = {
#    'dpipe_configs': os.path.join(MODULES_FOLDER, os.pardir, 'dpipe_configs'),
#}

# get_resource_manager = functools.partial(read_config, shortcuts=SHORTCUTS)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('--config_path', required=True)
    args = parser.parse_known_args()[0]
    read_config(args.config_path).get_resource(args.command)
    
