import Task1_tz_diff
import datetime

from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
import json  


# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST']) 
def task_home():
    t_diff = '01:06:00'
    if(request.method == 'GET'): 
        lst_file = []
        data = Task1_tz_diff.timeDiff_sec(t_diff)
        lst_file.append(data) 
        return lst_file
    
@app.route('/home/<int:num>', methods = ['GET']) 
def display(t_diff): 
  
    data = Task1_tz_diff.timeDiff_sec(t_diff)
    list_diff = jsonify({'data': data})
    return list_diff

if __name__ == '__main__': 
      app.run(debug = True) 
