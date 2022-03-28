import os

from PIL import Image,ImageDraw,ImageFont

def get_concat_h(imgs):
    images = []
    font = ImageFont.truetype("arial.ttf",size=35)
    for i in imgs:
        img = Image.open('downloads/images/'+i)
        img.resize((min(img.width,img.height),min(img.width,img.height)))
        img.thumbnail((300,200))
        draw = ImageDraw.Draw(img)
        draw.text((10, 10),i.split('.')[1],font=font,fill='black')
        images.append(img)

    dst = Image.new('RGB',(600,600))
    dst.paste(images[0],(0, 0))
    dst.paste(images[1],(0, 200))
    dst.paste(images[2],(0, 400))
    dst.paste(images[3],(300, 0))
    dst.paste(images[4],(300, 200))
    dst.paste(images[5],(300, 400))
    img_name = 'downloads/gr_images/gr.'
    for i in imgs:
        img_name += i.split('.')[1]+'_'
    img_name=img_name+'.jpg'
    dst.save(img_name)
    return img_name

def get_gr_photo(keys):
    images = []
    print(keys)
    for img in os.listdir('downloads/gr_images'):
        print(img)
        if keys.sort() == img.split('.')[1].split('_').sort():
            print('old')
            return 'downloads/gr_images/'+img
    else:
        for file in os.listdir('downloads/images'):
            if file.split('.')[1] in keys:
                images.append(file)
        print('new')
        return get_concat_h(images)
