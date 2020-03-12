import requests
import base64
import json

import cv2
import numpy as np
import argparse


def from_base64(base64_data):
    
    nparr = np.fromstring(base64.b64decode(base64_data), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR)

def img_base64(img_path):
    with open(img_path,"rb") as f:
        base64_str = base64.b64encode(f.read())
    return base64_str


parser = argparse.ArgumentParser()
parser.add_argument("--img", help="img name")
args = parser.parse_args()

print(args.img)

img_b64 = img_base64(args.img)

r = requests.post('http://140.112.31.84:9487/',  json={"img": str(img_b64, 'utf-8')})
   
result = json.loads(r.content)
     
print(result['ans'])

   
