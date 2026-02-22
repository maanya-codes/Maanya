data = {
    "id1":{"name": "Sara","class":"V","subj_int":"PCM"},
    "id2":{"name":"Aryan" ,"class":"V","subj_int":"BCM"},
    "id3":{"name":"Snithik" ,"class":"V","subj_int": "PCME"},
    "id4":{"name": "Sara","class":"V","subj_int":"PCM"},
}

result = {}
seen = set()

for tempholder, i in data.items():
    unqkey = (i["name"], i["class"], i["subj_int"])
    if unqkey not in seen:
        seen.add(unqkey)
        result[tempholder] = i

for k, v in result.items():
    print(k, ":", v)
