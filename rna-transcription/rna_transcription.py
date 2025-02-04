def to_rna(dna_strand):
    translator = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(translator)