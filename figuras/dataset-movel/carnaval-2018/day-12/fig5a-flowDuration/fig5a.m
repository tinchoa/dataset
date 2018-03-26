figure
durationAttack = csvread('saidadurationAttack.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('saidadurationNormal.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
ylabel('Cumulative Distribution (CDF)');
xlabel('Flow Duration (ms)');