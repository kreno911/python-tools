###! This was moved here as our "endpoint" file

# This was main_test.py

# Showing how structure is supposed to work 

from fastapi import APIRouter

# We use APIRouter for this API
router = APIRouter()

@router.get("/")
async def root():
    print("/ called...")
    return { "This is a test FastAPI service" }

@router.get("/posts")
async def posts():
    print("/posts called...")
    return { "posts": "These are posts" }

@router.post("/createpost")
async def create_posts():
    '''
    Simple call: curl -XPOST http://127.0.0.1:8000/createpost
    '''
    print("/createpost called...")
    return { "This creates posts" }

