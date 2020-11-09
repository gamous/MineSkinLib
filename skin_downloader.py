#! python3
#! requirements:requests
#Version3 by Gamous 2020/5/17

import requests,json,base64,os,sys,time

def get_uuid(name):
    res=json.loads(requests.get('https://api.mojang.com/users/profiles/minecraft/'+name).text)
    #if res.has_key("error"):
    #    print("[!]Name Not Found")
    #    return 0
    print(res["id"])
    return res["id"]

def get_history(uuid):
    if(uuid):
        history = json.loads(requests.get('https://api.mojang.com/user/profiles/%s/names'%uuid).text)
        for used in history:
            print("[USED]:"+used["name"])

def get_skin(uuid):
    return json.loads(base64.b64decode(json.loads(requests.get('https://sessionserver.mojang.com/session/minecraft/profile/'+uuid).text)["properties"][0]["value"]))["textures"]["SKIN"]["url"]

def down_skin(url,path):
    if not os.path.exists("./skin"):
        os.makedirs("./skin")
    if not os.path.exists("./head"):
        os.makedirs("./head") 
    with open(path, 'wb') as f:
        f.write(requests.get(url).content)
    print("[INFO]:Skin downloaded on "+path)

def getOne(name):
        uuid=get_uuid(name)
        print("[UUID]:"+uuid)
        get_history(uuid)
        skin=get_skin(uuid)
        print("[SKIN]:"+skin)
        down_skin(skin,"./skin/%s.jpg"%(name))
