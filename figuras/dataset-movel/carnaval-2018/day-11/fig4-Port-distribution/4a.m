figure
orgAttacks = csvread('saidaportsOrigenAttacks.csv');
bar(orgAttacks(:,1),orgAttacks(:,2),'r')
hold on
orgNormal = csvread('saidaportsOrigenNormal.csv');
bar(orgNormal(:,1),orgNormal(:,2),'g')
xlim([0 1024])