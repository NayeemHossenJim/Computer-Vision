from ultralytics import YOLO

Model = YOLO('yolo12n.pt')

Results = Model.track('C:/Computer-Vision/OpenCV/0.Data/Cow.mp4', show=True, save=True)