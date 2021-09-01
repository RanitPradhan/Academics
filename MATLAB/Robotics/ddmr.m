clear
clc

 

wheelR = 0.0520;
ticksPerRot = 627.2;
l=0.28;
w= 3.14;
dt = 0.01;
x = 1 ;%input("enter x : ");
y = 1 ;%input("enter y : ");
theta=deg2rad(30);

 


t = linspace(0,0.01,100);

 


leftEncoderCount = 1*t;
rightEncoderCount = 1*t;

 


leftWheelTravel= leftEncoderCount*(2*pi*wheelR*ticksPerRot);
rightWheelTravel= rightEncoderCount*(2*pi*wheelR*ticksPerRot);

 

 

distTraveled = 0.5*(leftWheelTravel+rightWheelTravel);
%plot(distTraveled)
x=[1];
y=[1];

 

 

for i = 1:length(distTraveled)

 

if distTraveled(i) <2
v=1;
else
v=0;
end
V(i) = v;
vl(i)=(v-(w*l/2))/wheelR;
vr(i)=(v+(w*l/2))/wheelR;
r(i) = (l/2)*((vr(i)+vl(i))/(vr(i)-vl(i)));
icx(i) = x(i)-r(i)*sin(theta);
icy(i) = y(i)+r(i)*cos(theta);
xn(i) = (cos(w*dt)*(x(i)-icx(i)))+(-sin(w*dt)*(y(i)-icy(i)))+icx(i);
yn(i)= (sin(w*dt)*(x(i)-icx(i)))+(cos(w*dt)*(y(i)-icy(i)))+icy(i);
thetan(i)=theta+w*dt;
theta=thetan(i);
x(i+1)=xn(i);
y(i+1)=yn(i);

 


plot(xn(i),yn(i),'b*')
axis([0 2 0 2])
hold on
pause(0.1)
end

 

% 
% subplot(2,2,1)
% plot(V)
% subplot(2,2,2)
% plot(xn,yn)
% xlabel("xn");
% ylabel("yn");