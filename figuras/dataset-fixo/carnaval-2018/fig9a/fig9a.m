figure
durationAttack = csvread('fig9a-saidaBytesHeaderAttackFor-new.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig9a-saidaBytesHeaderNormalFor-new.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 1000])
ylabel('Cumulative Distribution (CDF)');
xlabel('Total bytes used in headers (Bytes)');