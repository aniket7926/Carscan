# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import json

def visualize(img_file,json_file):
  with open(json_file) as f:
    data = json.load(f)
  img=Image.open(img_file)
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype("/content/sample_data/arial.ttf", 20)
  #Iteration through each dictionary in the json file,
  for i in range(1,len(data)):
    text=data[i]['value']['polygonlabels']
    for j in range(0,len(data[i]['value']['points'])):
      x=data[i]['value']['points'][j][0]
      y=data[i]['value']['points'][j][1]
      x=(x*data[i]['original_width'])/100
      y=(y*data[i]['original_height'])/100
      draw.rectangle([x,y,x+100,y+100],outline='green',width=2)#The width and Height were not mentioned in the json file. Therefore, used 100 as default value for creating a box.
      draw.text((x,y-10),text,font=font)

  img.show()
  img.save('results.jpg')
