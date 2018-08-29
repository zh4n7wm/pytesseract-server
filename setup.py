import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytesseract-server",
    version="0.0.1",
    author="ox0spy",
    author_email="ox0spy@gmail.com",
    description=" rest api with pytesseract",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ox0spy/pytesseract-server",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
