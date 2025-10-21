from ultralytics import YOLO

model = YOLO("C:/Computer-Vision/Ultralytics/yolo12n.pt") 
results = model.train(epochs=5)
model.val()