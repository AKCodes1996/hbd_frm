



import configparser


config = configparser.ConfigParser()
config.read("hybrid_framework\\config\\config.ini")


def config_read(sec,key):
  return config.get(sec,key)


