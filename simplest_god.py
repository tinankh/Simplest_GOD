#

#   SGOD - Simplest JPEG Grid Origin Detector
#   Copyright (c) 2019 Tina Nikoukhah <tina.nikoukhah@gmail.com>

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.

#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.

#

import argparse
import os
from PIL import Image
import numpy as np

# Parse program arguments
parser = argparse.ArgumentParser()

parser.add_argument("input_filename", help="path to the input image")
args = parser.parse_args()

img = Image.open(args.input_filename)
width, height = img.size

width = int(width/8) * 8 - 8
height = int(height/8) * 8 - 8

ycbcr = img.convert('YCbCr')
(Y, Cb, Cr) = ycbcr.split()

filename = os.path.splitext(os.path.basename(str(args.input_filename)))[0]

outdir="outdir_temp_"+str(filename)

if not os.path.exists(outdir):
    os.mkdir(outdir)

result = []

for i in range(64):
    x = i%8; y= int(i/8);
    area = (x, y, width+x, height+y)
    crop_image = Y.crop(area)
    file_candidate = outdir + "/crop" + str(x) + "_" + str(y) + ".jpg"
    crop_image.save(file_candidate, quality=100)
    result.append(os.path.getsize(file_candidate))

aligned = np.sort(result)[16:]

mean = np.mean(aligned)
std = np.std(aligned)

gridorigin = np.argmin(result)

if np.min(result) < (mean - 7.0*std) :
    print("grid origin: ({},{})".format(int(np.argmin(result)/8),np.argmin(result)%8))
else:
    print("no grid found")
