import json
from Types import DataType
from DataReader import DataReader

class JSONDataReader(DataReader):
    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)