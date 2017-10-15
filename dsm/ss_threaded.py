import socket
import json
import configparser

Config = configparser.ConfigParser()
Config.read("config.ini")
port = Config.get("Settings", "Port")