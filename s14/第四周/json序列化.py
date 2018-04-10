
import json

info = {
    'name' : 'alex',
    'age'  : 22
}
f = open('test.test','w')
f.write(json.dumps(info))
f.close()
