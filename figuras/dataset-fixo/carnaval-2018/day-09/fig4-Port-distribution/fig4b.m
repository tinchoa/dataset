figure
hold on
dstAttacks = csvread('fig4b-saidaportsDstAttacks.csv');
bar(dstAttacks(:,1),dstAttacks(:,2),'r')
dstNormal = csvread('fig4b-saidaportsDstNormal.csv');
bar(dstAttacks(:,1),dstAttacks(:,2),'g')
xlim([0 1024])
