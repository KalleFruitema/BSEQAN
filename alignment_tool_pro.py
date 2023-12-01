from Bio import Align, SeqIO
from pprint import pprint


def align_all_seqs(file, outfile: str=''):
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = Align.substitution_matrices.load("BLOSUM80")
    aligner.mode = "local"
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -1

    seqs = []
    for seq_record in SeqIO.parse(file, "fasta"):
        seqs.append(seq_record)

    file_content = ''
    align_dict = {}
    for seq1 in seqs:
        align_dict.update({
            seq1.description: {}
        })
        for seq2 in seqs:
            score = aligner.score(seq1.upper(), seq2.upper())
            align_dict[seq1.description].update({
                seq2.description: score
            })
            if outfile:
                if f"{seq1.description}\n{seq2.description}" not in file_content and\
                f"{seq2.description}\n{seq1.description}" not in file_content:
                    alignments = aligner.align(seq1.upper(), seq2.upper())
                    file_content += (f"{seq1.description}\n{seq2.description}\n"
                                    f"{list(alignments)[0]}\n\n")
    if outfile:
        with open(outfile, 'w') as alignment_file:
            alignment_file.write(file_content)
    # pprint(align_dict, sort_dicts=False)
    return align_dict

    
def calculate_distances(align_dict: dict, outfile=""):
    distance_dict = {}
    for head1, sequence_dict in align_dict.items():
        distance_dict.update({
            head1: {}
        })
        for head2, score in sequence_dict.items():
            distance = (1 - score / align_dict[head1][head1]) * (1 - score / align_dict[head2][head2])
            distance_dict[head1].update({
                head2: distance
            })

    if outfile:
        csv_fmt = ("," + ",".join(list(distance_dict.keys())) + "\n" + 
                   "\n".join([','.join([key, *[str(score) 
                                               for score in list(val.values())]])
                              for key, val in distance_dict.items()]))

        with open(outfile, "w") as file:
            file.write(csv_fmt)
    return distance_dict


def main():
    align_dict = align_all_seqs("tests/opdracht_seqs.fa")
    align_dict = align_all_seqs("tests/opdracht_seqs_namen.fa",
                                outfile="tests/alignments_pro.txt")
    distance_dict = calculate_distances(align_dict)
                                        # outfile="tests/pro_distmatrix.csv")


if __name__ == "__main__":
    main()
