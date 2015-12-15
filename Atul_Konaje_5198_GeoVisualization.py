__author__ = 'Atul'

#Name Atul Konaje (Atul.Konaje@mavs.uta.edu)
#UTA ID 1001145198
#Course CSE6331 (2155-CSE-6331-004-ADV-TOPICS-IN-DATABASE-SYSTEMS--2015-Summer)
# import the Bottle framework
from bottle import static_file
from bottle import route, template, request,run
import json
import csv
import json

#Handle the inital request
@route('/',method="GET")
def welcome():

    output = static_file('default.html',root="views/")
    return output

#To recieve the csv file dropped
@route('/csvdata',method="POST")
def send():

     fileopen=request.files['file'].file
     #fname=request.files['file'].filename
     reader = csv.reader(fileopen)
     line=reader.next()
     fieldnames=line
     print fieldnames
     data_dict = csv.DictReader(fileopen,fieldnames)
     final_value=[]
     final_value.append(['Lat', 'Long', 'Name','mag'])
     i=0
     for row in data_dict:
       i=i+1
       if(row['latitude']=="FALSE" or row['longitude']=="FALSE"):
           continue
       final_value.append([float(row['latitude']),float(row['longitude']),"Place:"+row['place']+"  Time: "+row['time'],float(row['mag'])])
       #if i==10:
           #break
     #print final_value   
     return json.dumps(final_value)


@route('/geochart',"POST")

def processrequest():
    print "proccessing"

run(host='0.0.0.0', port=8080, debug=True)
