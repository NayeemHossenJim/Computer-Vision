import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("C:/Users/nayee/OneDrive/Documents/Computer-Vision/data/Jam.mp4")
assert cap.isOpened(), "Error reading video file"

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("speed_management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

speedestimator = solutions.SpeedEstimator(
    show=True, 
    model="C:/Users/nayee/OneDrive/Documents/Computer-Vision/Ultralytics/yolo12n.pt",
    fps=fps,
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = speedestimator(im0)
    video_writer.write(results.plot_im)  

cap.release()
video_writer.release()
cv2.destroyAllWindows() 