%Ranit
n=-10:1:10;
n0=1;
step=n>=n0;
subplot(3,1,1)
stem(n,step)
x1=[-2 3 0 1 5];
n=0:1:4;
subplot(3,1,2)
stem(-n,x1)