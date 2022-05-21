# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

### Create env variables 
# Up Bank API key
ENV api_token="up:yeah:0pQ3QobrxkOzFetYj3uDvgKPqXECo1OlN64U49v8R9NOMkXKgOSlJPVB5lYjsxhcWnMBvQz0SSEiWhbQDP5w4xpckaHNLiIMvC2bJqBVeJI5nZWp5MBu4Q4or42fYhX6"
# # Binance API key
ENV bin_token="OmkFFB1UaQDx8rAiD5C78bE4JOXw4O9V9xxnY2lN5rP6T8cvY8sYRDA0ANub5f6I"
ENV bin_secret="etDykKq85CUDP6p0BGNPrOO4E3juffM4YM9QDwUIJVEQ8murJDPcMbm8WgF4kcqg"
# # Database connection info
ENV host_url="192.168.0.222"
ENV sql_port=4307
ENV sql_usr="root"
ENV sql_pass="ironman"


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "src/main.py"]

