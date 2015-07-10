import os
from setuptools import setup
from djangocms_livedraftswitch import VERSION

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst', 'md')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


def read_file(name):
    return open(os.path.join(os.path.dirname(__file__), 
                             name)).read()    

readme = read_file('README.md')
changes = read_file('CHANGES.md')

setup(
    name='djangocms-livedraftswitch',
    version=VERSION,
    description='Returns classic DjangoCMS-style live-draft switch to DjangoCMS',
    long_description=read_md('\n\n'.join([readme, changes])),
    author='Fran Hrzenjak',
    author_email='fran.hrzenjak@gmail.com',
    license="The Unlicense",
    platforms=["any"],
    url='https://github.com/frnhr/djangocms-livedraftswitch/',
    packages=[
        'djangocms_livedraftswitch',
    ],
    include_package_data=True,  # use MANIFEST.in during install
    classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: Public Domain',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities',
    ],
)
