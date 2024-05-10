def validate_pin(pin):
    # Check if the length of the PIN is either 4 or 6
    if len(pin) == 4 or len(pin) == 6:
        # Check if all characters in the PIN are digits
        if pin.isdigit():
            return True
    return False