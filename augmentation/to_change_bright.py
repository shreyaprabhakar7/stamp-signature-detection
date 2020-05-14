def bright_contrast (img1, alpha=1, beta=0):
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

dstpath =  # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in asme folder")

# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 

i=0
for image in tqdm(files):
    i+=1
    img = cv2.imread(join(path,image))
    bright = bright_contrast(img, alpha=1.4)
    start=image.find('(')
    end=image.find(')')
    img_number=int(image[start+1:end])
    new_image_name = image[:start+1]+str(img_number+count)+image[end:]
    dstPath = join(dstpath,new_image_name)
    cv2.imwrite(dstPath,bright)
    
count+=i
