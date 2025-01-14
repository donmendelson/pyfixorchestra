from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfixorchestra", # Replace with your own username
    version="1.1.0",
    author="Nathanael Judge",
    author_email="nzjudge@mtu.edu",
    description="FIX pyorchestra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FIXTradingCommunity/pyfixorchestra",
    packages=setuptools.find_packages(),
	include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
