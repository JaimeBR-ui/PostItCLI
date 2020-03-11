import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postIt-JaimeBR-ui",
    version="0.0.1",
    author="Jaime Bohorquez",
    author_email="",
    description="Post it CLI package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JaimeBR-ui/PostItCLI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
