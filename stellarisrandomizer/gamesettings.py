import numpy as np

MaxAI = {"tiny": 6, "small": 12, "medium": 18, "large": 24}
MaxFallen = {"tiny": 1, "small": 2, "medium": 3, "large": 4}
MaxMarauder = {"tiny": 1, "small": 2, "medium": 2, "large": 3}


def get_ranges(size):

    ranges = {
        "AI empires": list(range(0, MaxAI[size])),
        "Advanced AI starts": list(range(0, MaxAI[size])),
        "Fallen Empires": list(range(0, MaxFallen[size])),
        "Marauder Empires": list(range(0, MaxMarauder[size])),
        "Tech/ Tradition cost": np.arange(0.25, 5.01, 0.25),
        "Habitable Worlds": np.arange(0.25, 5.01, 0.25),
        "Primitive Civilizations": np.arange(0.0, 5.01, 0.25),
        "Crisis Strength": list(np.arange(0.0, 5.01, 0.25)) + [10, 25],
        "Mid-Game Start Year": list(range(2225, 2325, 25)),
        "End-Game Start Year": list(range(2250, 3000, 25)),
        "Victory Year": list(range(2450, 3200, 25)),
        "AI Aggressiveness": ["low", "normal", "high"],
        "Empire Placement": [
            "Random",
            "Distributed Players",
            "Clustered Players",
            "Clusters",
        ],
        "Advanced Neighbors": ["off", "on"],
        "Hyperlane Density": list(np.arange(0.5, 2.76, 0.25)) + ["full"],
        "Abandoned Gateways": np.arange(0.0, 5.01, 0.25),
        "Wormhole Pairs": np.arange(0.0, 5.01, 0.25),
        "Guaranteed Habitable Worlds": [0, 1, 2],
        "Caravaneers": ["off", "on"],
    }
    return ranges
