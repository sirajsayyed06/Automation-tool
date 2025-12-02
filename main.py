import json
from automation.file_organizer import organize_files
from automation.excel_parser import parse_excel
from automation.email_alerts import send_alert
from automation.system_cleanup import clean_system

def load_settings():
    with open("config/settings.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    settings = load_settings()

    if settings["tasks"]["file_organizer"]:
        organize_files(settings["paths"]["downloads"])

    if settings["tasks"]["excel_parser"]:
        parse_excel(settings["paths"]["excel_file"])

    if settings["tasks"]["email_alerts"]:
        send_alert("Automation Tasks Completed")

    if settings["tasks"]["system_cleanup"]:
        clean_system(settings["paths"]["cleanup_target"])

    print("All selected automation tasks completed.")
