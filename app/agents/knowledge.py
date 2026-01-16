import json

class KnowledgeAgent:
    def __init__(self, path="app/data/cars.json"):
        with open(path) as f:
            self.data = json.load(f)

    def get_models(self, car_type):
        return self.data.get(car_type, [])
