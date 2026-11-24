Python Server Health Monitoring System

This is an individual Python project I built to learn more about system monitoring and DevOps fundamentals.

The application monitors CPU usage, RAM usage, and disk usage. It checks these values against configurable limits and generates alerts when resource usage goes beyond the defined thresholds.

It also records monitoring information in a log file, making it easier to track events and identify errors.

Features

- CPU Monitoring: Checks current CPU utilization.
- RAM Monitoring: Tracks memory usage.
- Disk Monitoring: Checks disk space utilization.
- Configurable Thresholds: Allows resource limits and monitoring intervals to be changed through `config.json`.
- Alerts: Detects when CPU, RAM, or disk usage exceeds the configured limits.
- Health Status: Displays an overall HEALTHY or WARNING status.
- Monitoring Summary: Shows the number of healthy and warning metrics.
- Error Handling: Handles monitoring errors and continues monitoring after the configured interval.
- Logging:** Records monitoring activity, warnings, and errors in a log file.
- Configuration Validation: Checks configuration values before starting the monitoring process.
- Unit Testing: Includes tests for monitoring, alert handling, and configuration validation.

Technologies Used

- Python
- psutil
- JSON
- Python Logging
- unittest
- Git and GitHub
- GitHub Actions

Project Structure

```text
Python-Server-Health-Monitor/
│
├── .github/
│   └── workflows/
│       └── python-tests.yml
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
```

Getting Started

1. Clone the repository

```bash
git clone https://github.com/Asfaqsulaim/Python-Server-Health-Monitor.git
```

2. Open the project folder

```bash
cd Python-Server-Health-Monitor
```

3. Install the required dependencies

```bash
python -m pip install -r requirements.txt
```

Configuration

The monitoring thresholds and interval can be changed in `config.json`.

Example configuration:

```json
{
    "CPU_LIMIT": 80,
    "RAM_LIMIT": 75,
    "DISK_LIMIT": 90,
    "INTERVAL": 5
}
```

- `CPU_LIMIT`: Maximum CPU usage percentage.
- `RAM_LIMIT`: Maximum RAM usage percentage.
- `DISK_LIMIT`: Maximum disk usage percentage.
- `INTERVAL`: Time between monitoring cycles, in seconds.

The configuration loader checks these values before the monitoring process starts.

Running the Application

Run the following command from the project directory:

```bash
python main.py
```

The application will continuously monitor system resources and display the results in the terminal.

Running the Tests

I included unit tests to check the monitoring functions, alert conditions, and configuration validation.

To run all tests:

```bash
python -m unittest discover -v
```

GitHub Actions

I also added a GitHub Actions workflow to automate the testing process.

Whenever code is pushed or a pull request is created, the workflow:

1. Sets up the Python environment.
2. Installs the required dependencies.
3. Runs the unit tests.
4. Reports whether the tests pass or fail.

This helped me understand the basics of Continuous Integration (CI) and how automated testing can be included in a development workflow.

What I Learned

While building this project, I got practical experience with:

- Monitoring system resources using Python.
- Working with the `psutil` library.
- Managing configuration through JSON.
- Handling exceptions and application errors.
- Implementing logging for monitoring and debugging.
- Writing unit tests.
- Using Git and GitHub to manage project changes.
- Setting up a basic CI workflow with GitHub Actions.

Future Improvements

Some features I'd like to explore in future versions:

- Email notifications for critical alerts.
- Historical monitoring reports.
- Docker containerization.
- Integration with cloud monitoring services.
- An optional web-based dashboard.
