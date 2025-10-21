from ultralytics import solutions

inf = solutions.Inference(
    model="C:/Computer-Vision/Ultralytics/Models/yolo12m.pt",
)

inf.inference()
