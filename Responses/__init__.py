import os
import json


class Responses:
    _response_folder = os.path.join(os.path.dirname(__file__), "")

    @classmethod
    def _loadResponse(cls, lang: str) -> None:
        with open(os.path.join(cls._response_folder, f"{lang}.json"), "r") as file:
            cls._responses = json.load(file)

    @classmethod
    def getResponse(cls, key: str, lang: str = "en") -> str:
        cls._loadResponse(lang)
        return cls._responses[key]
