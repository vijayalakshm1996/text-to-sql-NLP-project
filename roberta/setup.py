from setuptools import setup, find_packages
# updating transformers patch to 4.30.0 due to github dependabot alert
# "Insecure Temporary File in GitHub repository huggingface/transformers 4.29.2 and prior. A fix is available at commit 80ca92470938bbcc348e2d9cf4734c7c25cb1c43 and has been released as part of version 4.30.0."
setup(
    name='RAT-SQL',
    version='1.0',
    description='A relation-aware semantic parsing model from English to SQL',
    packages=find_packages(exclude=["*_test.py", "test_*.py"]),
    package_data={
        '': ['*.asdl'],
    },
    install_requires=[
        'asdl~=0.1.5',
        'astor~=0.7.1',
        'attrs~=18.2.0',
        'babel~=2.7.0',
        'bpemb~=0.2.11',
        'cython~=0.29.1',
        'jsonnetbin',
        'networkx~=2.2',
        'nltk~=3.4',
        'numpy~=1.16',
        'pyrsistent~=0.14.9',
        'pytest~=5.3.2',
        'records~=0.5.3',
        'stanford-corenlp~=3.9.2',
        'tabulate~=0.8.6',
        'tqdm~=4.36.1',
        'transformers~=4.30.0',
    ],
    entry_points={"console_scripts": ["ratsql=run:main"]},
)
