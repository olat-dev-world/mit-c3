import Task1_tz_diff
import datetime
from flask import Flask, jsonify, request 

# creating a Flask app 
app = Flask(__name__) 

@app.route('/', methods = ['GET', 'POST']) 
def task_home():
    t_diff = '00:00:00'
    lst_data = [] 

    if(request.method == 'GET'): 
        data = Task1_tz_diff.timeDiff_sec(t_diff)
        lst_data.append(data) 
        return lst_data
    
    if(request.method == 'POST'): 
        req_str = request.get_data().decode('utf-8').strip()  
        req_lines = req_str.split('\\n')
        for x in range(0, len(req_lines), 2):
            data = Task1_tz_diff.timeDiff(str(req_lines[x]), str(req_lines[x+1]) )
            lst_data.append(data)
        return lst_data


if __name__ == '__main__': 
      app.run(debug = True) 
