import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {message}\n"

    with open("logs/automation.log", 'a') as f:
        f.write(log_entry)

    print(log_entry, end="")