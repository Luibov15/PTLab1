import pytest
from JSONDataReader import JSONDataReader
from Types import DataType

class TestJSONDataReader:
    @pytest.fixture()
    def json_content(self) -> tuple[str, DataType]:
        data = {
            "Иванов Иван Иванович": [("математика", 80), ("программирование", 90), ("литература", 76)],
            "Петров Петр Петрович": [("математика", 100), ("социология", 90), ("химия", 61)]
        }
        json_data = '''{
            "Иванов Иван Иванович": {
                "математика": 80,
                "программирование": 90,
                "литература": 76
            },
            "Петров Петр Петрович": {
                "математика": 100,
                "социология": 90,
                "химия": 61
            }
        }'''
        return json_data, data

    def test_read(self, tmpdir, json_content):
        p = tmpdir.join("data.json")
        p.write(json_content[0])
        reader = JSONDataReader()
        assert reader.read(str(p)) == json_content[1]