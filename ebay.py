#!/usr/bin/python

from htmlparser import between

html = open("won.html").read()

# page 1
won_div = between(html, '<div id="ItemDisplayContainer_WonNext">', 'function')

#won = []
#while items:
item = between(won_div, '<div id="itIn">', '</span>')
title = between(item, 'title="', '"')
print 'title: %s' % title
itemid = between(item, '"> (', ')')
print 'itemid: %s' % itemid

#    append item...
#itemid = won[0].itemid

html = open(itemid+".html").read()
transid = between(html, 'transid=', '&')
print 'transid: %s' % transid
