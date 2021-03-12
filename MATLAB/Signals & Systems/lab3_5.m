t= 0:19;
x=zeros(size(t));
j=1;
d=0;
for i=0:19
if i>=0 && d<4
x(j)=d+1;
end
j=j+1;
d=d+1;
if d==4
d=0;
end
end
stem(t,x)
xlabel("Time(sec)");
ylabel("X(t)");
