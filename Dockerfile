FROM python:3.12

# Install required dependencies including xvfb
RUN apt-get update && apt-get install -y \
    xvfb \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libappindicator3-1 \
    libasound2 \
    fonts-liberation \
    libnspr4 \
    libnss3 \
    libxss1 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    wget \
    gnupg \
    xauth

# Set environment variable for the DISPLAY
ENV DISPLAY=:99

# Copy the application files and install dependencies
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Install pyautogui and dependencies
RUN pip3 install pyautogui mouseinfo pillow

# Default command (e.g., running tests or app)
CMD ["pytest"]
