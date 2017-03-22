sample_image_folder = fullfile(matlabroot,'toolbox/images/imdata');

[filename,user_canceled] = imgetfile();

I = imread(filename);

x = input('enter earth x coordinate');
y = input('enter earth y coordinate');

defaultx = 2800;
defaulty = 3872;

image(I);

hold on;

plot (x,y,'g.','MarkerSize',10);


