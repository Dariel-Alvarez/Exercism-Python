codon_aminoacids = {
        "AUG" : "Methionine",
        "UUU" : "Phenylalanine",
        "UUC" : "Phenylalanine", 
        "UUA" : "Leucine", 
        "UUG" : "Leucine", 
        "UCU" : "Serine", 
        "UCC" : "Serine", 
        "UCA" : "Serine", 
        "UCG" : "Serine", 
        "UAU" : "Tyrosine", 
        "UAC" : "Tyrosine", 
        "UGU" : "Cysteine", 
        "UGC" : "Cysteine", 
        "UGG" : "Tryptophan" 
        }

def proteins(strand):

    list_of_codons = []

    translated_array = []

    for i in range(0, len(strand), 3):
        list_of_codons.append(strand[i:i+3])
    
    for codon in list_of_codons:
        if codon == "UAA" or codon == "UAG" or codon == "UGA":
            break

        translated_array.append(codon_aminoacids[codon])

    return translated_array
        


# def translation(codon):
#     codon_aminoacids = {
#         "AUG" : "Methionine",
#         "UUU" : "Phenylalanine",
#         "UUC" : "Phenylalanine", 
#         "UUA" : "Leucine", 
#         "UUG" : "Leucine", 
#         "UCU" : "Serine", 
#         "UCC" : "Serine", 
#         "UCA" : "Serine", 
#         "UCG" : "Serine", 
#         "UAU" : "Tyrosine", 
#         "UAC" : "Tyrosine", 
#         "UGU" : "Cysteine", 
#         "UGC" : "Cysteine", 
#         "UGG" : "Tryptophan" 
#         }