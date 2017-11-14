#!/usr/bin/env python3
#-*-coding:utf-8-*-
# __datetime__
# __purpose__

"""run this project"""
from mcs import app
import config


class Run_App:
    def __init__(self):
        self.app = app.Init_app().create_app()
        self.app.config.from_object(config.DevConfig)
    def normal_run(self):
        self.app.run()
if __name__ == "__main__":
    Run_App().normal_run()