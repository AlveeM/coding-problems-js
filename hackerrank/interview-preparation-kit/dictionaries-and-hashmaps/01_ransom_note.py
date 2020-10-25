from collections import Counter

def checkMagazine(magazine, note):
    if len(note) > len(magazine):
        print("No")
        return
    
    mag_dict = Counter(magazine)
    note_dict = Counter(note)

    for key in note_dict:
        if key not in mag_dict or mag_dict[key] < note_dict[key]:
            print("No")
            return

    print("Yes")
    return