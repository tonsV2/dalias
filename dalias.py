import requests

r = requests.post('http://localhost:8081/api/findByAllTags', json=["alias"])

for line in r.json():
  print "alias %s='%s'" % (line["name"], line["line"])
