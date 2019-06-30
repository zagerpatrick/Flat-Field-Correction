# Set working directory
%cd "Data_Folder"

# Import packages and modules
import random
import re
import glob
import math
import numpy as np
import scipy as sp
import skimage
import matplotlib.pyplot as plt

from tqdm import tqdm
from math import sqrt
from numpy import (mean, float_, dot, interp, uint8, uint16,
                   uint64, log10, any as np_any, all as np_all)
from skimage import io
from skimage import filters
from skimage import img_as_ubyte
from skimage.filters import gaussian

from matplotlib import colors as c
import matplotlib.gridspec as gridspec

def imread_rgb(f):
    '''
    Function used to read in rgb images properly through
    skimage ImageCollection.
    '''
    return skimage.io.imread(f)
