function [T] = propulsionTime(d, pM, pW) 

lightspeed = 299792458;         % in m/s
lightyear = 9.4610e+15;

%d = d *lightyear;

pF = 0.01*pW; %payload fraction, usually <1% of spacecraft mass
fM = 1000 * pF * 1.008 * 0.119;   %assume hydrogen fuel, 100% conversion rate x mass percent of hydrogen in h20

eM = fM * 286000; %assume complete combustion


fissionE = pF * (lightspeed^2) * 0.001;     % 0.1% mass energy conversion

fusionE = 10 * pF * (lightspeed^2) * 0.009;     % 0.9% mass energy conversion, payload fraction increased

warp10 = 9166 * lightspeed;


switch pM
    case 1    %conventional rockets
        rawTime = (d*lightyear)/70220;     %this is the speed of the fastest spacecraft made in m/s
        T = rawTime + ((pW*70220)/eM);
        T = T * 2; %half time accelerating, half decelerating
    case 2    %ion pulse
        rawTime = (d*lightyear)/90000;
        T = rawTime + 83314.4;
        T = T *2;
    case 3    %nuclear fission fragment
        rawTime = (d*lightyear) /(lightspeed * 0.01);  %assume maximum theoretical speed of 1% c
        T = rawTime + (pW*lightspeed * 0.01)/fissionE;
        T = T * 2;
    case 4 % nuclear fusion
        rawTime = (d*lightyear) / (lightspeed * 0.05); %assume maximum theoretical speed of 5% c
         T = rawTime + (pW*lightspeed * 0.01)/fusionE;
         T = T * 2;
    case 5 % reactionless beamed
        rawTime = (d*lightyear) / 3.1854e+07;        %hypothetical beam sail max speed adjusted for deceleration
        T = rawTime;
    case 6 %star trek
        T = (d*lightyear) / warp10;
    otherwise
        T = -999;
end

T = T /(60*60*24*365);          % time in years
        
         