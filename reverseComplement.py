#Python Problem 1
#reverseComplement.py
#Introduction to Bioinformatics Assignment 2
#Purpose: reverse complement of DNA sequence
#Your Name: Brian Franzone
#Date: 02/Oct/2014

from Bio.Seq import Seq

#s1 is the string you should use to generate a reverse complement sequence
s1 = Seq("AAAAACCCCCTCGGCTAATCGACTACTACTACTACTACTTCATCATCATCAGGGGGGGGCTCTCTCTAAAAACCCCTTTTGGGGG")

#Print the reverse complement sequence
print '%s' % s1.reverse_complement()