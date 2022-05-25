import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="orquesta-engine",                        # This is the name of the package
    version="1.0.0a1",                        # The initial release version
    author="Orquesta",                     # Full name of the author
    description="Orquesta Python SDK",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries"
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=2.7',                # Minimum version requirement of the package
    py_modules=["orquesta"],             # Name of the python package
    package_dir={'':'orquesta/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)