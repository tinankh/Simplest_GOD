#!/usr/bin/env python3

#   SGOD - Simplest JPEG Grid Origin Detector
#   Copyright (c) 2019 Tina Nikoukhah <tina.nikoukhah@gmail.com>
#                      Jérémy Anger <angerj.dev@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.

import io
import numpy as np
from PIL import Image


def get_jpeg_size(img, x, y):
    width, height = img.size
    width = (width // 8) * 8 - 8
    height = (height // 8) * 8 - 8
    crop_image = img.crop((x, y, width + x, height + y))
    buffer = io.BytesIO()
    crop_image.save(buffer, format='JPEG', quality=100)
    return len(buffer.getvalue())

def detect_jpeg_grid(img, *, fast=False):
    img = img.convert('YCbCr').split()[0]
    get_size = lambda i, j: get_jpeg_size(img, i, j)

    if not fast:
        kappa = 7.0
        coords = [(i,j) for i in range(8) for j in range(8)]
        result = [get_size(i, j) for i, j in coords]

        sorted_result = np.sort(result)
        mean = np.mean(sorted_result[16:])
        std = np.std(sorted_result[16:])

        mini = sorted_result[0]

    else:
        kappa = 7.0
        coords = [(i,i) for i in range(8)]
        result = [get_size(i, j) for i,j in coords]

        sorted_result = np.sort(result)
        mean = np.mean(sorted_result[2:])
        std = np.std(sorted_result[2:])

        i1 = np.where(result == sorted_result[0])[0][0]
        i2 = np.where(result == sorted_result[1])[0][0]
        mini = np.min([sorted_result[0], get_size(i1,i2), get_size(i2,i1)])

        for i in [(i1,i2), (i2,i1)]:
            coords.append(i)
            result.append(get_size(*i))

    if mini < (mean - kappa*std) :
        xx, yy = coords[np.argmin(result)]
        return xx,yy

    else:
        print("no grid found")
        return -1,-1

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename", help="path to the input image")
    parser.add_argument("--fast", action='store_true')
    args = parser.parse_args()

    img = Image.open(args.input_filename)
    x, y = detect_jpeg_grid(img, fast=args.fast)
    print(x, y)
