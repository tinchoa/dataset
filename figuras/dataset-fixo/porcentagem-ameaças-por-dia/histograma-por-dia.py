'''
all files are originally in @sepetiba:/home/dataset/nPPoe

this script will take the relation in % of flows atacks in each day

Output is a csv with the porcentage of flows :
day,totalFlows,ataques,normal,porcentageAttacks
'''

import pandas as pd
import numpy as np


dias=['classes-16.out','classes-17.out','classes-18.out','classes-19.out','classes-20.out','classes-21.out','classes-24.out','classes-25.out','classes-26.out','classes-27.out','classes-28.out','classes-01.out','classes-02.out','classes-03.out']

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

#no matlab
'''
figure
formatSpec = '%s%f%f%f%f%[^\n\r]';
delimiter = ',';

fileID = fopen('porcentages.csv','r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
fclose(fileID);

day = dataArray{:, 1};
day=['Day 16';'Day 17';'Day 18';'Day 19';'Day 20';'Day 21';'Day 22'];
totalFlows = dataArray{:, 2};
ataques = dataArray{:, 3};
normal = dataArray{:, 4};
porcentageAttacks = dataArray{:, 5};
bar(porcentageAttacks)
set(gca,'xticklabel',day)
ylabel('Percentage of Threats');
ylim([0 40])




'''




