character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:

    # 특정 키가 딕셔너리인 경우
    if type(character[key]) is dict:
        for k in character[key]:
            print('{} : {}'.format(k, character[key][k]))
    
    # 특정 키가 리스트인 경우
    elif type(character[key]) is list:
        for item in character[key]: # item = 리스트의 요소
            print('{} : {}'.format(key, item))

    # 그 이외의 경우 (name, level)
    else:
        print('{} : {}'.format(key, character[key]))