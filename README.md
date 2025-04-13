# 📸 Motion Detector and Email Sender with PiCamera2 and OpenCV

This project uses a Raspberry Pi with a PiCamera2 module (IMX219, OV5647) to detect motion using OpenCV. When motion is detected, an image is saved and automatically sent to a configured email address. You can customize motion sensitivity and resolution easily using environment variables.

##  Features
- Motion detection via frame differencing
- Photo capture on movement
- Automatic email alerts with attached images
- Live preview window using OpenCV
- Dockerized for easy deployment
- Configurable sensitivity via environment variable `DIFF_THRESHOLD`

---

## 🧰 Requirements
- Raspberry Pi with PiCamera2 module - (IMX219, OV5647)
- Raspberry Pi OS (Bullseye or newer)
- Python 3.9+
- Docker & Docker Compose

---

## 🔧 Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/motion-detector.git
cd motion-detector
```

### 2. Set your environment variables

Edit the `docker-compose.yml` or create a `.env` file:

```env
SENDER_EMAIL=youremail@gmail.com
RECIPIENT_EMAIL=destination@example.com
EMAIL_PASSWORD=your_app_password
DIFF_THRESHOLD=5000
```

> 💡 Tip: Use an app-specific password if you have 2FA enabled on Gmail.


### 3. Build and run
```bash
docker-compose up --build
```

The motion detection script will start and display a live preview. Images with detected motion will be saved and emailed.

---

## 🗂 Project Structure

```
motion-detector/
├── app/
│   └── motion_detector.py      # Main script
├── Dockerfile                  # Container setup
├── docker-compose.yml          # Service configuration
├── requirements.txt            # Python dependencies
└── .env                        # Email and detection settings
```

---

## 🛠 Customize
- Adjust motion sensitivity with the `DIFF_THRESHOLD` environment variable.
- Change the capture resolution in `camera_config` in the Python script.
- Modify the email logic to send to multiple addresses or use other services (e.g. Telegram, Discord).

---

## 📜 License
MIT License

---
