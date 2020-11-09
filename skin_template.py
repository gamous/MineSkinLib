skin_template={
    'head':           {'top': ( 8,  0, 15,  7), 'bottom': (16,  0, 23,  7), 'right': ( 0,  8,  7, 15), 'front': ( 8,  8, 15, 15), 'left': (16,  8, 23, 15), 'back': (24,  8, 31, 15)},
    'head_outer':     {'top': (40,  0, 47,  7), 'bottom': (48,  0, 55,  7), 'right': (32,  8, 39, 15), 'front': (40,  8, 47, 15), 'left': (48,  8, 55, 15), 'back': (56,  8, 63, 15)},
    'right_leg':      {'top': ( 4, 16,  7, 19), 'bottom': ( 8, 16, 11, 19), 'right': ( 0, 20,  3, 31), 'front': ( 4, 20,  7, 31), 'left': ( 8, 20, 11, 31), 'back': (12, 20, 15, 31)},
    'right_arm':      {'top': (44, 16, 47, 19), 'bottom': (48, 16, 51, 19), 'right': (40, 20, 43, 31), 'front': (44, 20, 47, 31), 'left': (48, 20, 51, 31), 'back': (52, 20, 55, 31)},
    'body':           {'top': (20, 16, 23, 19), 'bottom': (28, 16, 35, 19), 'right': (16, 20, 19, 31), 'front': (20, 20, 27, 31), 'left': (28, 20, 31, 31), 'back': (32, 20, 39, 31)},
    'body_outer':     {'top': (20, 32, 23, 35), 'bottom': (28, 32, 35, 35), 'right': (16, 36, 19, 47), 'front': (20, 36, 27, 47), 'left': (28, 36, 31, 47), 'back': (32, 36, 39, 47)},
    'right_leg_outer':{'top': ( 4, 32,  7, 35), 'bottom': ( 8, 32, 11, 35), 'right': ( 0, 36,  3, 47), 'front': ( 4, 36,  7, 47), 'left': ( 8, 36, 11, 47), 'back': (12, 36, 15, 47)},
    'right_arm_outer':{'top': (44, 32, 47, 35), 'bottom': (48, 32, 51, 35), 'right': (40, 36, 43, 47), 'front': (44, 36, 47, 47), 'left': (48, 36, 51, 47), 'back': (52, 36, 55, 47)},
    'left_leg_outer': {'top': ( 4, 48,  7, 51), 'bottom': ( 8, 48, 11, 51), 'right': ( 0, 52,  3, 63), 'front': ( 4, 52,  7, 63), 'left': ( 8, 52, 11, 63), 'back': (12, 52, 15, 63)},
    'left_leg':       {'top': (20, 48, 23, 51), 'bottom': (24, 48, 27, 51), 'right': (16, 52, 19, 63), 'front': (20, 52, 23, 63), 'left': (24, 52, 27, 63), 'back': (28, 52, 31, 63)},
    'left_arm':       {'top': (36, 48, 39, 51), 'bottom': (40, 48, 43, 51), 'right': (32, 52, 35, 63), 'front': (36, 52, 39, 63), 'left': (40, 52, 43, 63), 'back': (44, 52, 47, 63)},
    'left_arm_outer': {'top': (52, 48, 55, 51), 'bottom': (56, 48, 59, 51), 'right': (48, 52, 51, 63), 'front': (52, 52, 55, 63), 'left': (56, 52, 59, 63), 'back': (60, 52, 63, 63)}
}
skin_template_old={
    'head':           {'top': ( 8,  0, 15,  7), 'bottom': (16,  0, 23,  7), 'right': ( 0,  8,  7, 15), 'front': ( 8,  8, 15, 15), 'left': (16,  8, 23, 15), 'back': (24,  8, 31, 15)},
    'hat':            {'top': (40,  0, 47,  7), 'bottom': (48,  0, 55,  7), 'right': (32,  8, 39, 15), 'front': (40,  8, 47, 15), 'left': (48,  8, 55, 15), 'back': (56,  8, 63, 15)},
    'leg':            {'top': ( 4, 16,  7, 19), 'bottom': ( 8, 16, 11, 19), 'right': ( 0, 20,  3, 31), 'front': ( 4, 20,  7, 31), 'left': ( 8, 20, 11, 31), 'back': (12, 20, 15, 31)},
    'arm':            {'top': (44, 16, 47, 19), 'bottom': (48, 16, 51, 19), 'right': (40, 20, 43, 31), 'front': (44, 20, 47, 31), 'left': (48, 20, 51, 31), 'back': (52, 20, 55, 31)},
    'body':           {'top': (20, 16, 23, 19), 'bottom': (28, 16, 35, 19), 'right': (16, 20, 19, 31), 'front': (20, 20, 27, 31), 'left': (28, 20, 31, 31), 'back': (32, 20, 39, 31)},
}

def trans(a,x,y):
    for  i in a:
        a[i]=list(a[i])
        a[i][0]+=x
        a[i][2]+=x
        a[i][1]+=y
        a[i][3]+=y
        a[i]=tuple(a[i])  
    return (a)

from PIL import Image

def rect_clear(im,rect):
    rect_size = tuple([rect[2]-rect[0]+1, rect[3]-rect[1]]+1)
    rect_pos = tuple([rect[0], rect[1]])
    brush = Image.new("RGBA", rect_size, (255, 255, 255, 0))
    im.paste(brush, rect_pos)

def outer_clear(im,skin):
    for section in skin:
        if "outer" in section and "head" not in section:
            for cover in skin[section]:
                rect_clear(im,skin[section][cover])

def isSkin(skin:Image):
    if (skin.height==32 or skin.height==64)and skin.width==64:return True
    return False

def isNewFormat(skin:Image):
    if skin.height==64:return True
    return False

def isOldFormat(skin:Image):
    if skin.height==32:return True
    return False

def Old2New(skin):
    if isNewFormat(skin):return
    new_skin=Image.new("RGBA",(64,64))
    for cover in skin_template["head"]:
        new_skin.paste(skin.crop(skin_template_old["head"][cover]),(skin_template["head"][cover][:2]))
    new_skin.show()
    new_skin.save("test2.png")
def dressing(skin_,cloth_,output_):
    try:
        skin = Image.open(skin_)
    except:
        print("[!]File not found: %s"%skin_)
        return
    try:
        cloth = Image.open(cloth_)
    except:
        print("[!]File not found: %s"%cloth_)
        return
    outer_clear(skin,skin_template)
    r,b,g,a=cloth.split()
    skin.paste(cloth,(0,32),mask = a)
    skin.paste(cloth,(0,32),mask = a)
    skin.save(output_)
    print("[INFO]:Suit %s's cloth on "%output_)

skin = Image.open("./Az_NokiaChrist.jpg")
print(isSkin(skin))
print(isOldFormat(skin))
print(isNewFormat(skin))
Old2New(skin)
dressing("./Az_sLivER_.jpg","./cloth/龙凤呈祥3.png","test.png")
#trans(skin_template['left_leg_outer'],48,0)