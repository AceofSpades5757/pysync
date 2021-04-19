""" Basic setup.py using setuptools.

Classifiers
-----------
[Dynamic List of Classifiers](https://pypi.org/classifiers/)
"""
import setuptools


with open("README.md", "r") as fin:
    long_description = fin.read()
with open("LICENSE", "r") as fin:
    license = fin.read()

setuptools.setup(
    name='pysync',
    version='0.0.5',
    install_requires=[
        'typer',
    ],
    author='Kyle L. Davis',
    author_email='AceofSpades5757.github@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=license,
    python_requires='>=3.6',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        pysync=pysync.main:cli
    ''',
)
