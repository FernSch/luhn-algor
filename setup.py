from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Verify credit card information with luhn algorithm.\n'
LONG_DESCRIPTION = 'A package to verify credit card information with luhn algorithm.\n'

# Setting up
setup(
    name="luhn-algor",
    version=VERSION,
    author="Fern S",
    author_email="<fernschoenberg@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'luhn', 'credit card'],
    classifiers=[
        "Development Status :: Done",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)