from ultralytics.data.annotator import auto_annotate

auto_annotate(data="C:/Computer-Vision/data/Cow.jpg", det_model="C:/Computer-Vision/Ultralytics/yolo12n.pt", sam_model="Ultralytics\sam2_b.pt")