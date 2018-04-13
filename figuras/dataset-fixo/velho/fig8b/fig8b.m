figure
durationAttack = csvread('fig8b-saidaSubFlowBytesAttackDownnew.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig8b-saidaSubFlowBytesNormalDownnew.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 1000])
ylim([0 1])
ylabel('Cumulative Distribution (CDF)');
xlabel('SubFlows Size (Bytes)');