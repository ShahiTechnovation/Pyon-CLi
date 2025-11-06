#!/usr/bin/env python3
"""Setup script for Pyon CLI tool."""

from setuptools import setup, find_packages

setup(
    name="pyon-cli",
    version="1.0.0",
    description="Python CLI tool for deploying smart contracts to Polygon",
    author="Pyon CLI Team",
    author_email="team@pyoncli.dev",
    url="https://github.com/ShahiTechnovation/pyvax-cli",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "web3>=6.0.0",
        "py-solc-x>=2.0.0",
        "eth-account>=0.9.0",
        "cryptography>=41.0.0",
        "requests>=2.31.0",
    ],
    entry_points={
        "console_scripts": [
            "pyon-cli=pyon_cli.cli:app",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software Distribution",
    ],
)
