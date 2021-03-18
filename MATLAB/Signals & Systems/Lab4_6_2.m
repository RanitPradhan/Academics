%Ranit
t=0:0.01:2;
sig=ones(size(t));
j=1;
for i=0:0.01:2
    if (i>=1)
        sig(j)=-1;
    end
    j=j+1;
end
t2=t-5;
t2=t2/2;
t2=-1*t2;
plot(t2,sig);
ylim([-2 2]);
xlim([1 3])