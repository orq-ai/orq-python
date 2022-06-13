import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = None
with open('orquestadev/version.py') as f:
    exec(f.read())

setuptools.setup(
    name="orquesta-dev",
    version=str(__version__),
    author="orquestadev",
    description="Official Orquesta SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages('orquestadev'),
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
    ],
    python_requires='>=2.7',
    py_modules=["orquestadev", "base_client", "utils", "version"],
    package_dir={'': 'orquestadev'},
    install_requires=[
        'requests'
    ]
)
