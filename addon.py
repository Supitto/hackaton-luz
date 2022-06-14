# This is an auto generated file, don't edit it manually

import json

class ExtractFundsAnbima:

    def __init__(self):
        self.state = []

    def response(self, flow):
        if flow.request.host != "data.anbima.com.br": return
        if flow.request.method != b"GET": return
        if flow.request.path != "/fundos-bff/fundos": return
        decoded_body = json.load(flow.response.content)
        decoded_body = decoded_body["content"]
        self.state += decoded_body

    def request(self, flow):
        if flow.request.path == "/commit":
            with open("/out/output.json","wb") as f:
                json.dump(self.state)

