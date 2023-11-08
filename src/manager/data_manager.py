import os
from tkinter import filedialog
import json

class EventModel():
    def __init__(self, data: dict):
        self.name = data['name']
        self.request_body = data['request_body']

class EnvironmentModel():
    def __init__(self, data: dict):
        self.events: dict = self.createEventModel(data['events'])
        self.server_url = data['server_url']

    def createEventModel(self, data: dict):
        x = {}
        for key, value in data.items():
            x[key] = EventModel(value)

        return x
    
    def getEventByKey(self, key: str) -> EventModel:
        print(key)
        return self.events[key]

class DataManager():
    def __init__(self):
        self.path = 'caches/save_file.json'
        self.data: dict = {};
        self.current_env: str = ""

    def getCurrentData(self) -> EnvironmentModel:
        return self.getDataByName(self.current_env)

    def loadData(self):
        json_file = open(self.path, 'r')
        json_data = json_file.read()
        data: dict = json.loads(json_data)
        for key, value in data.items():
            self.data[key] = EnvironmentModel(value)

    def getDataByName(self, name_env) -> EnvironmentModel:
        if self.data[name_env] is not None:
            return self.data[name_env]
        return {}
    
    def getEnvList(self) -> list:
        x = []
        for i in self.data:
            x.append(i)
        return x
    






        