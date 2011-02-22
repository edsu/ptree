from setuptools import setup

description = \
"""
ptree is a minimal implementation of PairTree, which is a filesystem
convention from the digital preservation community for mapping
identifiers to file system locations, and vice versa.

See https://confluence.ucop.edu/display/Curation/PairTree for more details.
"""

setup(
    name = 'ptree',
    version = '0.1',
    url = 'http://github.com/edsu/ptree',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    py_modules = ['ptree',],
    scripts = ['ptree.py'],
    description = description,
    platforms = ['POSIX'],
    test_suite = 'test',
    classifiers = [
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Topic :: Communications :: File Sharing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Filesystems',
    ],
)
