def create_dropdown(name, options):

    base = (
        f"<label for='{name}'>Choose {name}:</label>"
        f"<select id='{name}' name='{name}'>"
    )
    choices = [f"<option value='{o}'>{o}</option>" for o in options]
    footer = "</select>"
    return base + " ".join(choices) + footer
