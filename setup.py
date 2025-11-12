from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """
    Reads the requirements.txt file and returns a list of requirements.
    """
    requirement_list : List[str]= []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")
    
    return requirement_list
print(get_requirements())
setup(
    name='AI_Trip_Planner',
    version='0.0.1',
    author='Utkarsh Patidar',
    author_email='utkarshpatidfar170@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A Flask application for planning trips using AI.',
    license='MIT',  # Add a valid SPDX license expression
    classifiers=[
        "License :: OSI Approved :: MIT License",  # Update license classifier
    ]
)