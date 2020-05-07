#!/usr/bin/env python
import sys
import copy

# This scripts works with a multiple sequence alignment in PHYLIP format

def read(path):
    with open(path, "r") as file:
        content = file.readlines()
        names = []
        seqs = []
        for line in content:
            name, seq = line.strip("\n").split()
            names.append(name)
            seqs.append(seq)
        seqs_temp = copy.copy(seqs)
        name_counter_1 = 0
        for seq_1 in seqs:
            name_counter_2 = copy.copy(name_counter_1)
            for seq_2 in seqs_temp:
                denominator = len(seq_1)
                numerator = 0
                counter = 0
                seq_1 = list(seq_1)
                seq_2 = list(seq_2)
                for s in seq_1:
                    if s == '?' or s == 'N' or seq_2[counter] == '?' or seq_2[counter] == 'N':
                        denominator -= 1
                    else:
                        if s != seq_2[counter]:
                            numerator += 1
                    counter += 1

                if denominator == 0:
                    number = 1
                else:
                    number = float(numerator)/denominator
                    if number == 0:
                        number = 0
                print names[name_counter_1]+'   '+names[name_counter_2]+'   '+str(number)

                name_counter_2 += 1

            name_counter_1 += 1
            seqs_temp.pop(0)


if __name__ == '__main__':
    try:
        path = sys.argv[1]
        read(path)
    except Exception, e:
        print e
        print '[Error] invalid file path, for example: python comparasion.py names.txt'
