figure
durationAttack = csvread('fig8b-saidaSubFlowBytesAttackDown-new.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig8b-saidaSubFlowBytesNormalDown-new.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 1000])
ylim([0 1])
ylabel('Cumulative Distribution (CDF)');
xlabel('SubFlows Size (Bytes)');