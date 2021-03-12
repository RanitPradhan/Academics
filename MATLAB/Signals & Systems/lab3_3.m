n=-10:10;
y=zeros(length(n));
j=1;
for i=-10:10
if(i>=0)
y(j)=i;
end
j=j+1;
end
stem(n,y)
xlabel('time')
ylabel('Y(t)')
