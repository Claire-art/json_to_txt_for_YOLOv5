labelme 버전이 다르면 json 형식이 달라지는 문제 해결


## 변경해주어야 하는 부분

**1.**
```python
input_folder = 'path/to/json/folder' # json 파일이 있는 폴더 지정

output_folder = 'path/to/yolov5/folder' #txt 파일을 저장할 폴더 지정
```

**2.**
```python
class_map = {
    'class1': 0,
    'class2': 1,
}
```
