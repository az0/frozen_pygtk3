# Minimal application built with GTK+ version 3 with Python 2.7 for Windows

This was tested on Microsoft Windows 7 64-bit.

## Prerequisites

* https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi
* http://sourceforge.net/projects/pygobjectwin32/files/pygi-aio-3.14.0_rev22-setup.exe/download
* http://sourceforge.net/projects/cx-freeze/files/4.3.3/cx_Freeze-4.3.3.win32-py2.7.msi/download

## Procedure

1. Install the prerequisites
1. Run ``setup.py build``
1. Run ``copy_dlls.bat``
1. Find the application in ``build\exe.win32-2.7```

## Known issues

The frozen application is 93MB and 4660 files, much of which are the locales and icons.

