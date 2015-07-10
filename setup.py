import os
from setuptools import setup

version = '0.2.1'

def read_file(name):
    return open(os.path.join(os.path.dirname(__file__), 
                             name)).read()    

readme = read_file('README.md')
changes = read_file('CHANGES.md')

setup(
    name='djangocms-livedraftswitch',
    version=version,
    description='Returns classic DjangoCMS-style live-draft switch to DjangoCMS',
    long_description='\n\n'.join([readme, changes]),
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
