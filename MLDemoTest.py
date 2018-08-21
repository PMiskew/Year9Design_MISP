'''Tk_Canvas_Image_url.py
display an image obtained from an internet web page in Tkinter
tested with Python27 and Python33  by  vagaseat   21nov2012
'''
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

import io
import base64

try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen


root = tk.Tk()
root.title("display a website image")
# a little more than width and height of image
w = 520
h = 320
x = 80
y = 100
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# this GIF picture previously downloaded to tinypic.com
image_url = "http://i46.tinypic.com/r9oh0j.gif"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)
# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')
# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
cv.create_image(10, 10, image=photo, anchor='nw')

app = ClarifaiApp(api_key='25dd403977044f108b994b4fb8a5c7c0')

model = app.models.get('general-v1.3')
image = ClImage(url=image_url)
print(model.predict([image]))
root.mainloop()