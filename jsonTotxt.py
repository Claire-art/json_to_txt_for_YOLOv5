import os
import json

def labelme_to_yolov5(labelme_path, yolov5_path, class_map):
    with open(labelme_path, 'r') as f:
        data = json.load(f)

    image_width = data['imageWidth']
    image_height = data['imageHeight']

    annotations = data['shapes']
    lines = []

    for annotation in annotations:
        label = annotation['label']
        class_id = class_map.get(label, -1)

        if class_id == -1:
            continue

        bbox = annotation['points']
        x_min = min(bbox[0][0], bbox[1][0])
        x_max = max(bbox[0][0], bbox[1][0])
        y_min = min(bbox[0][1], bbox[1][1])
        y_max = max(bbox[0][1], bbox[1][1])

        x_center = (x_min + x_max) / 2.0
        y_center = (y_min + y_max) / 2.0
        width = x_max - x_min
        height = y_max - y_min

        x_center /= image_width
        width /= image_width
        y_center /= image_height
        height /= image_height

        line = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
        lines.append(line)

    with open(yolov5_path, 'w') as f:
        f.write('\n'.join(lines))

def convert_folder(input_folder, output_folder, class_map):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            labelme_path = os.path.join(input_folder, filename)
            yolov5_filename = os.path.splitext(filename)[0] + ".txt"
            yolov5_path = os.path.join(output_folder, yolov5_filename)

            labelme_to_yolov5(labelme_path, yolov5_path, class_map)
            print(f"Converted {filename} to {yolov5_filename}")

# 변경해주어야 하는 부분
input_folder = 'path/to/json/folder' # json 파일이 있는 폴더 지정
output_folder = 'path/to/yolov5/folder' #txt 파일을 저장할 폴더 지정

# 클래스 넘버링 맞춰주기!
class_map = {
    'class1': 0,
    'class2': 1,
}

convert_folder(input_folder, output_folder, class_map)
