from setuptools import setup, find_packages

setup(
    name='vertexpacking',
    version='0.1',
    packages=find_packages(),
    install_requires=['networkx>=3.3', 'gurobipy>=11.0.2', 'scipy>=1.14.0', 'pandas>=2.2.2', 'openpyxl>=3.1.5'],  
    python_requires='>=3.12.4',
) 