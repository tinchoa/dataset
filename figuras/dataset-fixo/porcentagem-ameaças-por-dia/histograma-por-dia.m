
%no matlab
figure
formatSpec = '%s%f%f%f%f%[^\n\r]';
delimiter = ',';

fileID = fopen('porcentages.csv','r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
fclose(fileID);

day = dataArray{:, 1};
day=['Day 16';'Day 17';'Day 18';'Day 19';'Day 20';'Day 21';'Day 22'];
totalFlows = dataArray{:, 2};
ataques = dataArray{:, 3};
normal = dataArray{:, 4};
porcentageAttacks = dataArray{:, 5};
bar(porcentageAttacks)
set(gca,'xticklabel',day)
ylabel('Percentage of Threats');
ylim([0 40])



