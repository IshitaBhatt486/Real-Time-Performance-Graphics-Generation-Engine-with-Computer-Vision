from camera.camera import Camera
import cv2

camera = Camera()

while True:

    data = camera.get_frame()

    frame=data["frame"]

    fps=data["fps"]

    if frame is None:
        break

    print(frame)
    print(fps)

    cv2.imshow("MIPE", frame)

    if cv2.waitKey(1)==ord('q'):
        break

camera.release()
cv2.destroyAllWindows()