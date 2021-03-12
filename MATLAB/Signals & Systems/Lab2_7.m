t=10:8.01:10;
j=1;
x=zeros(size(t));
y=10*sin(2*pi*20*t).*exp(-10*t);

plot(t,y)
xlabel( 'time')
hold
ylabel("Y(t)")

y_2=10*sin(2*pi*20*t).exp(-5*t)
plot(t,y_2)