# This module contains routines used for basic image data manipulation
from PIL import Image
import re
from io import BytesIO
import base64

def base64_to_img(base64_data):
    # Convert image from base64 text format to native/viewable image file
    #print(base64_data) # Print image_data as sanity check
    image_data = re.sub('^data:image/.+;base64,', '', base64_data) #.decode('base64') # Removes metadata from start of text string
    #print(image_data) # Print image_data as sanity check
    image_obj = Image.open(BytesIO(base64.b64decode(image_data))) # creates an image object from stripped base64 data
    return image_obj

def img_rot_90deg(image_obj):
    # Convert image from native/viewable image file to base64 text format
    return image_obj.rotate(90) # degrees counter-clockwise

def img_to_base64(image_obj):
    # Convert image from native/viewable image file to base64 text format
    buffered = BytesIO()
    image_obj.save(buffered, format="png")
    img_str_encoded = base64.b64encode(buffered.getvalue())
    img_str = 'data:image/png;base64,' + img_str_encoded.decode("utf-8")
    return img_str

def img_to_disk(image_obj,filename):
    # Save image to specified location on disk
    image_obj.save('./img/'+filename+'.png','png') # This should be an absolute path
    return 'image saved!'
