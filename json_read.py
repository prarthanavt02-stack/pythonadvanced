#read

import json
f=open("data.json","r")

content=json.load(f)

#content=f.read()

print(content)
print(content[0],'name')
f.close()