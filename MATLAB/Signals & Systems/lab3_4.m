n=-10:10;
y=zeros(length(n));
j=1;
for i=-10:10
    y(j)=cos(5*pi*i)-sin(5*pi*i);
    j=j+1;
end
stem(n,y)
xlabel('time')
ylabel('Y(t)')
