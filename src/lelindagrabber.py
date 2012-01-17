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
    name = thisdate.replace('/', '_')+"_"+hour
    urllib.urlretrieve( url, path+name)
    print "Got pic: " + name
  

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Error: no date argument specified'
        print 'Usage: lelindagrabber.py 2011/12/20 2011/12/23 \n'
        sys.exit(1)
    try:
        start_date = datetime.strptime(sys.argv[1], d_format)
        end_date = datetime.strptime(sys.argv[2], d_format) 
    except (TypeError, IndexError):
        sys.stderr.write("Example: lelindagrabber.py 2011/12/20 2011/12/23 \n")
        sys.exit(1)

        
    print "Le LindaGrabber Started \n"
    print "retrieving pictures from" + str(start_date) +" to " + str(end_date)
       
    h_list = ["1000","1400","1600"] #daily pic hours list
    path = "./pics/" #The path where you want to store the downloaded images
    for date in daterange(start_date, end_date):
        for hour in h_list:
            retrieveImages( date, hour, path )
    print "Finished retrieving pics now generating video movie.mp4... \n"
    print "Be patient... it's gonna take some minutes \n"
    os.system('convert -delay 1x2 -limit memory 1024mb -limit map 64mb ./pics/201* movie.mp4')
    print "Jpeg to Mp4 conversion completed...enjoy :P \n"
     
     


