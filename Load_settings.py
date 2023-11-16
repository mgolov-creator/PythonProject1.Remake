saved_dict = {}
def load_settings():
    global saved_dict
    saved_dict = {}
    with open("savedsettings", "r") as file:
        strings_saved = file.readlines()
        for i in strings_saved:
            i.strip()
            j = (i.strip()).split(":")
            if j[1].isdigit():
                saved_dict[j[0]] = int(j[1])
            else:
                saved_dict[j[0]] = j[1]
    return saved_dict