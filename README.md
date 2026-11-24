Python Server Health Monitoring System

A Python-based server monitoring tool that tracks CPU, RAM, and disk usage, checks configurable thresholds, generates alerts, and records monitoring information in log files.

Features

- CPU Monitoring: Tracks CPU utilization.
- RAM Monitoring: Tracks memory utilization.
- Disk Monitoring: Tracks disk usage.
- Configurable Thresholds: Set CPU, RAM, and disk limits using "config.json".
- Automated Alerts: Detects when resource usage exceeds configured limits.
- Overall Health Status: Reports whether the server is HEALTHY or WARNING.
- Monitoring Summary: Counts healthy and warning metrics.
- Error Handling: Handles monitoring failures and retries after the configured interval.
- Logging: Records monitoring information, warnings, and errors.
- Configuration Validation: Checks configuration values before monitoring starts.
- Unit Testing: Includes automated tests for monitoring, alerts, and configuration.

Technologies Used

- Python
- psutil
- JSON
- Logging
- Unittest
- Git and GitHub

Project Structure

server-health-monitor/
│
├── main.py
├── monitor.py
├── alerts.py
├── config_loader.py
├── config.json
├── requirements.txt
├── test_alerts.py
├── test_config.py
├── test_monitor.py
├── .gitignore
└── README.md

Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder

cd server-health-monitor

3. Install dependencies

python -m pip install -r requirements.txt

Configuration

Edit "config.json" to customize monitoring thresholds and intervals.

Example:

{
    "CPU_LIMIT": 80,
    "RAM_LIMIT": 75,
    "DISK_LIMIT": 90,
    "INTERVAL": 5
}

- CPU_LIMIT: Maximum CPU usage percentage.
- RAM_LIMIT: Maximum RAM usage percentage.
- DISK_LIMIT: Maximum disk usage percentage.
- INTERVAL: Monitoring interval in seconds.

Running the Application

Start the monitoring system:

python main.py

The application continuously monitors system resources and displays monitoring reports in the terminal.

Running Tests

Execute the automated test suite:

python -m unittest discover -v

Logging

Monitoring information, warnings, and errors are recorded in "server_monitor.log".

The log file helps track system performance and troubleshoot monitoring failures.

Learning Outcomes

Through this project, I practised:

- Python programming and OOP fundamentals.
- Working with external Python libraries.
- System resource monitoring.
- Configuration management using JSON.
- Exception handling and recovery.
- Logging and debugging.
- Unit testing.
- Git and GitHub project management.

Future Improvements

- Email notifications for critical alerts.
- Web-based monitoring dashboard.
- Historical performance reports.
- Docker containerization.
- Cloud-based monitoring integration.

---

Project: Python Server Health Monitoring System
Purpose: Practical learning project focused on Python, system monitoring, and DevOps fundamentals.