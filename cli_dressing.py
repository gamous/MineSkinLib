import argparse,base64,os,sys
from PIL import Image
import skin_template

def get_parser():
    parser = argparse.ArgumentParser(description='Dressing your minecraft skin(work on 1.8)')
    parser.add_argument('-i','--input', help="name of intput skin")
    parser.add_argument('-u','--cloth', help="name of suite file")
    parser.add_argument('-o','--output',nargs='?', help="name of output skin")
    return parser

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
    
    r,b,g,a=cloth.split()
    skin.paste(cloth,(0,32),mask = a)
    skin.save(output_)
    print("[INFO]:Suit %s's cloth on "%output_)

def main():
    parser = get_parser()
    args = parser.parse_args()
    if not (args.cloth and args.input):
        parser.print_help()
        return
    if not args.output:
        print(os.path.splitext(os.path.basename(args.input))[0])
        args.output=   os.path.splitext(os.path.basename(args.input))[0] + ' with ' +  os.path.splitext(os.path.basename(args.cloth))[0] +'.png'
    dressing(args.input,args.cloth,args.output)
    return 1
if __name__ == "__main__":
    main()

