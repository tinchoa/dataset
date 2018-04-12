figure
durationAttack = csvread('fig7b-saidaFlowSizeBytesAttackDown-new.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig7b-saidaFlowSizeBytesNormalDown-new.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 1000])
ylim([0 1])
ylabel('Cumulative Distribution (CDF)');
xlabel('Flow Size (Byte)');