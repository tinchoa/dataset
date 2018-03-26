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
ylabel('Cumulative Distribution (CDF)');
xlabel('Bytes per Flow');