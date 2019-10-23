from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='rocket',
    version='0.0.2',
    author='Breitburg',
    include_package_data=True,
    url='https://github.com/breitburg/rocket',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=open(str(Path(__file__).resolve().parent.joinpath('requirements.txt')), 'r').read().split('\n')
)
