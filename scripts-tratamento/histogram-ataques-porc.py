'''
this script will take the relation in % of flows atacks in each day

Output is a csv with the porcentage of flows :
day,totalFlows,ataques,normal,porcentageAttacks
'''

import pandas as pd
import numpy as np


dias=['classes-16.out','classes-17.out','classes-18.out','classes-19.out','classes-20.out','classes-21.out','classes-27.out']

porcentages={}

output=open('porcentage.csv','w')

for arq in dias:
	print 'analizing file: ' +str(arq)
	arquivo=open(arq)
	df=pd.read_csv(arquivo,header=None)
	ataques=df.loc[df[45] != 0]
	normal=df.loc[df[45] == 0]
	total=df.shape[0] #total flows in 
	qtdAtaques=ataques.shape[0]
	qtdNormales=normal.shape[0]
	por=(qtdAtaques*100)/float(total)
	porcentages[arq]=total,qtdAtaques,qtdNormales,por
	output.write(arq+','+str(total)+','+str(qtdAtaques)+','+str(qtdNormales)+','+str(por)+'\n')


output.close()





