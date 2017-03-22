function [d] = distanceFrom (tI, bI, P) 

fres = 24.038461; % this is the resolution of the file


% calculates distance from base planet to target planet
% P is planetary matrix
% tI is target index
% bI is base index

xT = P(tI, 1);
yT = P(tI, 2);

xB = P(bI, 1);
yB = P(bI, 2);

xT = xT * fres;     
yT = yT * fres;     
xB = xB * fres;     
yB = yB * fres;     

d = sqrt((xT-xB)^2 + (yT-yB)^2);


