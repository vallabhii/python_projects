def electronic_configuration(Z):
    orbitals = [
        ("1s", 2),
        ("2s", 2),
        ("2p", 6),
        ("3s", 2),
        ("3p", 6),
        ("4s", 2),
        ("3d", 10),
        ("4p", 6),
        ("5s", 2),
        ("4d", 10),
        ("5p", 6),
        ("6s", 2),
        ("4f", 14),
        ("5d", 10),
        ("6p", 6),
        ("7s", 2),
        ("5f", 14),
        ("6d", 10),
        ("7p", 6)
    ]
    config = []
    remaining = Z
    for i, (orbital, capacity) in enumerate(orbitals):
        if remaining <= 0:
            break
        electrons = min(remaining, capacity)
        config.append([orbital, electrons, capacity])
        remaining -= electrons
    for i in range(len(config)):
        orb, e, cap = config[i]
        if "d" in orb:
            if e == 4 or e == 9:
                for j in range(i - 1, -1, -1):
                    if "s" in config[j][0] and config[j][1] > 0:
                        config[j][1] -= 1
                        config[i][1] += 1
                        break
        if "f" in orb:
            if e == 6 or e == 13:
                for j in range(i - 1, -1, -1):
                    if "s" in config[j][0] and config[j][1] > 0:
                        config[j][1] -= 1
                        config[i][1] += 1
                        break
    result = []
    for orb, e, _ in config:
        if e > 0:
            result.append(f"{orb}^{e}")
    return " ".join(result)

a=True
print("This program finds the electronic configuration of any given element!")
while a==True:
    Z = int(input("Enter atomic number of the element: "))
    if Z<1 or Z>118:
        print("Element with this atomic number does not exist.")
    else:
        print(electronic_configuration(Z))
    while True:
        print("Would you like to check the configuration for another element?")
        play=input("Enter \"y\" for yes and \"n\" for no: ")
        if play=="y":
            break
        elif play=="n":
            print("Thank you for using the electronic configuration calculator!")
            a=False
            break
        else:
            print("Please enter a valid response.")
