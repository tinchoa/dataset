from subprocess import Popen, PIPE
import os, shutil

file=open('folders3','r')
date=[]
a=file.readlines()
for i in range(len(a)):
        print 'analizing ' +str(a[i])
        a[i]=a[i].replace('\n','')
        (stdout, stderr) = Popen(["head",a[i]+'/eve-test.json'], stdout=PIPE).communicate()
        b=stdout.split('flow_id')
        aux=b[0].split('timestamp')
        z=aux[1].split('T')
        z=z[0].split(':')[1].split('"')[1]
        if not os.path.exists(z):
                os.makedirs(z)
                date.append(z)
                shutil.move(a[i],z)
        else:
                shutil.move(a[i],z)

