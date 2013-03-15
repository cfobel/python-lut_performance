from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext


setup(name = "lut_performance",
    version = "0.0.1",
    description = "Lookup table performance experiment",
    keywords = "lut_performance",
    author = "Christian Fobel",
    url = "https://github.com/cfobel/python-lut_performance",
    license = "GPL",
    long_description = """""",
    cmdclass = {'build_ext': build_ext},
    packages = ['lut_performance'],
    ext_modules = [Extension('lut_performance.cLut_performance',
                             ['src/cLut_performance.pyx'])]
)
