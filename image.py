from PIL import Image, ImageFilter

img= Image.open('C:/Users/Shivangi rautela/sublime text/images/my_img.jpg')
filtered_img1 = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.SHARPEN)
filtered_img3 = img.filter(ImageFilter.SMOOTH)
filtered_img4 = img.convert('L')#L for gray scale image 
filtered_img1.save("blur.png",'png') #png supports image filters
filtered_img2.save("sharp.png",'png')
filtered_img3.save("smooth.png",'png')  # give new name and extension to a file using save 
crooked = filtered_img4.rotate(90)
crooked.save("gray_scaleimg.png",'png')
crooked.show()


print(img.mode)
print(img.format)
print(img.size)
print(dir(img))

