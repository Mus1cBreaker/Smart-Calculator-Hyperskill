def check_email(string):
    if " " in string:
        return False
    if "@" in string and "@." not in string and string.find("@") < string.rfind("."):
        return True
    return False
