#!/usr/bin/python2

from pycharts2 import Chart

c = Chart()
c.register_interval(0, 0, 5)
c.register_interval(5, 10, 15)
c.register_interval(6, 5, 10)
c.register_interval(10, 20, 25)
c.register_interval(11, 15, 20)
c.register_interval(16, 25, 30)
c.render("1.png")
