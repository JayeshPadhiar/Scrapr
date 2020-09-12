from __future__ import unicode_literals

import bs4
import argparse
import youtube_dl as ydl


class Engine:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def get(self, *args):

        getparser = self.parser
        getparser.add_argument('-l', '--links', nargs='+', required=True)

        args = getparser.parse_args(args)
        links = args.links

        params = {
            'format': 'bestaudio/best',    
        }

        try:
            with ydl.YoutubeDL(params) as getter:
                getter.download(links)
        except Exception as getex:
            print('Error : ', getex)

    def handle(self, comm, *args):
        self.plex = {
            'get': self.get
        }
        self.plex.get(comm)(*args)