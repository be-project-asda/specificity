import os
from os import path
from os import listdir
from os.path import isfile, join
import re
import sys
import skimage
import scipy
from skimage import io
from scipy import io

from decaf.scripts.imagenet import DecafNet

#jpg_filter=re.compile('^.*\.jpg$');
#onlyfiles = [ f for f in listdir(mypath) if py_filter.match(f) ];


print sys.argv 


net = DecafNet('../imagenet_pretrained/imagenet.decafnet.epoch90', '../imagenet_pretrained/imagenet.decafnet.meta');

mypath=sys.argv[1];
savepath=sys.argv[2];
jpg_files=listdir(mypath);


for index,imname in enumerate(jpg_files):
	savefname=savepath+'/'+imname+'_decaf.mat';
	if not os.path.exists(savefname):
		print imname;
		im=skimage.io.imread(mypath+'/'+imname,False,'pil');
		scores= net.classify(im, center_only=True);
	#	pool5 = net.feature('pool5_cudanet_out');
		fc6 = net.feature('fc6_cudanet_out');
		fc6n = net.feature('fc6_neuron_cudanet_out');
		fc7 = net.feature('fc7_cudanet_out');
		fc7n = net.feature('fc7_neuron_cudanet_out');
		scipy.io.savemat(savefname,mdict={'fc6':fc6,'fc7':fc7,'fc7n':fc7n,'fc6n':fc6n});


