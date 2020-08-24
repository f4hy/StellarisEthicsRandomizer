MaxAI = {"tiny": 6, "small": 12, "medium": 18, "large": 24}
MaxFallen = {"tiny": 1, "small": 2, "medium": 3, "large": 4}
MaxMarauder = {"tiny": 1, "small": 2, "medium": 2, "large": 3}


DIFFICULTY_SETTINGS = {"Captain", "Commodore", "Admiral", "Grand Admiral"}
def difficulties():
    options = []
    for i in DIFFICULTY_SETTINGS:
        options.append(i)
        options.append(i + "- Scaling")
    return options


def get_ranges(size):
    def arange(start, end, inc):
        i = start
        values = [start]
        while i < end:
            i += inc
            values.append(i)
        return values

    def percents(inc):
        vals = arange(0.0, 1.0, inc)
        return [f"{100*i:.0f}% of max" for i in vals if i <= 1]

    ranges = {
        "Galaxy Size": ["Tiny: 200 stars", "Small: 400 Stars", "Medium: 600 Stars"],
        "Galaxy Shape": ["Elliptical", "Spiral", "Ring"],
        f"AI empires (max:{MaxAI})": percents(1.0 / 12.0),
        f"Advanced AI starts (max:{MaxAI})": percents(1.0 / 12.0),
        f"Fallen Empires: (max:{MaxFallen})": (range(0, MaxFallen[size] + 1)),
        f"Marauder Empires: (max:{MaxMarauder})": (range(0, MaxMarauder[size] + 1)),
        "Tech/ Tradition cost": arange(0.25, 5.0, 0.25),
        "Habitable Worlds": arange(0.25, 5.0, 0.25),
        "Primitive Civilizations": arange(0.0, 5.0, 0.25),
        "Crisis Strength": (arange(0.0, 5.0, 0.25)) + [10, 25],
        "Mid-Game Start Year (deafult: 2300)": (range(2225, 2325 + 1, 25)),
        "End-Game Start Year (default: 2400)": (range(2250, 3000 + 1, 25)),
        "Victory Year (default 2500)": (range(2450, 3200 + 1, 25)),
        "AI Aggressiveness": ["low", "normal", "high"],
        "Empire Placement": [
            "Random",
            "Distributed Players",
            "Clustered Players",
            "Clusters",
        ],
        "Advanced Neighbors": ["off", "on"],
        "Hyperlane Density": (arange(0.5, 2.76, 0.25)) + ["full"],
        "Abandoned Gateways": arange(0.0, 5.0, 0.25),
        "Wormhole Pairs": arange(0.0, 5.0, 0.25),
        "Guaranteed Habitable Worlds": [0, 1, 2],
        "Caravaneers": ["off", "on"],
        "Difficulty": difficulties(),
        "Randomize Ethics": ["off"],
    }
    return ranges
