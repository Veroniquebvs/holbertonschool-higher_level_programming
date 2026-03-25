import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error : {template} isn't a string")
        return None
    if not template:
        print("Template is empty, no output files generated.")
        return None

    if not isinstance(attendees, list):
        print(f"Error : {attendees} isn't a list")
        return None
    if not attendees:
        print("No data provided, no output files generated.")
        return None
    for items in attendees:
        if not isinstance(items, dict):
            print(f"{items} isn't a list of dictionaries")
            return None

    for i, guest in enumerate(attendees):
        filename = f"output_{i+1}.txt"
        if os.path.exists(filename):
            continue
        else:
            result = template
            placeholders = ["name", "event_title", "event_date",
                            "event_location"]
            for key in placeholders:
                value = guest.get(key)
                if value is None:
                    value = "N/A"
                result = result.replace("{" + key + "}", str(value))
            with open(filename, "w") as f:
                f.write(result)
