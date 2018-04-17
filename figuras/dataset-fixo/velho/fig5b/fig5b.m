figure
protoAttack = csvread('fig5b-saidaprotoAttacknew.csv');
protoNormal = csvread('fig5b-saidaprotoNormalnew.csv');
values=[protoNormal(1,2),protoAttack(1,2);protoNormal(2,2),protoAttack(2,2)];
x=bar(values);
set(gca,'xticklabel',{'TCP';'UDP'})
ylabel('Number of Flows');
hatchfill2(x(1),'cross','HatchAngle',45);
hatchfill2(x(2),'single','HatchAngle',0);