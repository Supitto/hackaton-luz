#!/usr/bin/python3
import json

def generate_imports(imports):
    return '\n'.join('import '+i for i in imports)


def generate_filter(filter_spec):
    content = ""
    content += f"class {filter_spec['id']}:\n"
    content += "\n"
    content += "    def __init__(self):\n"
    content += "        self.state = []\n"
    content += "\n"

    content += "    def response(self, flow):\n"
    if "host" in filter_spec["match_when"]:
        content += f"        if flow.request.host != \"{filter_spec['match_when']['host']}\": return\n"
    if "method" in filter_spec["match_when"]:
        content += f"        if flow.request.method != b\"{filter_spec['match_when']['method']}\": return\n"
    if "path" in filter_spec["match_when"]:
        content += f"        if flow.request.path != \"{filter_spec['match_when']['path']}\": return\n"
    
    if filter_spec["parse_like"]["payload_type"] == "json":
        content += "        decoded_body = json.load(flow.response.content)\n"
        for f in filter_spec["parse_like"]["filter"].split('.')[1:]: #jq like filter, still needs to implement the rest of it
            content += f"        decoded_body = decoded_body[\"{f}\"]\n"
    else:
        content += "        decoded_body = \"\" #not implemented\n"
    
    if filter_spec["parse_like"]["behaviour"] == "aggregate":
        content += "        self.state += decoded_body\n"
    else:
        content += "        #process mechanism not implemented\n"

    content += "\n"

    content += "    def request(self, flow):\n"
    content += f"        if flow.request.path == \"{filter_spec['process_with']['path']}\":\n"
    if filter_spec['process_with']['behaviour'] == "dump":
        content += f"            with open(\"{filter_spec['process_with']['outfile']}\",\"wb\") as f:\n"
        if filter_spec['process_with']['format'] == "json":
            content += f"                json.dump(self.state)\n"
        else:
            content += "                pass # data format not implemented\n"
    else:
        content += "            # process mechanism not implemented"

    
    return content


def main():
    import_contents = generate_imports(['json'])

    with open('specification.json', 'rb') as f:
        all_specs = json.load(f)

    filter_contents = '\n\n'.join(
        [generate_filter(spec) for spec in all_specs])

    full_content = "# This is an auto generated file, don't edit it manually\n"
    full_content += '\n'
    full_content += import_contents
    full_content += '\n'
    full_content += '\n'
    full_content += filter_contents
    full_content += '\n'

    with open('addon.py','w')  as f:
        f.write(full_content)


if __name__ == "__main__":
    main()
