function [T] = colonizeTime (tI, cM, P) 

%P i planetary matrix
%tI is target index
%cM is colonization method

%first check metallicity



m = P(tI, 3);         %metallicity factor

e = P(tI, 4);         %energy output of star

switch cM
    case 0            %normal human reproduction
        T = 70*m*sqrt(e)
    case 1            %embroyonic
        T = 40*m*sqrt(e)
    case 2            %robotic174,000
        T = 20*m*sqrt(e)
    otherwise
        T = -999
end


        