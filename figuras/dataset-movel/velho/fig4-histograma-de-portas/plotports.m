clear all
clc
close all

udp = csvread('hist-portas-udp.csv');
tcp = csvread('hist-portas-tcp.csv');
all = csvread('hist-portas-all.csv');


redgreenmap = [0 0.8 0; 1 0 0];

f1 = figure('pos',[100 100 800 250]);
y1 = all([1:1024],[3,4]);
bar(y1,'stacked','barwidth',2)
set(gca,'YScale','log')

colormap(redgreenmap)
xlim([1 1024])
% y = all([1:53 55:123 125:443 445:1024],[5,6])


f2 = figure('pos',[100 400 800 250]);
y2 = all([1:1024],[6,7]);
bar(y2,'stacked','barwidth',2)
set(gca,'YScale','log')
colormap(redgreenmap)
xlim([1 1024])