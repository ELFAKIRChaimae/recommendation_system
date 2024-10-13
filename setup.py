from setuptools import setup
with open("README.md" , 'r' ,encoding="utf-8") as fh :
    long_description=fh.read()

SRC_REPO='src'
LIST_OF_RESUIREMENTS=['streamlit']

setup(
src=SRC_REPO,
version='0.0.1',
description='a recommendation systems '

)