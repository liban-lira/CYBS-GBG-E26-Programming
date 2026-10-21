# ---------------------------------Exercise 1 - Scanner settings--------------------------
def validate_scan_intensity(input):
    try:
        scan = int(input)
    except ValueError:
        raise ValueError("Intensity must be a number")
    if not (1 <= scan <= 10):
        raise ValueError("Intensity must be between 1 and 10")

    return scan


# Usage
# try:
#     scan_input = input("Enter number: ")
#     valid_scan = validate_scan_intensity(scan_input)
#     print(f"Valid port: {valid_scan}")
# except ValueError as e:
#     print(f"Invalid input: {e}")


def validate_timeout(input):
    try:
        timeout = int(input)
    except ValueError:
        raise ValueError("Timeout must be a number")
    if not (1 <= timeout <= 300):
        raise ValueError("Timeout must be between 1 and 300")

    return timeout


# Usage
# try:
#     timeout_input = input("Enter number: ")
#     valid_timeout = validate_timeout(timeout_input)
#     print(f"Valid port: {valid_scan}")
# except ValueError as e:
#     print(f"Invalid input: {e}")


# ---------------------------------Exercise 2 - Allow or block?--------------------------


def validate_scan_type(value):
    allowed_list = ["network", "port", "vulnerability"]

    if value.lower() not in allowed_list:
        raise ValueError(
            "scan type must be one of the following: [network, port, vulnerability]"
        )
    return value.lower()


# Usage
# try:
#     scan = validate_scan_type("POT")
#     print("this is allowed:", scan)

# except ValueError as e:
#     print(e)

# ---------------------------------Exercise 3 - IP Address Validator --------------------------

# LØSNING LAVET AF MATHIAS
import re


def validate_ip_advanced(ip):
    # More robust IPv4 pattern
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    pat2 = r"^(10\.|192\.168|172\.1[6-9]\.|172\.2[0-9]\.|172\.3[0-1]\.)"
    if not re.match(pattern, ip):
        raise ValueError("Invalid IP address format")
    if re.match(pat2, ip):
        raise ValueError("Private ips is not accepted")

    return ip


# Usage
# try:

#     ip = validate_ip_advanced("192.169.29.1")
#     print("valid:", ip)
# except ValueError as e:
#     print(e)

# ---------------------------------Exercise 4 - Security Config Validator--------------------------

config = {
    "scan_type": "network",
    "target_ips": ["8.8.8.8", "1.1.1.1", "100.22.21.22"],
    "scan_intensity": 5,
    "timeout": 10,
    "output_file": "scan>results.txt",
}


def sanitize_filename(filename):
    # Remove dangerous characters
    dangerous_chars = '<>:"/\\|?*'
    for char in dangerous_chars:
        filename = filename.replace(char, "_")
    # Remove leading/trailing dots and spaces
    filename = filename.strip(". ")
    return filename


def security_config_validator(config):
    return {
        "scan_type": validate_scan_type(config["scan_type"]),
        "target_ips": [validate_ip_advanced(ip) for ip in config["target_ips"]],
        "scan_intensity": validate_scan_intensity(config["scan_intensity"]),
        "timeout": validate_timeout(config["timeout"]),
        "output_file": sanitize_filename(config["output_file"]),
    }


try:
    result = security_config_validator(config)
    print(result)
except ValueError as e:
    print(e)
