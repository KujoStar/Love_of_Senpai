import os
import pandas as pd
import json
from PIL import Image, ImageDraw, ImageFont

# 字体准备
font_name = ImageFont.truetype("C:Windows/Fonts/msyh.ttc", 174)
font_saying = ImageFont.truetype("C:Windows/Fonts/simhei.ttf", 137)

source_json = "settings.json"# 设置文件，可以设置名字和天数，一一对应填入list
template_picture = "田所.jpg"# 作为底图的图片，可以自行更换
target_folder_name = "先辈的爱"# 目标文件夹名，可以自行更换

with open(source_json, "r", encoding = "utf-8") as f:
    json_content = json.load(f)

names = json_content["name"]
days = json_content["day"]

assert len(names) == len(days), "名字数和天数不对应（恼），给我修改三回啊三回"

# 重定义图片尺寸
x, y = 2137, 2137

# 实现居中功能（大概看上去居中
def pos(underline):
 return (565 - len(underline) / 2 * 37)

for i in range(0, len(names)):
    try:
        image = Image.open(template_picture)
    except Exception as e:
        raise Exception("打开图片失败！检查文件名是否有误")
    
    image = image.resize((x, y))
    draw = ImageDraw.Draw(image)
    
    name = names[i]
    day = days[i]
    
    draw.text((838, 1765), name, (0,213,250), font = font_name)
    draw = ImageDraw.Draw(image)
    saying = "这是我爱你的第" + str(day) + "天"
    draw.text((pos(saying), 1915 + 60), saying, (0, 213, 250), font = font_saying)
    draw = ImageDraw.Draw(image)
    
    # 保存图片
    if not os.path.exists(target_folder_name):
        os.makedirs(target_folder_name)
    image.save(f"{target_folder_name}/{name}.jpg")