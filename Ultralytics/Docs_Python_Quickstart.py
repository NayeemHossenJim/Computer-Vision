from ultralytics import YOLO

model = YOLO("C:/Computer-Vision/Ultralytics/yolo12n.pt")

results = model.predict("C:/Computer-Vision/data/Walking.mp4")

# Export the model to ONNX format
success = model.export(format="onnx")