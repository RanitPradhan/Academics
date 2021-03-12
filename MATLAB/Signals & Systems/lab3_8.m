       t= -4:4;
   x=[-3 -2 -1 0 1 1 3 2 3];
   j=1;
  for i=-4:4
  	 if i==1
       			x(j)=1;
    		end
    	j=j+1;
end
delta=t==0;
a=x.*delta;
figure(1)
stem(t,a)
%impulse
step=t>0;
b=x.*step;
figure(2)
stem(t,b)
%unit step
ramp=t.*step;
c=x.*ramp;
figure(3)
stem(t,c)
%ramp
