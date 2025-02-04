import pandas as pd

from fastapi import FastAPI

#create API Object
app = FastAPI()

#read data
data = pd.read_csv('data.csv')

# coba root home API (get)
@app.get("/")
def root():
    return {'message':'My first API !'} 

# endpoint sapaan
@app.get("/name./{name}")
def greet(name):
    return {'message': f'Hai{name}, how are you?'}

#endpoint return data 
@app.get("/data")
def get_data():
    return data.to_dict(orient='records')


#get data by id 
@app.get("/data/{id}")
def search_data(id:int):
    result = data[data['id']==id]
    return {'result': result.to_dict(orient='records')}

#http://127.0.0.1:8000/data/3

#nambah data 
#@app.post("/data{data}")
#def add_data(new_data:dict):
 #   new_data = new.data.split ('-')
  #  new_row = data {'id': new_data [0],
#                    'nama': new_data[1],
 #                   'age': new_data[2],
#                    'job': new_data[3]
 #                   }
   
  #  new_row = pd.DataFrame(new_data)
   # data = pd.concat([data, new_row], ignore_index=True)

    #return {'message':'data is update !'}