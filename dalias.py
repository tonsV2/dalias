import requests
from parse import parse
import json, pprint


def pp(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def merge_two_dicts(x, y):
    z = x.copy()  # start with x's keys and values
    z.update(y)  # modifies z with y's keys and values & returns None
    return z


def read_aliases():
    aliasFile = "/home/tons/.config/dalias/alias.list"
    with open(aliasFile) as f:
        content = f.readlines()
    parsed = [parse("alias {}='{}'", alias) for alias in content]
    return {alias[0]: alias[1] for alias in parsed}


def write_aliases(aliases):
    formatted = ["alias %s='%s'" % (alias, line) for (alias, line) in aliases.items()]
    with open("/home/tons/.config/dalias/alias.list", "w") as f:
        f.write("\n".join(formatted))


def read_remote_aliases():
    #r = requests.post('http://localhost:8081/api/findByAllTags', json=["alias"])
    r = requests.post('https://glacial-spire-56714.herokuapp.com/api/findByAllTags', json=["alias"])
    remoteAliases = {alias["name"]: alias["line"] for alias in r.json()}
    return remoteAliases


aliases = read_aliases()
remoteAliases = read_remote_aliases()
allAliases = merge_two_dicts(aliases, remoteAliases)
# for (alias, line) in allAliases.items():
#    print("%s: %s" % (alias, line))
#write_aliases(allAliases)
pp(allAliases)
