import cv2

from ultralytics import solutions,YOLO

cap = cv2.VideoCapture("C:/Computer-Vision/data/src/Walking.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("isegment_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize instance segmentation object
isegment = solutions.InstanceSegmentation(
    show=True, 
    model="C:/Computer-Vision/Ultralytics/Models/yolo11n-seg.pt", 
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = isegment(im0)
    video_writer.write(results.plot_im) 

cap.release()
video_writer.release()
cv2.destroyAllWindows()