created app/ to go with best practice structure


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

