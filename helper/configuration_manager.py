import logging

from jproperties import Properties

from helper.utils import path_from_project_root, read_config


class ConfigurationManager:
    __configs = Properties()
    with open(path_from_project_root('resources/config.properties'), 'rb') as __config_file:
        __configs.load(__config_file)

    @staticmethod
    def __fetch(property_key: str) -> str:
        return ConfigurationManager.__configs.get(property_key)[0]

    @staticmethod
    def browser() -> str:
        logging.info(ConfigurationManager.__fetch('browser'))
        return ConfigurationManager.__fetch('browser')

    @staticmethod
    def headless() -> bool:
        logging.info(ConfigurationManager.__fetch('headless'))
        return ConfigurationManager.__fetch('headless') == 'True'

    @staticmethod
    def browser_channel() -> str:
        logging.info(ConfigurationManager.__fetch('browser.channel'))
        return ConfigurationManager.__fetch('browser.channel')

    @staticmethod
    def slow_motion() -> int:
        return int(ConfigurationManager.__fetch('slow.motion'))

    @staticmethod
    def base_url() -> str:
        return ConfigurationManager.__fetch('base.url')

class ConfigurationManager1:

    @staticmethod
    def headless() -> bool:
        return read_config('BROWSER', 'headless') == 'True'

    @staticmethod
    def browser_channel() -> str:
        return read_config('BROWSER', 'channel')

    @staticmethod
    def slow_motion() -> int:
        return int(read_config('BROWSER', 'slowmotion'))

