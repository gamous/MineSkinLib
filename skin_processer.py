
#! python3
#! requirements:pillow

#------------------------------------------------------#
#    _     _____  ____  _    _         _     _ _       #
#   / \   |__  / / ___|| | _(_)_ __   | |   (_) |__    #
#  / _ \    / /  \___ \| |/ / | '_ \  | |   | | '_ \   #
# / ___ \  / /_   ___) |   <| | | | | | |___| | |_) |  #
#/_/   \_\/____| |____/|_|\_\_|_| |_| |_____|_|_.__/   #
#              Mincraft Skin tool lib                  #
#           Version1 by Gamous 2020/7/30               #
#------------------------------------------------------#

skin_template={
    'head':           {'top': ( 8,  0, 16,  8), 'bottom': (16,  0, 24,  8), 'right': ( 0,  8,  8, 16), 'front': ( 8,  8, 16, 16), 'left': (16,  8, 24, 16), 'back': (24,  8, 32, 16)},
    'head_outer':     {'top': (40,  0, 48,  8), 'bottom': (48,  0, 56,  8), 'right': (32,  8, 40, 16), 'front': (40,  8, 48, 16), 'left': (48,  8, 56, 16), 'back': (56,  8, 64, 16)},
    'right_leg':      {'top': ( 4, 16,  8, 20), 'bottom': ( 8, 16, 12, 20), 'right': ( 0, 20,  4, 32), 'front': ( 4, 20,  8, 32), 'left': ( 8, 20, 12, 32), 'back': (12, 20, 16, 32)},
    'right_arm':      {'top': (44, 16, 48, 20), 'bottom': (48, 16, 52, 20), 'right': (40, 20, 44, 32), 'front': (44, 20, 48, 32), 'left': (48, 20, 52, 32), 'back': (52, 20, 56, 32)},
    'body':           {'top': (20, 16, 24, 20), 'bottom': (28, 16, 36, 20), 'right': (16, 20, 20, 32), 'front': (20, 20, 28, 32), 'left': (28, 20, 32, 32), 'back': (32, 20, 40, 32)},
    'body_outer':     {'top': (20, 32, 24, 36), 'bottom': (28, 32, 36, 36), 'right': (16, 36, 20, 48), 'front': (20, 36, 28, 48), 'left': (28, 36, 32, 48), 'back': (32, 36, 40, 48)},
    'right_leg_outer':{'top': ( 4, 32,  8, 36), 'bottom': ( 8, 32, 12, 36), 'right': ( 0, 36,  4, 48), 'front': ( 4, 36,  8, 48), 'left': ( 8, 36, 12, 48), 'back': (12, 36, 16, 48)},
    'right_arm_outer':{'top': (44, 32, 48, 36), 'bottom': (48, 32, 52, 36), 'right': (40, 36, 44, 48), 'front': (44, 36, 48, 48), 'left': (48, 36, 52, 48), 'back': (52, 36, 56, 48)},
    'left_leg_outer': {'top': ( 4, 48,  8, 52), 'bottom': ( 8, 48, 12, 52), 'right': ( 0, 52,  4, 64), 'front': ( 4, 52,  8, 64), 'left': ( 8, 52, 12, 64), 'back': (12, 52, 16, 64)},
    'left_leg':       {'top': (20, 48, 24, 52), 'bottom': (24, 48, 28, 52), 'right': (16, 52, 20, 64), 'front': (20, 52, 24, 64), 'left': (24, 52, 28, 64), 'back': (28, 52, 32, 64)},
    'left_arm':       {'top': (36, 48, 40, 52), 'bottom': (40, 48, 44, 52), 'right': (32, 52, 36, 64), 'front': (36, 52, 40, 64), 'left': (40, 52, 44, 64), 'back': (44, 52, 48, 64)},
    'left_arm_outer': {'top': (52, 48, 56, 52), 'bottom': (56, 48, 60, 52), 'right': (48, 52, 52, 64), 'front': (52, 52, 56, 64), 'left': (56, 52, 60, 64), 'back': (60, 52, 64, 64)}
}
skin_template_alex={
    'head':           {'top': ( 8,  0, 16,  8), 'bottom': (16,  0, 24,  8), 'right': ( 0,  8,  8, 16), 'front': ( 8,  8, 16, 16), 'left': (16,  8, 24, 16), 'back': (24,  8, 32, 16)},
    'head_outer':     {'top': (40,  0, 48,  8), 'bottom': (48,  0, 56,  8), 'right': (32,  8, 40, 16), 'front': (40,  8, 48, 16), 'left': (48,  8, 56, 16), 'back': (56,  8, 64, 16)},
    'right_leg':      {'top': ( 4, 16,  8, 20), 'bottom': ( 8, 16, 12, 20), 'right': ( 0, 20,  4, 32), 'front': ( 4, 20,  8, 32), 'left': ( 8, 20, 12, 32), 'back': (12, 20, 16, 32)},
    'body':           {'top': (20, 16, 24, 20), 'bottom': (28, 16, 36, 20), 'right': (16, 20, 20, 32), 'front': (20, 20, 28, 32), 'left': (28, 20, 32, 32), 'back': (32, 20, 40, 32)},
    'body_outer':     {'top': (20, 32, 24, 36), 'bottom': (28, 32, 36, 36), 'right': (16, 36, 20, 48), 'front': (20, 36, 28, 48), 'left': (28, 36, 32, 48), 'back': (32, 36, 40, 48)},
    'right_leg_outer':{'top': ( 4, 32,  8, 36), 'bottom': ( 8, 32, 12, 36), 'right': ( 0, 36,  4, 48), 'front': ( 4, 36,  8, 48), 'left': ( 8, 36, 12, 48), 'back': (12, 36, 16, 48)},
    'left_leg_outer': {'top': ( 4, 48,  8, 52), 'bottom': ( 8, 48, 12, 52), 'right': ( 0, 52,  4, 64), 'front': ( 4, 52,  8, 64), 'left': ( 8, 52, 12, 64), 'back': (12, 52, 16, 64)},
    'left_leg':       {'top': (20, 48, 24, 52), 'bottom': (24, 48, 28, 52), 'right': (16, 52, 20, 64), 'front': (20, 52, 24, 64), 'left': (24, 52, 28, 64), 'back': (28, 52, 32, 64)},
    'right_arm':      {'top': (44, 16, 47, 20), 'bottom': (47, 16, 50, 20), 'right': (40, 20, 44, 32), 'front': (44, 20, 47, 32), 'left': (48, 20, 50, 32), 'back': (50, 20, 54, 32)},
    'right_arm_outer':{'top': (44, 32, 47, 36), 'bottom': (47, 32, 50, 36), 'right': (40, 36, 44, 48), 'front': (44, 36, 47, 48), 'left': (48, 36, 50, 48), 'back': (50, 36, 54, 48)},
    'left_arm':       {'top': (36, 48, 39, 52), 'bottom': (39, 48, 42, 52), 'right': (32, 52, 36, 64), 'front': (36, 52, 39, 64), 'left': (40, 52, 42, 64), 'back': (42, 52, 46, 64)},
    'left_arm_outer': {'top': (52, 48, 55, 52), 'bottom': (55, 48, 58, 52), 'right': (48, 52, 52, 64), 'front': (52, 52, 55, 64), 'left': (56, 52, 58, 64), 'back': (58, 52, 62, 64)}
}
skin_template_old={
    'head':           {'top': ( 8,  0, 16,  8), 'bottom': (16,  0, 24,  8), 'right': ( 0,  8,  8, 16), 'front': ( 8,  8, 16, 16), 'left': (16,  8, 24, 16), 'back': (24,  8, 32, 16)},
    'hat':            {'top': (40,  0, 48,  8), 'bottom': (48,  0, 56,  8), 'right': (32,  8, 40, 16), 'front': (40,  8, 48, 16), 'left': (48,  8, 56, 16), 'back': (56,  8, 64, 16)},
    'leg':            {'top': ( 4, 16,  8, 20), 'bottom': ( 8, 16, 12, 20), 'right': ( 0, 20,  4, 32), 'front': ( 4, 20,  8, 32), 'left': ( 8, 20, 12, 32), 'back': (12, 20, 16, 32)},
    'arm':            {'top': (44, 16, 48, 20), 'bottom': (48, 16, 52, 20), 'right': (40, 20, 44, 32), 'front': (44, 20, 48, 32), 'left': (48, 20, 52, 32), 'back': (52, 20, 56, 32)},
    'body':           {'top': (20, 16, 24, 20), 'bottom': (28, 16, 36, 20), 'right': (16, 20, 20, 32), 'front': (20, 20, 28, 32), 'left': (28, 20, 32, 32), 'back': (32, 20, 40, 32)},
}

