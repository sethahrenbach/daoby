import logging
import os
from shutil import copy2
from os.path import isfile

from yaml import safe_load as load, dump

logging.root.setLevel(logging.INFO)

if not isfile('./config.yml'):
    copy2('assets/default_configs.yml', 'config.yml')

with open('config.yml') as f:
    configs = load(f.read())

CONFIGS = configs
BOT_PREFIX = os.environ.get('BOT_PREFIX', CONFIGS.get('prefix', '-'))


def load_configs():
    with open('config.yml') as f:
        configs = load(f.read())

    for key, value in configs:
        CONFIGS[key] = value


def save_configs():
    with open('config.yml', 'w') as f:
        f.write(dump(CONFIGS))


def set_config(**kwargs):
    for key, value in kwargs.items():
        CONFIGS[key] = value

    save_configs()
