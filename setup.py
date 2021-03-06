from setuptools import setup, find_packages
from fluent import __version__

setup(
    name='libfluent',
    version=__version__,
    author='Breitburg',
    include_package_data=True,
    url='https://github.com/breitburg/fluent',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'pysdl2', 'reloadr==0.3.3'
    ],
    package_data={
        'fluent': ['assets/*']
    }
)
