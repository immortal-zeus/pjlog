from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name = 'pjlog',
    version = '0.1.9',
    description = 'Simple library for Logarithm with useful functions.',
    py_modules = ["pjlog"],
    package_dir = {'': 'src'},
    classifiers = [
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "License :: Free For Educational Use",

    ],
    long_description = long_description,
    long_description_content_type = "text/markdown",
    install_requires = [
    ],
    extras_require = {
        "dev":[],
    },

    url = "https://github.com/immortal-zeus/pjlog",
    author = "Parsh Jain",
    author_email = "laspparshinc@gmail.com",
)

