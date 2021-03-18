%Ranit
n=-2:6;
x1=[0 0 1 2 3 0 0 2 1];
x2=[-2 -1 1 2 0 0 0 -2 0];
y1=x1+x2
y2=2*x1
i=1;
while (i<10)
    y3(i)=x1(i)*x2(i);
    i=i+1;
end
y3
y4=x1-x2