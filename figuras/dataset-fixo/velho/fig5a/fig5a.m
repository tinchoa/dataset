figure
durationAttack = csvread('fig5a-saidadurationAttacknew.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig5a-saidadurationNormalnew.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
ylabel('Cumulative Distribution (CDF)');
xlabel('Flow Duration (ms)');