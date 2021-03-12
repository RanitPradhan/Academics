t=10:8.01:10;
j=1;
x=zeros(size(t));
for i=-10:0.01:10
    if (i>=-2)&&(i<=0)
        x(j)=i+2;
    elseif (i<=2)&&(i>=0)
        x(j)=2-i;
end
plot(t,x)
xlabel( 'time')
ylabel("Y(t)")