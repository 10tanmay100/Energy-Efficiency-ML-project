from setuptools import setup
from typing import List


def get_requirements_list()->List[str]:
    '''
    This function will going to return a list of strings which will contain name for all the libraries specified with requirements.txt
    '''
    with open("requirements.txt","r") as f:
        return f.readlines().remove("-e .")

setup(
name="energy-efficiency-predictor",
version="0.0.1",
author="Tanmay",
description="This is energy efficiency project for calculating heat temp loader and cool temo loader predictor",
packages=["energy_efficiency"],
install_requires=get_requirements_list()
)