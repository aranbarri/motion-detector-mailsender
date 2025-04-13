FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    libatlas-base-dev libjpeg-dev libtiff5 libgl1-mesa-glx \
    libqt5gui5 libqt5widgets5 libqt5core5a libqt5dbus5 \
    libxcb-xinerama0 libxcb-randr0 libxcb-shape0 \
    libxkbcommon-x11-0 libxrender1 libsm6 libxext6 \
    libx11-6 libxcb1 && \
    apt-get clean

WORKDIR /detektor

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY detektor/ .

CMD ["python", "motion_detektor.py"]
