import functools

import asyncio

class Scheduler():
    def __init__(self,loop):
        self.loop=loop

    def schedule(self,func, args=None, kwargs=None, interval=60):
        pass
