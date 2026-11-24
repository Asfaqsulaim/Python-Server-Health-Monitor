import json

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            config = json.load(config_file)

            required_keys = ["CPU_LIMIT",
                             "RAM_LIMIT",
                             "DISK_LIMIT", 
                             "INTERVAL"]
        for key in required_keys:
            if key not in config:
                raise ValueError(f"Missing required configuration key: {key}")

        for key in ["CPU_LIMIT", "RAM_LIMIT", "DISK_LIMIT"]:
            value = config[key]
            if not isinstance(value, int) or isinstance(value, bool):
                raise ValueError(f"{key} must be a number.")
            if not 0 <= value <= 100:
                raise ValueError(f"{key} must be between 0 and 100.")
    
        if not isinstance(config["INTERVAL"], int) or isinstance(config["INTERVAL"], bool):
                raise ValueError ("INTERVAL must be an integer.")

        if config["INTERVAL"] <= 0:
                raise ValueError("INTERVAL must be a positive number.")

        return config
            
    except FileNotFoundError:
         print(" ERROR: Configuration file not found.")

    except json.JSONDecodeError:
        print(" ERROR: Invalid JSON format.")

    except ValueError as e:
        print(f" Configuration Error: {e}")

    return None