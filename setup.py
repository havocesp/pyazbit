#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""PyAzBit - A Python AzBit cryptocurrency exchange API wrapper.
 - File: pyazbit/setup.py
 - Author: Havocesp <https://github.com/havocesp/pyazbit>
 - Created: 2023-10-23
"""

from pathlib import Path

from setuptools import find_packages, setup

requirements = Path(__file__).with_name('requirements.txt').read_text().splitlines()

setup(
    name='pyazbit',
    version='0.1.0',
    packages=find_packages(exclude=['.idea*', 'build*', '*.vs', '*.vscode', '*.code', '*.atom', '*.mypy_cache', '*.egg-info', 'dist*', 'venv*', '*__pycache__*', '*.tox*']),
    url='https://github.com/havocesp/pyazbit',
    license='MIT',
    author='havocesp',
    requires=requirements,
    author_email='10012416+havocesp@users.noreply.github.com',
    description='AzBit cryptocurrency exchange API wrapper.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)
