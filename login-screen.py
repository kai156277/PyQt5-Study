#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, time
from optparse import OptionParser
import random, datetime


if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    Joanna = os.path.join(os.environ['HOME'], "Pictures", "Joanna")
    parser = OptionParser()
    parser.add_option("-d", "--dir",
                      type='string', dest="dir",
                      help="背景图片所在目录", default=Joanna)
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose",
                      help="禁止输出图片地址至标准输出", default=True,)
    (options, args) = parser.parse_args()
    if options.verbose:
        print("background:", options.dir)
        print("quiet:", options.verbose)

    for root, dirs, files in os.walk(options.dir, topdown=False):
        img = os.path.join(options.dir, files[random.randint(0, len(files)-1)])

    if options.verbose:
        print("current lock-screen:", img)
    os.system('ln -sf {0} /home/zhao/init.d/login-screen.jpg'.format(img))
