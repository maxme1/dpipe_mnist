import os
import argparse
import functools

from resource_manager import read_config


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('--config_path', required=True)
    args = parser.parse_known_args()[0]
    read_config(args.config_path).get_resource(args.command)
    
