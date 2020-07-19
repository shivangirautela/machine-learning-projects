from PIL import Image, ImageFilter

img= Image.open('original.jpg')
img.thumbnail((400,400)) #within 400 range thumbnail modifies the current image only and also keeps aspect ration same does not squish images 
img.save('thumbnail.jpg')

print(img.size) # image.size is giving actual size best to preview 
