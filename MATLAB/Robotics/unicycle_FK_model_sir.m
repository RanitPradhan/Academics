% Differential Drive robot Forward Kinematics Model - Unicycle
clear
clc
close all
global dt;  % in seconds
global l;  % in meters
global x0 y0 theta0;   % in meters and radians

dt = 0.01;
l = 0.15;
x0 = 0;
y0 = 0;
theta0 =0;

% Robot Control inputs
vr = [5*ones(1,100),5*ones(1,100)]; %linspace(0,100,100);
vl = [4.5*ones(1,100),5*ones(1,100)]; %linspace(0,1,100);
close all

% Model input parameters
v = (vr+vl)/2;
w = (vr-vl)/l;

% loop of simulation
for i = 1:length(vr)
    try
        [xd,yd,thetad] = robot(v(i),w(i));
        if isnan(xd)
            warning('could not compute bot position')
        end
        subplot(2,1,1)
        title('X,Y position of bot')
        plot(xd,yd,'b*')
        axis([-5 5 -5 5])
        hold on
        grid on
        subplot(2,1,2)
        plot(i,thetad,'r*')
        title('theta')
        hold on
        grid on
    catch 
        warning('error in the program')
    end
   
   
   pause(0.1)
   
end

% Unicycle Forward Kinematics models

function [xd,yd,thetad] = robot(v,w)
global x0 y0 theta0 dt;

xd = x0 + v*cos(theta0)*dt;
yd = y0 + v*sin(theta0)*dt;
thetad = theta0 + w*dt;

x0 = xd;
y0 = yd;
theta0 = thetad;
end
