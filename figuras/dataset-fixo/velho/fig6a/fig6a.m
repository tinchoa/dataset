figure
durationAttack = csvread('fig6a-saidapacektNumberAttackFornew.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig6a-saidapacektNumberNormalFornew.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 100])
ylabel('Cumulative Distribution (CDF)');
xlabel('Packets Number');
