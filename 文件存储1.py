import json

data = [{
    'name' : '王伟',
    'gender' : 'male',
    'birthday' : '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:#这里用uft-8编码不然默认Unicode
    file.write(json.dumps(data, indent=2, ensure_ascii=False))#这里ensure_ascii为false，暂且不知道为什么