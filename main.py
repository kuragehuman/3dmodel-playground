import cv2
import mediapipe as mp
import matplotlib.pyplot as plt


import mediapipe
print(mediapipe)
print(mediapipe.__file__)

mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

with mp_pose.Pose(static_image_mode=False) as pose:

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = pose.process(image_rgb)

        if result.pose_world_landmarks:

            landmarks = result.pose_world_landmarks.landmark

            xs = [lm.x for lm in landmarks]
            ys = [lm.y for lm in landmarks]
            zs = [lm.z for lm in landmarks]

            plt.clf()

            ax = plt.axes(projection="3d")
            ax.scatter(xs, ys, zs)

            plt.pause(0.001)

        cv2.imshow("camera", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()