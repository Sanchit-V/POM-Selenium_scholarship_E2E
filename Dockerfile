FROM python:3.12

# Set working directory
WORKDIR /var/www/app

# Copy application files
COPY . .

# Install xvfb and other dependencies
RUN apt-get update && apt-get install -y \
    xvfb \
    xauth \
    libxrender1 \
    libxtst6 \
    libxi6
# Upgrade pip and install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r requirements.txt && \
    pip3 install --no-cache-dir pyautogui mouseinfo pillow

# No CMD here; let docker-compose.yml handle the command with xvfb-run
