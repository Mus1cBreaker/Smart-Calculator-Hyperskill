def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return "I " + instructions[len("Simon says") + 1:]
    if instructions.endswith("Simon says"):
        return "I " + instructions[:instructions.index("Simon says") - 1]
    return "I won't do it!"

