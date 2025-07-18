import cv2
import numpy as np

# Use correct camera index (0 for webcam, 1 or URL for phone cam)
cap = cv2.VideoCapture(1)

# Blue ball HSV range (tuned for indoor light)
lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])

trajectory = []
ball_count = 1
swing_type = "Waiting..."

def classify_swing(path):
    if len(path) < 5:
        return "Too short"
    x_positions = [p[0] for p in path]
    dx = x_positions[-1] - x_positions[0]

    if abs(dx) < 15:
        return "Straight"
    elif dx > 15:
        return "Outswing"
    elif dx < -15:
        return "Inswing"
    else:
        return "Unknown"

frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.GaussianBlur(mask, (9, 9), 0)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest)

        if radius > 5:
            center = (int(x), int(y))
            cv2.circle(frame, center, int(radius), (0, 255, 0), 2)
            trajectory.append(center)

    for i in range(1, len(trajectory)):
        if trajectory[i - 1] and trajectory[i]:
            cv2.line(frame, trajectory[i - 1], trajectory[i], (255, 0, 0), 2)

    # Add header text
    header_text = f"Ball #{ball_count} ➤ {swing_type.upper()}"
    cv2.putText(frame, header_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 3)

    cv2.imshow("Live Swing Detection", frame)
    frame_counter += 1

    # Every 40 frames, detect and reset
    if frame_counter >= 40:
        new_result = classify_swing(trajectory)
        if new_result != "Too short":
            swing_type = new_result
            ball_count += 1
        trajectory.clear()
        frame_counter = 0

    # Press ESC to quit
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()