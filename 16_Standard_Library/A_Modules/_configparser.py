"""
configparser
"""

import configparser
import os
from pathlib import Path

def save_config_file(filepath, configobject):
    with open(filepath, "w") as file:
        configobject.write(file)

def create_config_file(filepath):
    conf = configparser.ConfigParser()
    conf.add_section("Settings")
    conf.set("Settings", "font", "Consolas")
    conf.set("Settings", "font_size", "12")
    conf.set("Settings", "font_style", "Normal")
    conf.set("Settings", "font_info", \
        "%(font)s %(font_size)s pt %(font_style)s")
    save_config_file(filepath, conf)

def get_config_file(filepath):
    conf = configparser.ConfigParser()
    conf.read(filepath)
    return conf

def get_setting(filepath, section, setting):
    return get_config_file(filepath).get(section, setting)

def set_setting(filepath, section, setting, value):
    conf = get_config_file(filePath)
    conf.set(section, setting, value)
    save_config_file(filepath, conf)

def remove_setting(filepath, section, setting):
    conf = get_config_file(filepath)
    conf.remove_option(section, setting)
    save_config_file(filepath, conf)

if __name__ == "__main__":

    filePath = str(Path(os.path.dirname(__file__)).parent.parent.joinpath('Temp', 'settings.ini'))

    create_config_file(filePath)

    set_setting(filePath, "Settings", "font", "Helvetica")
    print(get_setting(filePath, "Settings", "font_info"))

    set_setting(filePath, "Settings", "XXXXX", "XXXXX")
    print(get_setting(filePath, "Settings", "XXXXX"))

    remove_setting(filePath, "Settings", "XXXXX")
    