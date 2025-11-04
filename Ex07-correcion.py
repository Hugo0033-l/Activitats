def count_vocals(text:str):
    vocals = {"a":0, "e":0, "i":0, "o":0, "u":0}

    accents = str.maketrans(
        "àáäèéëíìïóòöúùü"
        "aaaeeeiiiooouuu"
    )

    text_format = text.lower().translate(accents)

    vocals["a"] = text_format.count("a")
    vocals["e"] = text_format.count("e")
    vocals["i"] = text_format.count("i")
    vocals["o"] = text_format.count("o")
    vocals["u"] = text_format.count("u")