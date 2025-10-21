import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("C:/Computer-Vision/data/src/Walking.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("heatmap_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize heatmap object
heatmap = solutions.Heatmap(
    show=True,  
    model="Ultralytics/Models/yolo12m.pt",  
    colormap=cv2.COLORMAP_PARULA,  
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = heatmap(im0)
    # print(results)  # access the output
    video_writer.write(results.plot_im) 

cap.release()
video_writer.release()
cv2.destroyAllWindows()  