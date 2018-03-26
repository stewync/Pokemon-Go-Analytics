# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 18:07:58 2017

@author: hi
"""
import os
import requests
from bs4 import BeautifulSoup
import urllib
import glob

string1 = "ios"
string2 = "android"

path = "C:\Castern\Semester 02\Data Science\Project 02\pokemon_data\data"

android_files = []
ios_files = []

for filename in os.listdir(path):
    for a in filename[0]:
        subpath = os.path.join(path,filename)
        #print(subpath)
        for each_path in os.listdir(subpath)[2]:
            subsubfile = os.path.join(subpath,each_path)
            #print(subsubfile)
            if each_path.endswith('android.html'):
               #android_files.append(each_path)
               infile = open(subsubfile)
               content = infile.read()
               soup = BeautifulSoup(content, "lxml")
               #print type(soup)
               print soup.prettify()