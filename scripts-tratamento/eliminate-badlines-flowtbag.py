
fileOld=open('classes-20.out','r')


lines=fileOld.readlines()

fileNew=open('featuresNew.out','w')




for i in range(len(lines)):
        e=lines[i].split(',')
        if ((len(e) == 46) ):
                k=0
                for j in e:
                        if len(j) == 0:
                                k=1
                if k==0:
                        fileNew.write(lines[i])

fileOld.close()
fileNew.close()
