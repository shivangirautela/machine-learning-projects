from PIL import Image,ImageFilter

img= Image.open('C:/Users/Shivangi rautela/sublime text/images/my_img.jpg')

filtered_img= img.convert('L')
resize = filtered_img.resize((300,300))
resize.save('resized_gray.png','png')

box=(50,50,100,100)
region = filtered_img.crop(box)
region.save('cropped.png','png')


