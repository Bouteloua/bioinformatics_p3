#Python Problem 2
#hamming.py
#Introduction to Bioinformatics Assignment 2
#Purpose: If the minimem number of chnage
#Your Name: Brian Franzone
#Date: Oct 2, 2014

def main():
	#stores 3 database sequences
	seqList = ["AGGATACAGCGGCTTCTGCGCGACAAATAAGAGCTCCTTGTAAAGCGCCAAAAAAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGGCCCCGGGAGCGGAGAGCGAGGGGAGGCAGATTCGGAGGAAGGTCTGAAAAG",
	           "AAAATACAGGGGGTTCTGCGCGACTTATGGGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCACAGACTATGGCAGCAGCGTTGGCCCGGCAAAAGGAGCGGAGAGCGAGGGGAGGCGGAGACGGACGAAGGTCTGAGCAG",
	           "CCCATACAGCCGCTCCTCCGCGACTTATAAGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGCCCAAAACAGCGGAGAGCGAGGGGAGGCGGAGACGGAGGAAGGTCTGAGCAG"]

	#your query sequence
	s1 = "AGGATACAGCGGCTTCTGCGCGACTTATAAGAGCTCCTTGTGCGGCGCCATTTTAAGCCTCTCGGTCTGTGGCAGCAGCGTTGGCCCGGCCCCGGGAGCGGAGAGCGAGGGGAGGCGGAGACGGAGGAAGGTCTGAGGAG"

	for index, i in enumerate(seqList):
		#Results
		print "The hamming counter in string %i: %s" % (index + 1, hammingCounter(i, s1))


#Count the number char changes in list of the same lenght 
def hammingCounter(list_str, input_str):
	counter = 0
	for index, (char_list, char_input) in enumerate(zip(list_str, input_str)):
		if char_list != char_input:
			counter += 1
	return counter

if __name__ == '__main__':
  main()