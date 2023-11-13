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
        self.raw_data: dict = {} # use for caching only

    def getCurrentData(self) -> EnvironmentModel:
        return self.getDataByName(self.current_env)

    def loadData(self):
        try:
            json_file = open(self.path, 'r')
            json_data = json_file.read()
            data: dict = json.loads(json_data)
            self.raw_data = data
            self.data = {}
            for key, value in data.items():
                self.data[key] = EnvironmentModel(value)
        except:
            os.mkdir('caches')

    def getDataByName(self, name_env) -> EnvironmentModel:
        if name_env in self.data:
            return self.data[name_env]
        return EnvironmentModel({"events": {}, "server_url": ""})
    
    def getEnvList(self) -> list:
        x = []
        for i in self.data:
            x.append(i)
        return x
    
    def saveData(self, event_obj, serve_url, environment_name):
        self.raw_data[environment_name] = {
            "events": event_obj,
            "server_url": serve_url
        }
        json_object = json.dumps(self.raw_data, indent=4)
 
        # Writing to sample.json
        with open(self.path, "w") as outfile:
            outfile.write(json_object) 

        # refresh data again
        self.loadData()
    






        