name = input("name : ")
job = int(input("job : "))

msg = '''------info of %s------
name:%s
job:%d
'''%(name,name,job)
print(msg)
msg1 = '''------info2e of {_name}------
name:{_name}
job:{_job}
'''.format(
    _name = name,
    _job = job
)
print(msg1)