import sys
sys.path.append('..')
from SETTINGS import *;
tag = 4;
fcn_img_size=256;
net_version = 1;
heart_delta_multiplier = 1.5; 
para_ss = 50;
do_cv = False;
num_epochs = 300;

shift = 10;
rotation = 25;
scale = 0.10;

no_contour_type = 'L';#other versions worse, so it's fixed to 'L'
