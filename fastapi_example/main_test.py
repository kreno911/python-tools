# Main tester for fastapi
# Use this just to poke around

'''
To run this:
    > uvicorn main_test:app1 --reload
    # Note name "main_test:app1" -> The proper way to do it (same as main filename)

uvicorn does hot reloads with "--reload", just save your file and it updates.

Note that this is python so matching of paths will go in order they are defined
in ths file. So...
    @app.get("/post/{id}")
    @app.get("/post")
If /post/{id} allows any id type including none, it will always match first one 
and /post will never get called. Restructure or rename. 

FastAPI main files usually site in an "app/" directory. Anytime you have your own package
directory, you would need an empty __init__.py file so python knows about this directory. 
    If you do this, uvicorn would need <dir>.<main-file-name> as reference 

'''

from fastapi import FastAPI
from fastapi.params import Body
from datetime import datetime
from pydantic import BaseModel

# Name here matters for uvicorn command 
app1 = FastAPI()

@app1.get("/")
async def root():
    print("/ called...")
    return { "This is a test FastAPI service" }

@app1.get("/posts")
async def posts():
    print("/posts called...")
    return { "posts": "These are posts" }

@app1.post("/createpost")
async def create_posts():
    '''
    Simple call: curl -XPOST http://127.0.0.1:8000/createpost
    '''
    print("/createpost called...")
    return { "This creates posts" }

@app1.post("/create-posts-a")
async def create_posts_w_body(payload: dict = Body(...)):
    '''
    Simple call: curl -XPOST http://127.0.0.1:8000/createpost
    '''
    print("/create-posts-a called...")
    print(payload)
    return { f"Created post for { payload['airport'] } and Airline: { payload['airline'] }" }

from typing import Optional
'''
Optional[...] is a shorthand notation for Union[..., None], telling the type checker 
that either an object of the specific type is required, or None is required. 
... stands for any valid type hint, including complex compound types or a Union[] 
of more types. Whenever you have a keyword argument with default value None, you should use Optional.
'''

'''
Define class using pydantic that tells us what structure we require for an API.
'''
class AirportData(BaseModel):
    ''' Define columns here '''
    airport: str
    airline: str
    # If you want an optional field, just give it a default value
    default_field: bool = True
    # Have field without default value but can be None
    # So this is optional AND if specified needs to be an int (error checked)
    rating: Optional[int] = None
    # You create fields only how you want to the user to send
    # In this case we use two fields like above 
    '''
    latitude: float
    longitude: float
    full_name: str
    create_date: Optional[datetime] = None
    '''

# Create api that uses the AirportData class: add to parameters
@app1.post("/create-posts")
async def create_posts_w_body(payload: AirportData):
    '''
    Simple call: curl -XPOST http://127.0.0.1:8000/createpost
    '''
    print("/create-posts called...with AirportData class as payload")
    print(payload)
    # Can convert any pydantic model to a dict
    print("dict:", payload.dict())

    # You access the class data like json with '.' operator 
    return { f"Created post for { payload.airport } and Airline: { payload.airline }" }
    
    # If you send incorrent data that does not match the structure
    # API auto sends an error:
    # curl ... -d '{ "airline":"United"}' ...
    # {"detail":[{"loc":["body","airport"],"msg":"field required","type":"value_error.missing"}...
    # Default fields like default_field are not required since it has default value   (returned to caller)

    # Error check on the Optional param:
    # curl -XPOST http://127.0.0.1:8000/create-posts -d '{ "airport":"JFK", "airline":"United", "rating":"a"}...
    # {"detail":[{"loc":["body","rating"],"msg":"value is not a valid integer"... (returned to caller)

# At this point we want to try saving our posts now in memory

# import random to simulate unique ids
from random import randrange

# Make sure to post some data first...
my_posts = []
# curl -X POST  http://127.0.0.1:8000/new-post -H 'Content-Type: application/json' -d '{ "airport":"EWR", "airline":"South West"}'
# curl -X POST  http://127.0.0.1:8000/new-post -H 'Content-Type: application/json' -d '{ "airport":"JFK", "airline":"United"}'
@app1.post("/new-post")
def create_post(payload: AirportData):
    ad_dict = payload.dict()
    # give id to post data 
    ad_dict['id'] = randrange(0, 10000)
    my_posts.append(ad_dict)
    return {"data":ad_dict}

# curl -X GET  http://127.0.0.1:8000/get-all-posts
@app1.get("/get-all-posts")
def get_all_posts():
    return { "posts" : my_posts }

# Create a function to find our post in the array
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

# Get data by id
# 
@app1.get("/get-data-byid/{id}")
def get_data(id: int):
    # Validate that id is an integer -> Just add ": int" to arg definition 
    print("Looking for id %d" % int(id))
    the_post = find_post(int(id))
    return {"post":the_post}

    

