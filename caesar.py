def main():
    dict = {"a": 1, 
            "b": 2, 
            "c": 3, 
            "d": 4, 
            "e": 5, 
            "f": 6, 
            "g": 7, 
            "h": 8, 
            "i": 9, 
            "j": 10, 
            "k": 11, 
            "l": 12, 
            "m": 13, 
            "n": 14, 
            "o": 15, 
            "p": 16, 
            "q": 17, 
            "r": 18, 
            "s": 19, 
            "t": 20, 
            "u": 21, 
            "v": 22, 
            "w": 23, 
            "x": 24, 
            "y": 25, 
            "z": 26 }
    text = input("Enter Text(Lowercase): ").lower().strip()
    key = int(input("Shift By: "))
    shift = (key % 26)
    key_list = list(dict.keys())
    val_list = list(dict.values())
    print("Your Cipher Text: ", end="")
    for i in text:
        try:
            a = (dict[i] + shift)
            if a > 26:
                a = a % 26
            position = val_list.index(a)
            print(key_list[position], end="")
        except KeyError:
            print(" ",end="")

if __name__ == "__main__":
    main()