def open_or_senior(data):
    categoriaztion = []
    for prospective_member in data:
        if prospective_member[0] >= 55 and prospective_member[1] > 7:
            categoriaztion.append("Senior")
        else:
            categoriaztion.append("Open")
    return categoriaztion