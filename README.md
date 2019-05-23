SGOD - Simplest JPEG Grid Origin Detector
=========================================

JPEG Grid Origin Detection by Simulated Compression

================================================

Version 1 - May 8th, 2019

by Tina Nikoukhah <tina.nikoukhah@gmail.com>

joint work with Rafael Grompone von Gioi, Miguel Colom and Jean-Michel Morel


Introduction
------------

SGOD is an implementation of the Simplest JPEG Grid Origin Detector described in the paper:

     "Détection de grille JPEG par compression simulée" by Tina
     Nikoukhah, Miguel Colom, Jean-Michel Morel and Rafael Grompone
     von Gioi.


Online Demo
------------

[IPOL](https://ipolcore.ipol.im/demo/clientApp/demo.html?id=77777000051)


Running SGOD Command
--------------------
python simplest_god.py <image>

You can remove the output of the algorithm created in outdir_temp_<image> by running
rm -r outdir_temp_*


Copyright and License
---------------------

Copyright (c) 2019 Tina Nikoukhah <tina.nikoukhah@gmail.com>

SGOD is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

SGOD is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.


Thanks
------

I would be grateful to receive any comment, especially about errors,
bugs, or strange results.
