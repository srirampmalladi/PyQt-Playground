#From http://www.py2exe.org/index.cgi/Py2exeAndPyQt

from distutils.core import setup
import py2exe

setup(windows=[{"script" : "../src/main.pyw"}],
      options={"py2exe" : {"includes" : ["sip", "PyQt4.QtNetwork"]}})