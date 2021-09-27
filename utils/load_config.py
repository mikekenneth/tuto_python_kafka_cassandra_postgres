from configparser import ConfigParser


def get_conf(ini_file: str, section: str = None) -> dict:
    """Get section configurations from ini file

    Args:
        ini_file (str): Configuration file that will be parsed
        section (str, optional): Specify the section to be return
    """  
    config = ConfigParser()
    config.read(ini_file)
    if section is not None:
        return dict(config[section])
    result = {}
    for i in config.sections():
        result.update({i: dict(config[i])})
    return result