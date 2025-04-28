FROM python:3.12

# Set working directory
WORKDIR /var/www/app

# Copy application files
COPY . .

# Upgrade pip and install dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r requirements.txt && \
    pip3 install --no-cache-dir pyautogui mouseinfo pillow

# Command to run the application
CMD ["python3", "main_driver_code.py"]