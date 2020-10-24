def countingValleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == "D":
            level -= 1
        if step == "U":
            level += 1
        if level == 0 and step == 'U':
            valleys += 1