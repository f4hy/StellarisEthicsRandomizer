from collections import Counter
from stellarisrandomizer.ranges import get_ranges
import random
import json


def vote_resolver(votes):
    print("votes", votes)
    c = Counter()
    for v in votes:
        c.update(v)
    if len(c) == 0:
        # no votes so return None
        return ("No Votes", [])
    _top, mostfrequent = c.most_common(1)[0]
    top_choices = [i for i, c in c.most_common(len(votes)) if c == mostfrequent]
    return (random.choice(top_choices), top_choices)


def game_vote_aggregator(jsons):
    keys = list(get_ranges("medium").keys())
    random.seed(json.dumps(jsons), version=2)

    selected = {}
    for k in keys:
        votes = [j.get(k, None) for j in jsons]
        selected[k] = vote_resolver(votes)
    return selected
