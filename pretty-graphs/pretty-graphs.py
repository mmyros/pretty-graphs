#! /usr/bin/env python
from __future__ import print_function, division, absolute_import, unicode_literals

# Copyright (C) 2021 ''

import random


def say_hello():
    """this is a doc string and will show up in the documentation when
    you run 'make docs'
    """
    greetings = ["hi ho!", "how do you do?", "what a nice day!"]
    print(random.choice(greetings))
