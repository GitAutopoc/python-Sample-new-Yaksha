import json
class TestResults:
    testCaseResults = ""
    customData = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
