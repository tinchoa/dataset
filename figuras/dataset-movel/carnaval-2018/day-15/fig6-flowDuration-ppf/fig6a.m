figure
durationAttack = csvread('saidapacektNumberAttackFor.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('saidapacektNumberNormalFor.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 100])
ylabel('Cumulative Distribution (CDF)');
xlabel('Packets Number');
