function [T] = colonize(tI, bI, cM, pM, P) 

%  P is the planetary matrix
%  tI = target planet index
%  bI = base planet index
%  cM = colonization method

%  pM = propulsion method

% calculate payload weight

switch cM
    case 0            %normal human reproduction
        pW = 1200000*3 + (200*70);  %shuttle payload x population + 200kg for matter/energy 
    case 1            %embroyonic
        pW = 1200000*3;  %frozen embryos = no extra energy needed
    case 2            %robotic
        pW = 500000 + (900 * 75);
    otherwise
        pW = 500000;
end



if (tI == 1) 
    T = 0;          % earth is already colonized!!
else
    d = distanceFrom(tI, bI, P);
    T = propulsionTime(d, pM, pW) + colonizeTime(tI, cM, P);
end
    

T= -1;
