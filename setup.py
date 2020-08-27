from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name = 'ptree',
    version = '0.3',
    url = 'http://github.com/edsu/ptree',
    author = 'Ed Summers',
    author_email = 'ehs@pobox.com',
    py_modules = ['ptree',],
    scripts = ['ptree.py'],
    description = 'Work with PairTree file system convention',
    long_description=long_description,
    long_description_content_type='text/markdown',
    platforms = ['POSIX'],
    test_suite = 'test',
    classifiers = [
        'License :: Public Domain',
        'Intended Audience :: Developers',
        'Topic :: Communications :: File Sharing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Filesystems',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
