from picamera2 import Picamera2
import cv2
import time
from datetime import datetime
import numpy as np
import smtplib
from email.message import EmailMessage
import os

# see docker-compose
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
DIFF_THRESHOLD = int(os.environ.get("DIFF_THRESHOLD"))
CAMERA_WIDTH = int(os.environ.get("CAMERA_WIDTH"))
CAMERA_HEIGHT = int(os.environ.get("CAMERA_HEIGHT"))

def movement_detect(filename):
    msg = EmailMessage()
    msg["Subject"] = "Movement detected!!"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg.set_content(f"{filename}")

    with open(filename, "rb") as f:
        img_data = f.read()
        msg.add_attachment(img_data, maintype="image", subtype="jpeg", filename=filename)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print("Image sent.")
    except Exception as e:
        print(f"Error while sending the email: {e}")

# Start
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(main={"format": "BGR888", "size": (CAMERA_WIDTH,CAMERA_HEIGHT)})
picam2.configure(camera_config)
picam2.start()
time.sleep(2)

# Initial capture
prev_frame = picam2.capture_array()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

try:
    while True:
        time.sleep(2)
        frame = picam2.capture_array()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Frame diff
        delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        movement_score = cv2.countNonZero(thresh)

        print(f"Movimiento detectado: {movement_score} px")

        # Configure number of pixels 
        if movement_score > DIFF_THRESHOLD:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"motion_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Movimiento detectado. Imagen guardada como {filename}")
            movement_detect(filename)
            time.sleep(1)

        # Refresh
        prev_gray = gray

except KeyboardInterrupt:
    print(" Detección detenida por el usuario.")
finally:
    picam2.close()
