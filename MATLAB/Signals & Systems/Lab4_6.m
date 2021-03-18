%Ranit
t=0:0.01:2;
sig=ones(size(t));
j=1;
for i=0:0.01:2
    if (i>=1)
        sig(j)=-1
    end
    j=j+1;
end
t2=t+3;
plot(t2,sig);
ylim([-2 2]);