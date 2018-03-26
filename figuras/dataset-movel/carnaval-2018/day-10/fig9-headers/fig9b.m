figure
durationAttack = csvread('saidaBytesHeaderAttackDown.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('saidaBytesHeaderNormalDown.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 1000])
ylim([0 1])
ylabel('Cumulative Distribution (CDF)');
xlabel('Total bytes used in headers (Bytes)');