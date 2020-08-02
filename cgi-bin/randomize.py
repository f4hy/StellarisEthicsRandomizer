import random
import hashlib


def generateRequiredEthic(empire_name, game_id):
    """Generate a fixed ethic from EMPIRE_NAME

    Given a name for your empire this will give you a required ethic. It is
    deterministic on the name so after discovery in game one can determine if
    the player obeyed the rule

    """
    ethics = {
        "Authoritarian": "https://stellaris.paradoxwikis.com/images/thumb/b/bf/Authoritarian.png/50px-Authoritarian.png",
        "Egalitarian": "https://stellaris.paradoxwikis.com/images/thumb/6/6a/Egalitarian.png/50px-Egalitarian.png",
        "Materialist": "https://stellaris.paradoxwikis.com/images/thumb/e/ef/Materialist.png/50px-Materialist.png",
        "Spiritualist": "https://stellaris.paradoxwikis.com/images/thumb/b/be/Spiritualist.png/50px-Spiritualist.png",
        "Militarist": "https://stellaris.paradoxwikis.com/images/thumb/4/44/Militarist.png/50px-Militarist.png",
        "Pacifist": "https://stellaris.paradoxwikis.com/images/thumb/4/4a/Pacifist.png/50px-Pacifist.png",
        "Xenophile": "https://stellaris.paradoxwikis.com/images/thumb/b/b0/Xenophile.png/50px-Xenophile.png",
        "Xenophobe": "https://stellaris.paradoxwikis.com/images/thumb/e/ed/Xenophobe.png/50px-Xenophobe.png",
    }
    # fanatic = [f"Fanatic {e}" for e in ethics]
    other = {
        "Hive Mind": "https://stellaris.paradoxwikis.com/images/4/43/Auth_hive_mind.png",
        "Machine Intelligence": "https://stellaris.paradoxwikis.com/images/a/af/Auth_machine_intelligence.png",
        "Corporate": "https://stellaris.paradoxwikis.com/images/1/18/Auth_corporate.png",
    }

    ethics.update(other)

    key = empire_name + game_id
    hashed = hashlib.sha256(key.encode()).hexdigest()
    random.seed(int(hashed, 16))
    required = random.choice(list(ethics.keys()))
    return hashed, required, ethics.get(required)
