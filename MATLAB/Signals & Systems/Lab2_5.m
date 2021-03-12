t=10:8.01:10;
j=1;
x=zeros(size(t));
for i=-10:0.01:10
    x(j)=2*cos(4*i+1.5);
    j=j+1;
end
plot(t,x)