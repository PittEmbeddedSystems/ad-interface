#!/usr/bin/env python3

from distutils.core import setup

setup(name='ad-interface',
      version='0.2',
      description='library for reading A/D outputs',
      py_modules=['ad_interface', 'ad_mcp', 'ad_fake']
    )
