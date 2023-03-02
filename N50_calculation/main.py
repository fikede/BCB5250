# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



import sys
from Bio import SeqIO

# print(len(sys.argv))
# print(str(sys.argv[1]))

fil = str(sys.argv[1])

sequences = []
lens = []
for record in SeqIO.parse(fil, "fasta"):
    sequences.append(record.seq)
    lens.append(len(record.seq))


# Calculate the total length of all contigs
total_contigs_length = sum(lens)
# Calculate the total number of contigs
num_contigs = len(sequences)
# Calculate the largest contig in terms of length
maxlen = max(lens)
N50 = 0

# Calculate N50
tot = 0
for l in lens:
    tot += l
    # print(l)
    if tot >= sum(lens)/2:
        N50 = l
        break

# print(num_contigs, total_contigs_length, maxlen, N50)
# print("Number of Contigs: ", num_contigs)
# print("Total length of contigs: ", total_contigs_length)
# print("Length of largest contig: ", maxlen)
# print("N50: ", N50)

# Write output to file report.txt
f = open("report.txt", "w")
f.write(f"Number of Contigs: {num_contigs}\n")
f.write(f"Total length of Contigs: {total_contigs_length}\n")
f.write(f"Length of largest Contig: {maxlen}\n")
f.write(f"N50: {N50}")

