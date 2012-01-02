'''
Created on Jan 2, 2012

@author: bons

'''

#!/usr/bin/python

import sys
import urllib
import time
import os
from datetime import datetime,timedelta


d_format = "%Y/%m/%d"

def retrieveImages( period,hour, path):
    
    thisdate = time.strftime("%Y/%m/%d", period.timetuple())
    url = "http://www.webcam-ski.com/archives/" + thisdate +"/"+ hour + "/lindarets/lindarets_MEGA.jpg"
    name = time.strftime("%Y_%m_%d", period.timetuple())+hour
    print "Got pic: " + name
    urllib.urlretrieve( url, path+name)
  

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    try:
        start_date = datetime.strptime(sys.argv[1], d_format)
        end_date = datetime.strptime(sys.argv[2], d_format) 
    except (TypeError, IndexError):
        sys.stderr.write("Example: lelindagrabber.py 2011/03/25 2011/04/02 \n")
        
    print "Le LindaGrabber Started \n"
    print "retrieving pictures from" + str(start_date) +" to " + str(end_date)
       
    h_list = ["1000","1400","1600"] #daily pic hours list
    path = "./pics/" #The path where you want to store the downloaded images
    day_count = (end_date - start_date).days + 1
    for date in daterange(start_date, end_date):
        for hour in h_list:
            retrieveImages( date, hour, path )
    print "Finished retrieving pics now generating video movie.mp4... \n"
    print "Be patients... it's gonna take some minutes \n"
    os.system('convert -delay 1x2 -limit memory 1024mb -limit map 64mb ./pics/201* movie.mp4')
    print "Jpeg to Mp4 conversion completed...enjoy :P \n"
     
     


