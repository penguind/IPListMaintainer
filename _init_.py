#! /bin/python2.7
# -*- coding:utf-8 -*-

'''
This program is for local network, used as automaticly maintaining the IP address list when IPs of some node changed.
It would be helped when there are many PCs configrated by DHCP running in a local network, or PCs are distanced from the administrator.IP address list will reflashed automaticly.
Two actors are defined in this program, Controller and Finder.
Controller is for working as a server to be connected by Finder.As most time, Controller has a fixed IP address, so a Finder would connect Controller and report its current IP address.When some Finder changed its IP address, Controller get new one and reflash the IP list in order that administrator could find the current IP of every Finder. 
Finder is designed for the PC which is monitored.Finder report its current IP to Controller within a fixed timeout with a particular key which is as a mark.
Good luck when you maintain your local network:)
'''