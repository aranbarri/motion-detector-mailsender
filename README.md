# 📸 Motion Detector and Email Sender with PiCamera2 and OpenCV

This project uses a Raspberry Pi with a PiCamera2 module (IMX219, OV5647) to detect motion using OpenCV. 

When motion is detected, an image is saved and automatically sent to a configured Gmail address. You can customize motion sensitivity and resolution easily using environment variables.

##  Features
- Motion detection via frame differencing
- Photo capture on movement
- Automatic email alerts with attached images
- Live preview window using OpenCV
- Dockerized for easy deployment
- Configurable sensitivity via environment variable `DIFF_THRESHOLD`

---

##  Requirements
- Raspberry Pi with PiCamera2 module - (IMX219, OV5647)
- Raspberry Pi OS (Bullseye or newer)
- Python 3.9+
- Docker & Docker Compose

---

##  Setup

### 1. Clone the repository
```bash
git clone https://github.com/aranbarri/motion-detector-mailsender.git
cd motion-detector-mailsender
```

### 2. Set your environment variables

Edit the `docker-compose.yml`:

```env
SENDER_EMAIL=youremail@gmail.com
RECIPIENT_EMAIL=destination@example.com
EMAIL_PASSWORD=your_app_password
DIFF_THRESHOLD=5000
CAMERA_WIDTH = 2028
CAMERA_HEIGHT = 1520
```
> Use an app-specific password if you have 2FA enabled on Gmail.


### 3. Build and run
```bash
docker-compose up -d
```

The motion detection script will start and display a live preview. Images with detected motion will be saved and emailed.

---

## 🗂 Project Structure

```
motion-detector-mailsender/
├── detektor/
│   └── motion_detektor.py      # Main script
├── Dockerfile                  # Container setup
├── docker-compose.yml          # Service configuration
├── requirements.txt            # Python dependencies
```

---

## 🛠 Customize
- Adjust motion sensitivity with the `DIFF_THRESHOLD` environment variable.
- Change the capture resolution the same way.
- Modify the email logic to send to multiple addresses or use other services (e.g. Telegram, Discord).

---

## 📜 License
MIT License

---
