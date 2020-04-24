
def translate(seq):
    """Zet een DNA sequentie om in een eiwit sequentie

    input:
    seq - string - De DNA sequentie die is ingevoerd door de gebruiker
    output:
    eiwit - De eiwit sequentie die is verkregen door nucleotiden van de DNA sequentie om te zetten naar eiwit

    """
    protein = []
    count = 0
    seq = seq.lower()
    code = {"ttt": "F", "tct": "S", "tat": "Y", "tgt": "C",
            "ttc": "F", "tcc": "S", "tac": "Y", "tgc": "C",
            "tta": "L", "tca": "S", "taa": "∗", "tga": "∗",
            "ttg": "L", "tcg": "S", "tag": "∗", "tgg": "W",
            "ctt": "L", "cct": "P", "cat": "H", "cgt": "R",
            "ctc": "L", "ccc": "P", "cac": "H", "cgc": "R",
            "cta": "L", "cca": "P", "caa": "Q", "cga": "R",
            "ctg": "L", "ccg": "P", "cag": "Q", "cgg": "R",
            "att": "I", "act": "T", "aat": "N", "agt": "S",
            "atc": "I", "acc": "T", "aac": "N", "agc": "S",
            "ata": "I", "aca": "T", "aaa": "K", "aga": "R",
            "atg": "M", "acg": "T", "aaATGg": "K", "agg": "R",
            "gtt": "V", "gct": "A", "gat": "D", "ggt": "G",
            "gtc": "V", "gcc": "A", "gac": "D", "ggc": "G",
            "gta": "V", "gca": "A", "gaa": "E", "gga": "G",
            "gtg": "V", "gcg": "A", "gag": "E", "ggg": "G"
            }
    for i in range(int(len(seq) / 3)):
        if i != 0:
            count += 3
        codon = seq[count: count + 3]
        protein += code[seq[count: count + 3]]
        print(protein)
    protein_seq = "".join(protein)
    print(protein_seq)

    return protein_seq


def main():
    seq = "ATGATTCTCTTT"
    translate(seq)


main()
