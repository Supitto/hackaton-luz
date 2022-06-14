import generate_addon


def string_test(expectation, reallity):
    if expectation == reallity:
        return True
    return False


def test1():
    expectation = "import json"
    reallity = generate_addon.generate_imports(['json'])
    return string_test(expectation, reallity)


def test2():
    expectation = ""
    reallity = generate_addon.generate_imports([''])
    return string_test(expectation, reallity)


def test3():
    expectation = "import json\nimport struct"
    reallity = generate_addon.generate_imports(['json', 'struct'])
    return string_test(expectation, reallity)


def test4():
    expectation = "class ExtractFundsAnbima:\n\n    def __init__(self):\n        self.state = []\n\n    def response(self, flow):\n        if flow.request.host != \"localhost\": return\n        if flow.request.method != b\"GET\": return\n        if flow.request.path != \"/yay\": return\n        decoded_body = json.load(flow.response.content)\n        decoded_body = decoded_body[\"content\"]\n        self.state += decoded_body\n\n    def request(self, flow):\n        if flow.request.path == \"/commit\":\n            with open(\"/out/output.json\",\"wb\") as f:\n                json.dump(self.state)\n"
    reallity = generate_addon.generate_filter({"id": "ExtractFundsAnbima", "match_when": {"host": "localhost", "method": "GET", "path": "/yay", "headers": {"contains": ["a"]}
                                                                                          },
                                               "parse_like": {
        "payload_type": "json",
        "behaviour": "aggregate",
        "filter": ".content"
    },
        "process_with": {
        "path": "/commit",
        "behaviour": "dump",
        "format": "json",
        "outfile": "/out/output.json"
    }
    })
    return string_test(expectation, reallity)


def test_all():
    print("Test 1 successfull?", test1())
    print("Test 2 successfull?", test1())
    print("Test 3 successfull?", test1())
    print("Test 4 successfull?", test4())

if __name__ == "__main__":
    test_all()
