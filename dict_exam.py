#/usr/bin/python
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)
print(res)

# Individual data
print(res["Kelly"])


sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]

if 20 in sampleDict.values():
    print('20 present in a dict')
else:
    print('20 NOT in a dict')
