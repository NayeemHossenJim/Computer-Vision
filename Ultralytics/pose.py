from ultralytics import YOLO

model = YOLO('yolo11n-pose.pt')
results = model.track('C:/Computer-Vision/data/Walking.mp4', show=True, save=True)