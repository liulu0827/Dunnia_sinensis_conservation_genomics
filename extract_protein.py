#!/usr/bin/env python3

def read_protein_names(file_path):
    """读取包含蛋白质序列名称的文件"""
    protein_names = set()
    with open(file_path, 'r') as file:
        for line in file:
            protein_names.add(line.strip())
    return protein_names

def extract_protein_sequences(protein_names, fasta_file_path, output_file_path):
    """从FASTA文件中提取指定的蛋白质序列"""
    with open(fasta_file_path, 'r') as fasta_file, open(output_file_path, 'w') as output_file:
        write_flag = False
        for line in fasta_file:
            if line.startswith(">"):
                protein_id = line.split()[0][1:]
                if protein_id in protein_names:
                    write_flag = True
                    output_file.write(line)
                else:
                    write_flag = False
            elif write_flag:
                output_file.write(line)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python extract_proteins.py protein_names.txt proteins.fa output.fa")
        sys.exit(1)

    protein_names_file = sys.argv[1]
    fasta_file = sys.argv[2]
    output_file = sys.argv[3]

    protein_names = read_protein_names(protein_names_file)
    extract_protein_sequences(protein_names, fasta_file, output_file)
