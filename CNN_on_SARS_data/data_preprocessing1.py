import os
import xmltodict
from collections import OrderedDict
import json


def getImageXml(img_tag):
    return f'./LS-SSDD-v1.0-OPEN/Annotations_sub/{img_tag}.xml'


all_ships = []
number_of_rows = 20
number_of_cols = 20
for file in os.listdir('./LS-SSDD-v1.0-OPEN/Annotations_sub'):
    img_tag = file.split('.')[0]
    xml_path = getImageXml(img_tag)
    with open(xml_path) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())['annotation']
        img_width = int(data_dict['size']['width'])
        img_height = int(data_dict['size']['height'])
        all_ships.append({'img_tag': img_tag, 'ships': [], 'ship_count': 0})
        if 'object' in data_dict:
            objects = data_dict['object']
            for ship in objects:
                if type(ship) == OrderedDict and 'name' in ship and ship['name'] == 'ship' and 'bndbox' in ship:
                    x_min = int(ship['bndbox']['xmin']) / img_width
                    y_min = int(ship['bndbox']['ymin']) / img_height
                    x_max = int(ship['bndbox']['xmax']) / img_width
                    y_max = int(ship['bndbox']['ymax']) / img_height
                    x_center = (x_min + x_max) / 2
                    y_center = (y_min + y_max) / 2
                    width = x_max - x_min
                    height = y_max - y_min
                    all_ships[-1]['ships'].append(
                        {'x_center': x_center, 'y_center': y_center, 'width': width, 'height': height})
                    all_ships[-1]['ship_count'] += 1


with open('output.json', 'w') as outfile:
    json.dump(all_ships, outfile)
