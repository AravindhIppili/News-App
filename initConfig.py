import os
import json
from ConfigManager import Config
from Utils.DAL.Services.UserService import UserService

base_dir = os.path.dirname(__file__)


def loadConfig(config_dict: dict):
    if "common" in config_dict:
        Config.registerDict(config_dict.get("common"))
    else:
        Config.registerDict(config_dict)


def initConfig(stage: str = "dev"):
    for config_file in [".env", "config"]:
        with open(os.path.join(base_dir, f"{config_file}.json")) as file:
            env = json.load(file)
        loadConfig(env)
        loadConfig(env.get(stage))

    user_service = UserService()
    user_service.initConnection()

    Config.register("user_service", user_service)
