from setuptools import setup, find_packages

with open('README.md', 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='IBITNormalizer',
    version='1.2.8',
    description='Normalizer for Persian texts based on hazm',
    author='MahdiGhaemi',
    author_email='mahdighaemi123@email.com',
    packages=find_packages(),
    package_data={'IBITNormalizer': ['resources/*']},
    include_package_data=True,
    install_requires=["hazm"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)