import json


class DBConnection:

    def __init__(self, databasePath: str) -> None:
        self.__databasePath = databasePath
        self.__cache = {}
        try:
            self.__loadCache()
        except FileNotFoundError:
            self.__saveCache()

    def __saveCache(self) -> None:
        with open(self.__databasePath, 'w') as db:
            json.dump(self.__cache, db)

    def __loadCache(self) -> dict:
        with open(self.__databasePath, 'r') as db:
            self.__cache = json.load(db)

    def add(self, key: str, obj: str) -> None:
        self.__cache[key] = obj
        self.__saveCache()

    def get(self, key) -> dict:
        try:
            return self.__cache[key]
        except KeyError:
            return None

    def get_all(self):
        return self.__cache