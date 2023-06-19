#/usr/bin/python
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sample_dict, key=sample_dict.get))

#List + List = Dict
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res_dict = dict(zip(keys, values))
print(keys)
print(values)
print(res_dict)


#Dict + Dict = Dict
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)

#Nested Dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

# solution
print(sampleDict['class']['student']['marks']['history'])
