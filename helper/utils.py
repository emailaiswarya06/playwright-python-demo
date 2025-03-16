import configparser
import logging
import os
from pathlib import Path


def path_from_project_root(file_path: str) -> str:
    _root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return _root_dir + '/' + file_path

def read_config(section, key, default=None):
    config = configparser.ConfigParser()
    config.optionxform = str  # Preserve case for keys

    config_file = Path(__file__).resolve().parent.parent / "config" / "test_config.ini"

    if not os.path.exists(config_file):
        logging.info(f"Config file not found: {config_file}")
        raise FileNotFoundError(f"Config file not found: {config_file}")

    config.read(config_file)

    if section not in config:
        raise KeyError(f"Section '{section}' not found in config file.")

    if key not in config[section]:
        raise KeyError(f"Key '{key}' not found in section [{section}].")

    return config[section][key] if default is None else config.get(section, key, fallback=default)
