def score(age):
    try:
        if 18 <= age < 25:
            return 18
        elif 25 <= age < 45:
            return 16
        elif 45 <= age < 100:
            return 20
        else:
            return -1
    except Exception:
        return -1
