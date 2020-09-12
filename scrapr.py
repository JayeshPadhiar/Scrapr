from __future__ import unicode_literals

import bs4
import argparse
import youtube_dl as ydl

import engine

scrapr = engine.Engine()

x = input('scrapr > ').split()

scrapr.handle(x[0], *x[1:])