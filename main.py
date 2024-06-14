# filename: python_example.py
# dir: yolov8/python_example.py
from ultralytics import YOLO

# build a new model from scratch
# model = YOLO("ultralytics/models/v8/yolov8s.yaml")
# # train the model
# results = model.train(**{'cfg':'ultralytics/yolo/cfg/default.yaml'})

model = YOLO("/home/sjw/Project/ultralytics-main/ultralytics/yolo/v8/detect/yolov8s.pt")  # or a segmentation model .i.e yolov8n-seg.pt
model.track(
    source="/home/sjw/Project/ultralytics-main/ultralytics/assets",
    stream=True,
    tracker="botsort.yaml/bytetrack.yaml"
)