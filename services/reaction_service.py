from data.reactions import REACTIONS

def get_reactions(category):

    return REACTIONS.get(
        category,
        REACTIONS["default"]
    )
