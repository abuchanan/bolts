import os
from setuptools import setup, find_packages

_this_dir = os.path.dirname(__file__)
readme_path = os.path.join(_this_dir, 'README.md')
readme = open(readme_path).read()

setup(
    name='',
    description="",
    long_description=readme,
    version='1.0.0',
    author='Alex Buchanan',
    author_email='buchanae@gmail.com',
    packages=find_packages(),
)
