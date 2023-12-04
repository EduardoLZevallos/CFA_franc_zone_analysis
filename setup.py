from setuptools import setup, find_packages

setup(
    name='cfa_analysis',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    package_data={
        '': ['*.py']
    },
    install_requires=[
        "bokeh",
        "jupyter_ai",
        "numpy",
        "pandas",
        "polars",
        "requests",
        "statistics"
    ],
)