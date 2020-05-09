import random
import hashlib


def generateRequiredEthic(empire_name, game_id):
    """Generate a fixed ethic from EMPIRE_NAME

    Given a name for your empire this will give you a required ethic. It is
    deterministic on the name so after discovery in game one can determine if
    the player obeyed the rule

    """
    ethics = [
        "Authoritarian",
        "Egalitarian",
        "Materialist",
        "Spiritualist",
        "Militarist",
        "Pacifist",
        "Xenophile",
        "Xenophobe",
    ]
    # fanatic = [f"Fanatic {e}" for e in ethics]
    other = ["Hive Mind", "Machine Intelligence", "Corporate"]

    all_choices = ethics + other

    key = empire_name + game_id
    hashed = hashlib.sha256(key.encode()).hexdigest()
    random.seed(int(hashed, 16))
    required = random.choice(all_choices)
    return hashed, required
