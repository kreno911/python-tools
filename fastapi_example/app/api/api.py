# This is the main API file which makes actual calls to our API

# Import from our endpoints folder
from .endpoints import posts

from fastapi import APIRouter

router = APIRouter()
# The prefix is what will be added to the URL when calling
# so: 8080:/p/posts to get posts 
# You could make this /posts so in posts.py you do not need /posts but "/" only 
# as /posts will be added to every function handling a path 
router.include_router(posts.router, prefix="/p", tags="[Posts]")


