from setuptools import setup,find_packages

requires = (
        'Flask',
        )

setup(
    name='pocketRocket',
    version='1.0',
    author='Carlos Tezna, Nicolas Gonzalez, Andres Pulgarin, Camilo Naranjo',
    author_email='cteznas@eafit.edu.co',
    description='Webapp for Numerical Analysis',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)