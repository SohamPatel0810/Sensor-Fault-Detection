from setuptools import find_packages,setup
from typing import List



def get_requirements()->List[str]:
    """Returns a list of requirements"""
    requirement_list:List[str] = []

    """Get each requirement from requirements.txt"""
    with open('requirements.txt') as f:
        required = f.read().splitlines()
        requirement_list.append(required)

    return requirement_list[0]

setup(
    name='sensor',
    version='0.0.1',
    author='Soham',
    author_email='soham.patel0820@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)