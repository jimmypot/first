
import json


def sayhi():
    print('hello world')
f = open('test.test','r')
data = json.loads(f.read())

print(data['age'])



