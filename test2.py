import json
import re
data = input('input json data:')
dic1 = json.loads(data)
data_list = [dic1]
keys = list(dic1.keys())
values = list(dic1.values())
for i in keys:
        dic_copy = json.loads(data)
        del dic_copy[i]
        data_list.append(dic_copy)
        dic_copy = json.loads(data)
        if type(dic_copy[i])==str:
                dic_copy[i]=''
                data_list.append(dic_copy)
        elif bool(re.search(r'\d',str(dic_copy[i]))):
                dic_copy[i]=65535
                data_list.append(dic_copy)
for i in data_list:
        print(i)