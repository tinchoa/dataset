import pandas as pd
import numpy as np
import sys


arquivo=open(sys.argv[1])


df=pd.read_csv(arquivo,header=None)
ataques=df.loc[df[45] != 0]
normal=df.loc[df[45] == 0]


##figura 4 'a'

###ataques
a=ataques.loc[:,1] #todos as portas
b=a.value_counts()
b.to_csv('fig4a-saidaportsOrigenAttacks.csv')

###normal
a=normal.loc[:,1]
b=a.value_counts()
b.to_csv('fig4a-saidaportsOrigenNormal.csv')


#no matlab
# figure
# hold on
# orgAttacks = csvread('fig4a-saidaportsOrigenAttacks.csv');
# bar(orgAttacks(:,1),orgAttacks(:,2),'r')
# orgNormal = csvread('fig4a-saidaportsOrigenNormal.csv');
# bar(orgNormal(:,1),orgNormal(:,2),'g')
# xlim([0 1024])



##figura 4 'b'

###ataques
a=ataques.loc[:,3] #todos as portas
b=a.value_counts()
b.to_csv('fig4b-saidaportsDstAttacks.csv')




###normal
a=normal.loc[:,3]
b=a.value_counts()
b.to_csv('fig4b-saidaportsDstNormal.csv')


#no matlab
# figure
# hold on
# dstAttacks = csvread('fig4b-saidaportsDstAttacks.csv');
# bar(dstAttacks(:,1),dstAttacks(:,2),'r')
# dstNormal = csvread('fig4b-saidaportsDstNormal.csv');
# bar(dstAttacks(:,1),dstAttacks(:,2),'g')
# xlim([0 1024])



##figura 5 'a'

#ataques
a=ataques.loc[:,25] 
a.to_csv('fig5a-saidadurationAttack.csv')

#normal
a=normal.loc[:,25] 
a.to_csv('fig5a-saidadurationNormal.csv')


#no matlab
# figure
# durationAttack = csvread('fig5a-saidadurationAttack.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig5a-saidadurationNormal.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# ylabel('Cumulative Distribution (CDF)');
# xlabel('Flow Duration (ms)');


##figura 5 'b'

#ataques
protoAtack=ataques.loc[:,4] #protocol
b=protoAtack.value_counts()
b.to_csv('fig5b-saidaprotoAttack.csv')


#normal
protoNormal=normal.loc[:,4] #protocol
b=protoNormal.value_counts()
b.to_csv('fig5b-saidaprotoNormal.csv')


#no matlab
# figure
# protoAttack = csvread('fig5b-saidaprotoAttack.csv');
# protoNormal = csvread('fig5b-saidaprotoNormal.csv');
# values=[protoNormal(1,2),protoAttack(1,2);protoNormal(2,2),protoAttack(2,2)];
# bar(values);
# set(gca,'xticklabel',{'TCP';'UDP'})
# ylabel('Number of Flows');

#figura 6 'a'

#ataques
a=ataques.loc[:,5]
a.to_csv('fig6a-saidapacektNumberAttackFor.csv')

#normal
a=normal.loc[:,5] 
a.to_csv('fig6a-saidapacektNumberNormalFor.csv')


#no matlab
# figure
# durationAttack = csvread('fig6a-saidapacektNumberAttackFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig6a-saidapacektNumberNormalFor.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 100])
# ylabel('Cumulative Distribution Function (CDF)');
# xlabel('Packets Number');


#figura 6 'b'

#ataques
a=ataques.loc[:,10]
a.to_csv('fig6b-saidaBytesAttackDown.csv')

#normal
a=normal.loc[:,10] 
a.to_csv('fig6b-saidaBytesNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('fig6b-saidaBytesAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig6b-saidaBytesNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 200])
# ylim([0 1])
# ylabel('Cumulative Distribution (CDF)');
# xlabel('Bytes per Flow');



#figura 7 'a'

#ataques
a=ataques.loc[:,6]
a.to_csv('fig7a-saidaFlowSizeFor.csv')

#normal
a=normal.loc[:,6] 
a.to_csv('fig7a-saidaFlowSizeBack.csv')


#no matlab
# figure
# durationAttack = csvread('fig7a-saidaFlowSizeFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig7a-saidaFlowSizeBack.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 100])
# xlabel('Flow Size (Byte)');
# ylabel('Cumulative Distribution (CDF)');


#figura 7 'b'

#ataques
a=ataques.loc[:,7]
a.to_csv('fig7b-saidaFlowSizeBytesAttackDown.csv')

#normal
a=normal.loc[:,7] 
a.to_csv('fig7b-saidaFlowSizeBytesNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('fig7b-saidaFlowSizeBytesAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig7b-saidaFlowSizeBytesNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylim([0 1])
# ylabel('Cumulative Distribution (CDF)');
# xlabel('Flow Size (Byte)');



#figura 8 'a'

#ataques
a=ataques.loc[:,35]
a.to_csv('fig8a-saidaSubFlowBytesAttackFor.csv')

#normal
a=normal.loc[:,35] 
a.to_csv('fig8a-saidaSubFlowBytesNormalFor.csv')


#no matlab
# figure
# durationAttack = csvread('fig8a-saidaSubFlowBytesAttackFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig8a-saidaSubFlowBytesNormalFor.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylabel('Cumulative Distribution (CDF)');
# xlabel('SubFlows Size (Bytes)');



#figura 8 'b'

#ataques
a=ataques.loc[:,37]
a.to_csv('fig8b-saidaSubFlowBytesAttackDown.csv')

#normal
a=normal.loc[:,37] 
a.to_csv('fig8b-saidaSubFlowBytesNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('fig8b-saidaSubFlowBytesAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig8b-saidaSubFlowBytesNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylim([0 1])
# ylabel('Cumulative Distribution (CDF)');
# xlabel('SubFlows Size (Bytes)');



#figura 9 'a'

#ataques
a=ataques.loc[:,42]
a.to_csv('fig9a-saidaBytesHeaderAttackFor.csv')

#normal
a=normal.loc[:,42] 
a.to_csv('fig9a-saidaBytesHeaderNormalFor.csv')


#no matlab
# figure
# durationAttack = csvread('fig9a-saidaBytesHeaderAttackFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig9a-saidaBytesHeaderNormalFor.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylabel('Cumulative Distribution (CDF)');
# xlabel('Total bytes used in headers (Bytes)');



#figura 9 'b'

#ataques
a=ataques.loc[:,43]
a.to_csv('fig9b-saidaBytesHeaderAttackDown.csv')

#normal
a=normal.loc[:,43] 
a.to_csv('fig9b-saidaBytesHeaderNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('fig9b-saidaBytesHeaderAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('fig9b-saidaBytesHeaderNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylim([0 1])
# ylabel('Cumulative Distribution (CDF)');
# xlabel('Total bytes used in headers (Bytes)');
