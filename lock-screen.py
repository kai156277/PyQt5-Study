#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, time
from optparse import OptionParser
import random, datetime

Joanna = os.path.join(os.environ['HOME'], "Pictures", "Joanna")

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", "--interval",
                      type="int", dest="sec",
                      help="背景图片切换间隔", default=300)
    parser.add_option("-d", "--dir",
                      type='string', dest="dir",
                      help="背景图片所在目录", default=Joanna)
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose",
                      help="禁止输出图片地址至标准输出", default=True,)
    (options, args) = parser.parse_args()
    if options.verbose:
        print("background:", options.dir)
        print("interval:", options.sec)
        print("quiet:", options.verbose)

    while True:
        random.seed(datetime.datetime.now())
        for _, _, files in os.walk(options.dir, topdown=False):
            random.shuffle(files)
            for name in files:
                img = os.path.join(options.dir, name)
                if options.verbose:
                    print("current lock screen:", img)
                os.system('gsettings set org.gnome.desktop.screensaver picture-uri "file:{0}"'.format(img))
                time.sleep(options.sec)
