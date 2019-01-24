def to_rna(dna_strand=''):
    """Converts a DNA strand to its matching RNA compliment."""
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))
