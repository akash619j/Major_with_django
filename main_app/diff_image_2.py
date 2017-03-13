#Video compression code on the basis of difference in consecutive frames

import soldier
from itertools import izip
import Image
noi=200
tokeep=[]
i=0
cnt=1

#print soldier.run('cp ').output


while (i<=noi-1):
    tokeep.append(i)
    soldier.run('cp '+str(i+1)+'.jpg Final_Frames').output
    if cnt>200:
    	break
    	
    for j in range(i+1,noi):
    	
        file1=str(i)+".jpg"
        file2=str(j)+".jpg"
        cnt=cnt+1
        if cnt>200:
        	break
        i1 = Image.open(file1)
        i2 = Image.open(file2)
        size = 400, 400
        im_resized = i1.resize(size, Image.ANTIALIAS)
        im_resized.save(file1, "JPEG")
        im_resized2 = i2.resize(size, Image.ANTIALIAS)
        im_resized2.save(file2, "JPEG")
#assert i1.mode == i2.mode, "Different kinds of images."
#assert i1.size == i2.size, "Different sizes."
   	pairs = izip(im_resized.getdata(), im_resized2.getdata())
    	if len(i1.getbands()) == 1:
    # for gray-scale jpegs
       	 	dif = sum(abs(p1-p2) for p1,p2 in pairs)
	else:
	        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

        ncomponents = i1.size[0] * i1.size[1] * 3
        perc=(dif / 255.0) * 100 / ncomponents
        print perc
        if(perc>=20):   #not similar frames!
                i=j
                break
	if j==noi:
		fl=1        
        #print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents
for i in range(0,len(tokeep)):
        print tokeep[i]
