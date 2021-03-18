%Ranit
t= -10:0.01:10;
impulse=t==2;
subplot(2,1,1);
plot(t,impulse)
ramp=(t>5).*t;
subplot(2,1,2);
plot(t,ramp)