#a func to clac skin template
def trans(a,x,y):
    for  i in a:
        a[i]=list(a[i])
        a[i][0]+=x
        a[i][2]+=x
        a[i][1]+=y
        a[i][3]+=y
        a[i]=tuple(a[i])  
    return (a)
#print(trans(skin_template_alex['left_arm'],8,-32))


from PIL import Image

def get_rect_size(rect):
    return tuple([rect[2]-rect[0], rect[3]-rect[1]])

def rect_clear(im,rect):
    rect_size = get_rect_size(rect)
    rect_pos = tuple([rect[0], rect[1]])
    brush = Image.new("RGBA", rect_size, (255, 255, 255, 0))
    im.paste(brush, rect_pos)

def outer_clear(skin):
    for section in skin_template:
        if "outer" in section and "head" not in section:
            for cover in skin_template[section]:
                rect_clear(skin,skin_template[section][cover])

def outer2inner(skin):
    for section in skin_template:
        if "outer" in section and "head" not in section:
            for cover in skin_template[section]:
                layer=skin.crop(skin_template[section][cover])
                r,b,g,a=layer.split()
                skin.paste(layer,(skin_template[section[:-6]][cover][:2]),mask = a)
    outer_clear(skin)
    return skin

def isSkin(skin:Image):
    if (skin.height==32 or skin.height==64)and skin.width==64:return True
    return False

