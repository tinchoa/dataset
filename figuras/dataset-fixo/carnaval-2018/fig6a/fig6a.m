figure
durationAttack = csvread('fig6a-saidapacektNumberAttackFor-new.csv');
[f,x] = ecdf(durationAttack(:,2));
plot(f,'r')
hold on
durationNormal = csvread('fig6a-saidapacektNumberNormalFor-new.csv');
[f,x] = ecdf(durationNormal(:,2));
plot(f,'g')
xlim([0 100])
ylabel('Cumulative Distribution (CDF)');
xlabel('Packets Number');
