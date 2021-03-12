function [t,step] = unitstepshifted(t0)
%generating a shifted unit step signal
t=-10:0.01:10;
step=t>=t0;

end