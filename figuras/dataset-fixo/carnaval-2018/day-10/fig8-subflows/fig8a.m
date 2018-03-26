figure
durationAttack = csvread('fig8a-saidaSubFlowBytesAttackFor.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig8a-saidaSubFlowBytesNormalFor.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 1000])
ylabel('Cumulative Distribution (CDF)');
xlabel('SubFlows Size (Bytes)');