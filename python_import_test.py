#!/usr/bin/python

import sys, os, datetime, datetime, re, json
import random, time, getopt, struct
import glob
from socket import *
import numpy

# This lib does not work on windows
#import fcntl

import sqlalchemy 

# from NetCDF4 import Dataset

# Not on windows 
import smtplib
from email.MIMEMultipart import MIMEMultipart
import urllib2, cookielib, platform
# md5 has been deprecated
import hashlib

# May or may not have Mysql - comment out
#import MySQLdb

# Import Bottle lib
import bottle

# Web service calls
import web

# FTP
from ftplib import FTP
