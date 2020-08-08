import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arena-engine",
    version="0.0.1",
    author="lladdy",
    author_email="me@lladdy.com",
    description="An Arena Engine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lladdy/arena-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)