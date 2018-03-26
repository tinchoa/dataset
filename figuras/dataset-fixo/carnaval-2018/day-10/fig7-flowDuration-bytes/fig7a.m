figure
durationAttack = csvread('fig7a-saidaFlowSizeFor.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig7a-saidaFlowSizeBack.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 100])
xlabel('Flow Size (Byte)');
ylabel('Cumulative Distribution (CDF)');