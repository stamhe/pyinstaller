#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#Tested on Windows 7 64bit with python 2.7.6 and PsychoPy 1.81.03

from PyInstaller.hooks import hookutils
datas = hookutils.collect_data_files('psychopy')
