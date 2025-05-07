# Update the base image to a more secure and recent version
FROM python:3.11-slim

# Set working directory
WORKDIR /app
USER root

# Install dependencies and Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
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
    xauth \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variable for Xvfb
ENV DISPLAY=:99

# Create a folder for pasting files from the local PC
RUN mkdir -p /home/seluser/Local_Paste_Files && \
    chown -R root:root /home/seluser/Local_Paste_Files

# Copy Upload_Files into container
COPY ./Upload_Files /home/seluser/Local_Paste_Files

# Add a script to copy files from Upload_Files to Local_Paste_Files
RUN echo "#!/bin/bash\ncp -r /home/seluser/Upload_Files/* /home/seluser/Local_Paste_Files/" > /usr/local/bin/copy_files.sh && \
    chmod +x /usr/local/bin/copy_files.sh

# Install Python dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install webdriver-manager pytest-html pyautogui mouseinfo pillow

# Copy application code
COPY . .

# Update CMD to execute the copy_files.sh script before running pytest
CMD ["sh", "-c", "/usr/local/bin/copy_files.sh && Xvfb :99 -screen 0 1920x1080x24 & pytest main_driver.py -v"]
