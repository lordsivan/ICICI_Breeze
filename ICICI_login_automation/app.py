# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import csv,datetime
import webbrowser
from threading import Timer

# Step-1 Register your app at
# https://api.icicidirect.com/apiuser/home

# Step-2
# 1. Use http://127.0.0.1:5000/icici/<username>/saveIciciSession
# 2. make sure to port number is correct
# 3. change username in above url


# Step-3 update the following
api_key="XXXXXXXXXXX"
User_name='YYYYY'


ret={
     'loginUrl': '',
     'userName':User_name,
     'table':[]
     }
 
ret['loginUrl']='https://api.icicidirect.com/apiuser/login?api_key='+api_key
 
app = Flask(__name__)

def open_browser():
      webbrowser.open_new("http://127.0.0.1:5000")
      
@app.route('/', methods=['GET'])
def homepage(): 
    
    #args = request.args
   
    
    import csv
    rows = []
    try:
        with open("icici_apiSession.csv", 'r') as file:
            csvreader = csv.reader(file)            
            for row in csvreader:
                rows.append(row)
    except:
        pass
    ret['table'] = rows
    
    return render_template('index.html', values=ret)



@app.route('/icici/<path:path>/saveIciciSession', methods=['GET',"POST"])
def saveIciciSession(path): 
     
    args = request.args
    
    apisession=args.get("apisession", default="", type=str)
    userid=path
    header=['username','api session','Session fetch date']
    row=[userid,apisession,str(datetime.datetime.now())]
    ret['table']= [header, [userid,apisession,str(datetime.datetime.now())]]
    
    f = open('icici_apiSession.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(row)
    f.close()

    return render_template('index.html', values=ret)


if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)

