figure
formatSpec = '%s%f%f%f%f%[^\n\r]';
delimiter = ',';

fileID = fopen('porcentage.csv','r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter,  'ReturnOnError', false);
fclose(fileID);

day = dataArray{:, 1};
day=['16/2';'17/2';'18/2';'19/2';'20/2';'21/2';'24/2';'25/2';'26/2';'27/2';'28/2';'01/3';'02/3';'03/3'];
totalFlows = dataArray{:, 2};
ataques = dataArray{:, 3};
normal = dataArray{:, 4};
porcentageAttacks = dataArray{:, 5};
%bar(porcentageAttacks)
bar([ataques  normal totalFlows],'stack')
set(gca,'xticklabel',day)
%ylabel('Percentage of Threats');
ylabel('Number of Flows');
legend('Alerts', 'Normal Traffic', 'Total Flows')
%ylim([0 40])
xtickangle(45)
