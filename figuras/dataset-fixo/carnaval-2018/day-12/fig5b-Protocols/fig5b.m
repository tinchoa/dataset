figure
protoAttack = csvread('saidaprotoAttack.csv');
protoNormal = csvread('saidaprotoNormal.csv');
values=[protoNormal(1,2),protoAttack(1,2);protoNormal(2,2),protoAttack(2,2)];
bar(values);
set(gca,'xticklabel',{'TCP';'UDP'})
ylabel('Number of Flows');