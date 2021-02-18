from global_vars import *

for obj in s3.Bucket('nyc-business-map').objects.all():
    print(obj)

