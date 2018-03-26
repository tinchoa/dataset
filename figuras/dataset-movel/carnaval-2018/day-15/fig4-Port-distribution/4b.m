figure
hold on
dstAttacks = csvread('saidaportsDstAttacks.csv');
bar(dstAttacks(:,1),dstAttacks(:,2),'r')
dstNormal = csvread('saidaportsDstNormal.csv');
bar(dstAttacks(:,1),dstAttacks(:,2),'g')
xlim([0 1024])
