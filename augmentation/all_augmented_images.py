srcpath_list = [r'original images path',r'#grayscled images path',r'#brightness changed images path',r'#contrast changesd images path',r'#hls images path']
dstpath_new = # dest folder path
for dstpath in srcpath_list:
    files = [f for f in listdir(dstpath) if isfile(join(dstpath,f))]
    for image in tqdm(files):
        copyfile(join(dstpath,image), join(dstpath_new,image))
