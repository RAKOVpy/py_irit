import json
import requests

req = requests.get('https://swapi.dev/api/starships/')
data = json.loads(req.text)
flag = False
ans_print = dict()

while True:
    if data['next'] is None:
        break
    for result in data['results']:
        if result['name'] == 'Millennium Falcon':
            temp = result['pilots']
            result['pilots'] = []
            for pilot_url in temp:
                find_indexs = ['name', 'height', 'mass', 'homeworld', 'homeworld_url']
                ans_dict_append_find = json.loads(requests.get(pilot_url).text)
                ans_dict_append_find['homeworld_url'] = ans_dict_append_find['homeworld']
                ans_dict_append_find['homeworld'] = json.loads(
                    requests.get(ans_dict_append_find['homeworld']).text)['name']
                result['pilots'].append({i: ans_dict_append_find[i] for i in find_indexs})

            new_indexs = ['ship_name', 'starship_class', 'max_atmosphering_speed', 'pilots']
            old_indexs = ['name', 'starship_class', 'max_atmosphering_speed', 'pilots']
            ans_print = {j: result[old_indexs[i]] for i, j in enumerate(new_indexs)}
            flag = True
            break
    if flag:
        break
    req = requests.get(data['next'])
    data = json.loads(req.text)

print(json.dumps(ans_print, indent=4))
with open('ans.json', 'w') as f:
    json.dump(ans_print, f, indent=4)
