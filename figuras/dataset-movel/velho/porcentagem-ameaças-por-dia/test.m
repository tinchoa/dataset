figure
formatSpec = '%s%f%f%f%f%[^\n\r]';
delimiter = ',';
fileID = fopen('porcentage.csv','r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
fclose(fileID);
day = dataArray{:, 1};
day=['Day 23';'Day 24'];
totalFlows = dataArray{:, 2};
ataques = dataArray{:, 3};
normal = dataArray{:, 4};
porcentageAttacks = dataArray{:, 5};
bar(porcentageAttacks)
set(gca,'xticklabel',day)
ylabel('Percentage of Threats');
ylim([0 10])
