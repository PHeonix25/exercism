# Hold the mapping in a static instance,
# rather than per-instantiation.
__dna_mapping__ = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }

def to_rna(dna_strand=''):
    """Converts a DNA strand to its matching RNA compliment."""
    return ''.join(__dna_mapping__.get(char, '') for char in dna_strand)
