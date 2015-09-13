from cx_Freeze import setup, Executable
import os, site, sys

site_dir = site.getsitepackages()[1]
include_dll_path = os.path.join(site_dir, "gnome")

missing_dll = ['libgtk-3-0.dll',
           'libgdk-3-0.dll',
           'libatk-1.0-0.dll',
           'libcairo-gobject-2.dll',
           'libgdk_pixbuf-2.0-0.dll',
           'libpango-1.0-0.dll',
           'libpangocairo-1.0-0.dll',
           'libpangoft2-1.0-0.dll',
           'libpangowin32-1.0-0.dll',
           'libffi-6.dll',
           'libfontconfig-1.dll',
           'libfreetype-6.dll',
           'libgio-2.0-0.dll',
           'libglib-2.0-0.dll',
           'libgmodule-2.0-0.dll',
           'libgobject-2.0-0.dll',
           'libpng16-16.dll',
          ]

gtk_libs = ['etc', 'lib', 'share']

include_files = []
for dll in missing_dll:
    include_files.append((os.path.join(include_dll_path, dll), dll))

for lib in gtk_libs:
    include_files.append((os.path.join(include_dll_path, lib), lib))

base = None

# Hide console window
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable("hello.py",
               base=base
    )
]

buildOptions = dict(
    compressed = False,
    includes = ["gi"],
    packages = ["gi"],
    include_files = include_files
    )

setup(
    name = "minimal GTK+ version 3 and Python 2.7 application",
    author = "Andrew Ziem",
    version = "1.0",
    description = "an exercise",
    options = dict(build_exe = buildOptions),
    executables = executables
)
