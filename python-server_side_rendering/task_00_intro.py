def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Template should be a string but got {type(template).__name__}.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees should be a list of dictionaries but got {type(attendees).__name__}.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        filled_values = {}
        for key in placeholders:
            val = attendee.get(key)
            if val is None:
                filled_values[key] = "N/A"
            else:
                filled_values[key] = str(val)

        try:
            content = template.format(**filled_values)
        except KeyError as e:
            print(f"Missing placeholder in template: {e}")
            content = template

        filename = f"output_{idx}.txt"
        with open(filename, "w") as f:
            f.write(content)