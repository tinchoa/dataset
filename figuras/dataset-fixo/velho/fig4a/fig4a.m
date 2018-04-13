figure
orgAttacks = csvread('fig4a-saidaportsOrigenAttacksnew.csv');
bar(orgAttacks(:,1),orgAttacks(:,2),'r')
hold on
orgNormal = csvread('fig4a-saidaportsOrigenNormalnew.csv');
bar(orgNormal(:,1),orgNormal(:,2),'g')
xlim([0 1024])