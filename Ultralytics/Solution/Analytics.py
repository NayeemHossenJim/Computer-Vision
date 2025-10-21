import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("C:/Computer-Vision/data/src/Walking.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(
    "analytics_output.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (1280, 720),  # this is fixed
)

# Initialize analytics object
analytics = solutions.Analytics(
    show=True,  # display the output
    analytics_type="area",  # pass the analytics type, could be "pie", "bar" or "area".
    model="C:/Computer-Vision/Ultralytics/Models/yolo12m.pt",
)

# Process video
frame_count = 0
while cap.isOpened():
    success, im0 = cap.read()
    if success:
        frame_count += 1
        results = analytics(im0, frame_count)
        out.write(results.plot_im)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows() 