def isNewFormat(skin:Image):
    if skin.height==64:return True
    return False

def isOldFormat(skin:Image):
    if skin.height==32:return True
    return False

def isCloth(cloth:Image):
    if cloth.height<=32 or cloth.height==64:return True
    return False

def Old2New(skin):
    if isNewFormat(skin):return
    new_skin=Image.new("RGBA",(64,64))
    for cover in skin_template["head"]:
        new_skin.paste(skin.crop(skin_template_old["head"][cover]),(skin_template["head"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["hat"][cover]),(skin_template["head_outer"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["leg"][cover]),(skin_template["right_leg"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["leg"][cover]),(skin_template["left_leg"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["body"][cover]),(skin_template["body"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["arm"][cover]),(skin_template["right_arm"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["arm"][cover]),(skin_template["left_arm"][cover][:2]))
    return new_skin

def Old2New_wihoutHat(skin):
    if isNewFormat(skin):return
    new_skin=Image.new("RGBA",(64,64))
    for cover in skin_template["head"]:
        new_skin.paste(skin.crop(skin_template_old["head"][cover]),(skin_template["head"][cover][:2]))
        #new_skin.paste(skin.crop(skin_template_old["hat"][cover]),(skin_template["head_outer"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["leg"][cover]),(skin_template["right_leg"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["leg"][cover]),(skin_template["left_leg"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["body"][cover]),(skin_template["body"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["arm"][cover]),(skin_template["right_arm"][cover][:2]))
        new_skin.paste(skin.crop(skin_template_old["arm"][cover]),(skin_template["left_arm"][cover][:2]))
    return new_skin

def get_head(skin,size=256,scale=0.88):
    head       = skin.crop(skin_template["head"]["front"]).resize((int(size*scale),int(size*scale)),resample=Image.BOX)
    head_outer = skin.crop(skin_template["head_outer"]["front"]).resize((size, size),resample=Image.BOX)
    img=Image.new("RGBA",(size, size))
    img.paste(head,((int(size*(1-scale)/2),int(size*(1-scale)/2))))
    r,b,g,a=head_outer.split()
    img.paste(head_outer,(0,0),mask = a)
    return img

def open_skin(path):
    try:
        skin = Image.open(path)
        if not isSkin(skin):
            print("[!]File not skin!")
        if isOldFormat(skin):
            print("[+]1.7skin detected, converting.")
            skin=Old2New(skin)
        return skin
    except:
        print("[!]File not found: %s"%path)
        exit()

def open_cloth(path):
    try:
        cloth = Image.open(path)
        if not isCloth(cloth):
            print("[!]File not cloth!")
        return cloth
    except:
        print("[!]File not found: %s"%path)
        exit()
        return

def alex_cloth(cloth):
    temp=Image.new("RGBA",(64,64))
    temp.paste(cloth,(0,32))
    cloth=temp
    new_cloth=Image.new("RGBA",(64,64))
    for section in skin_template:
        if "outer" in section and "head" not in section:
            for cover in skin_template[section]:
                new_cloth.paste(cloth.crop(skin_template[section][cover]).resize(get_rect_size(skin_template_alex[section][cover])),(skin_template_alex[section][cover][:2]))
                print("section:%s,cover:%s"%(section,cover))
    return new_cloth.crop((0,32,64,64))

def dressing(skin,cloth):
    outer_clear(skin)
    r,b,g,a=cloth.split()
    offset = 0 if cloth.height==64 else 32
    skin.paste(cloth,(0,offset),mask = a)
    skin.paste(cloth,(0,offset),mask = a)
    return skin
    #print("[INFO]:Suit %s's cloth on "%output_)
