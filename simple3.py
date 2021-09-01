import random
grammar = dict( # A grammar for a trivial subset of English.
        S = [['NP','VP']],
        NP = [['Art', 'N']],
        VP = [['V', 'NP']],
        Art = ['the', 'a'],
        N = ['man', 'ball', 'woman', 'table'],
        V = ['hit', 'took', 'saw', 'liked'])

def generate(phrase):
    "Generate a random sentence or phrase"
    if isinstance(phrase, list): 
        return mappend(generate, phrase)
    elif phrase in grammar:
        return generate(random.choice(grammar[phrase]))
    else: return [phrase]
    
def generate_tree(phrase):
    """Generate a random sentence or phrase,
     with a complete parse tree."""
    if isinstance(phrase, list): 
        return map(generate_tree, phrase)
    elif phrase in grammar:
        return [phrase] + generate_tree(random.choice(grammar[phrase]))
    else: return [phrase]
    
def mappend(fn, iterable):
    """Append the results of calling fn on each element of iterbale.
    Like iterools.chain.from_iterable."""
    return sum(map(fn, iterable), [])
