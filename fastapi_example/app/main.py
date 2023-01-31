#####
# When you run this need to be in /home/weather/mike/tests/venvs/test_api
#   uvicorn app.main:app --reload
# It follows the path from app down
# Complete call:
#   curl -X GET  http://127.0.0.1:8000/api/p/posts
#   Note /api begins the call from prefix below
#
# Installed into AWS lambda... make sure to zip site-packages to root:
#   cd lib/python3.8/site-packages/
#   zip -r9 ../../../test-api-function.zip .
#   # Then add your code base
#   zip -g ./test-api-function.zip -r app
#   # Upload to some S3 location
#   aws s3 cp test-api-function.zip s3://eimdev1-eim-upload/testit/ --sse
#   # Lambda will not be able to show code when you provide zip as it does not know 
#   # which py file to use...
#   # You specify handler in Runtime settings: app.main.handler
#   URL for api after creating API gateway resource:
#   https://fx4q6qg3c2.execute-api.us-gov-west-1.amazonaws.com/dev/api/p/posts
#####

from fastapi import FastAPI

# mangum import
from mangum import Mangum

# SO, from app dir get api/ and api.py lib/package 
from app.api.api import router as api_router

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "This is the root" }


# Tell the app to include this router with extra prefix
app.include_router(api_router, prefix="/api")
# Need to add Mangum handler  (needed for AWS LAMBDA)
handler = Mangum(app)

