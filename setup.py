# import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name="initial",                     # This is the name of the package
#     version="0.2.0",                        # The initial release version
#     author="Ming",                     # Full name of the author
#     description="For testing ws python package.",
#     long_description=long_description,      # Long description read from the the readme file
#     long_description_content_type="text/markdown",
#     packages=setuptools.find_packages(),    # List of all python modules to be installed
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],                                      # Information to filter the project on PyPi website
#     python_requires='>=3.9',                # Minimum version requirement of the package
#     py_modules=["initial"],             # Name of the python package
#     package_dir={'':'initial/src/initial'},     # Directory of the source code of the package
#     install_requires=[]                     # Install other dependencies if any
# )


import sys

if sys.version_info < (2, 6):
    print(sys.stderr, "{}: need Python 2.6 or later.".format(sys.argv[0]))
    print(sys.stderr, "Your Python is {}".format(sys.version))
    sys.exit(1)

from setuptools import setup, find_packages

setup(
    name="initial",
    version="0.2.0",
    license="MIT",
    description="A python library adding a json log formatter",
    package_dir={'': 'src'},
    packages=find_packages("src", exclude="tests"),
    install_requires=["setuptools", "thrift==0.10.0", "requests >= 2.13.0", "urllib3 >= 1.25.3"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'Topic :: System :: Logging',
    ]
)