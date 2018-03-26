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
b.to_csv('saidaportsOrigenAttacks.csv')

###normal
a=normal.loc[:,1]
b=a.value_counts()
b.to_csv('saidaportsOrigenNormal.csv')


#no matlab
figure
hold on
orgAttacks = csvread('saidaportsOrigenAttacks.csv');
bar(orgAttacks(:,1),orgAttacks(:,2),'r')
orgNormal = csvread('saidaportsOrigenNormal.csv');
bar(orgNormal(:,1),orgNormal(:,2),'g')
xlim([0 1024])



##figura 4 'b'

###ataques
a=ataques.loc[:,3] #todos as portas
b=a.value_counts()
b.to_csv('saidaportsDstAttacks.csv')




###normal
a=normal.loc[:,3]
b=a.value_counts()
b.to_csv('saidaportsDstNormal.csv')


#no matlab
figure
hold on
dstAttacks = csvread('saidaportsDstAttacks.csv');
bar(dstAttacks(:,1),dstAttacks(:,2),'r')
dstNormal = csvread('saidaportsDstNormal.csv');
bar(dstAttacks(:,1),dstAttacks(:,2),'g')
xlim([0 1024])



##figura 5 'a'

#ataques
a=ataques.loc[:,25] 
a.to_csv('saidadurationAttack.csv')

#normal
a=normal.loc[:,25] 
a.to_csv('saidadurationNormal.csv')


#no matlab
figure
durationAttack = csvread('saidadurationAttack.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('saidadurationNormal.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')


##figura 5 'b'

#ataques
protoAtack=ataques.loc[:,4] #protocol
b=protoAtack.value_counts()
b.to_csv('saidaprotoAttack.csv')


#normal
protoNormal=normal.loc[:,4] #protocol
b=protoNormal.value_counts()
b.to_csv('saidaprotoNormal.csv')


#no matlab
figure
protoAttack = csvread('saidaprotoAttack.csv');
protoNormal = csvread('saidaprotoNormal.csv');
values=[protoNormal(1,2),protoAttack(1,2);protoNormal(2,2),protoAttack(2,2)];
bar(values);
set(gca,'xticklabel',{'TCP';'UDP'})


#figura 6 'a'

#ataques
a=ataques.loc[:,5]
a.to_csv('saidapacektNumberAttackFor.csv')

#normal
a=normal.loc[:,5] 
a.to_csv('saidapacektNumberNormalFor.csv')


#no matlab
figure
durationAttack = csvread('saidapacektNumberAttackFor.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('saidapacektNumberNormalFor.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 100])



#figura 6 'b'

#ataques
a=ataques.loc[:,10]
a.to_csv('saidaBytesAttackDown.csv')

#normal
a=normal.loc[:,10] 
a.to_csv('saidaBytesNormalDown.csv')

#no matlab
figure
durationAttack = csvread('saidaBytesAttackDown.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('saidaBytesNormalDown.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 200])
ylim([0 1])




#figura 7 'a'

#ataques
a=ataques.loc[:,6]
a.to_csv('saidaFlowSizeFor.csv')

#normal
a=normal.loc[:,6] 
a.to_csv('saidaFlowSizeBack.csv')


#no matlab
# figure
# durationAttack = csvread('saidaFlowSizeFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('saidaFlowSizeBack.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 100])



#figura 7 'b'

#ataques
a=ataques.loc[:,7]
a.to_csv('saidaFlowSizeBytesAttackDown.csv')

#normal
a=normal.loc[:,7] 
a.to_csv('saidaFlowSizeBytesNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('saidaFlowSizeBytesAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('saidaFlowSizeBytesNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylim([0 1])



#figura 8 'a'

#ataques
a=ataques.loc[:,35]
a.to_csv('saidaSubFlowBytesAttackFor.csv')

#normal
a=normal.loc[:,35] 
a.to_csv('saidaSubFlowBytesNormalFor.csv')


#no matlab
# figure
# durationAttack = csvread('saidaSubFlowBytesAttackFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('saidaSubFlowBytesNormalFor.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])



#figura 8 'b'

#ataques
a=ataques.loc[:,37]
a.to_csv('saidaSubFlowBytesAttackDown.csv')

#normal
a=normal.loc[:,37] 
a.to_csv('saidaSubFlowBytesNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('saidaSubFlowBytesAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('saidaSubFlowBytesNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylim([0 1])




#figura 9 'a'

#ataques
a=ataques.loc[:,42]
a.to_csv('saidaBytesHeaderAttackFor.csv')

#normal
a=normal.loc[:,42] 
a.to_csv('saidaBytesHeaderNormalFor.csv')


#no matlab
# figure
# durationAttack = csvread('saidaBytesHeaderAttackFor.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('saidaBytesHeaderNormalFor.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])



#figura 9 'b'

#ataques
a=ataques.loc[:,43]
a.to_csv('saidaBytesHeaderAttackDown.csv')

#normal
a=normal.loc[:,43] 
a.to_csv('saidaBytesHeaderNormalDown.csv')

#no matlab
# figure
# durationAttack = csvread('saidaBytesHeaderAttackDown.csv');
# [f,x] = ecdf(durationAttack(:,2));
# plot(f,'r')
# hold on
# durationNormal = csvread('saidaBytesHeaderNormalDown.csv');
# [f,x] = ecdf(durationNormal(:,2));
# plot(f,'g')
# xlim([0 1000])
# ylim([0 1])


