%Ranit
t=-5:0.01:5;
y=sin(t);
plot(t,y,'-.')
hold on
y2=sin(2*t);
plot(t,y2,'g--')
hold on
y3=sin(5*t);
plot(t,y3,'r:')