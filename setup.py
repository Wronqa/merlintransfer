from setuptools import setup, find_packages

setup(
    name="merlintransfer",
    version="0.5",
    packages=find_packages(),
    install_requires=[
        "paramiko==2.11.0",
    ],
    include_package_data=True,
    author="Paweł Gawżynski && Jakub Wrona",
    author_email="kuba.wrona@onet.pl",
    description="Simple ssh uploader",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/wronqa/merlintransfer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)