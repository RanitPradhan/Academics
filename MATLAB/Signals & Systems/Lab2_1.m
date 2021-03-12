t=10:8.01:10;
j=1;
x=zeros(size(t));
for i=-10:0.01:10
    if i==0
    x(j)=1;
    end
    j=j+1;
end
plot(t,x)
xlabel( 'time')
ylabel('Y(t)')