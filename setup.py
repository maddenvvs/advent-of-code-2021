from setuptools import setup, find_packages

setup(
    name="aoc2021",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points="""
        [console_scripts]
        aoc2021=aoc2021.main:cli
    """,
)
