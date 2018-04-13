figure
durationAttack = csvread('fig6b-saidaBytesAttackDownnew.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig6b-saidaBytesNormalDownnew.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 200])
ylim([0 1])
ylabel('Cumulative Distribution (CDF)');
xlabel('Bytes per Flow');