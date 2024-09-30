#Elizabeth Vaught
#evaught@uncc.edu
#comprehensions lab


#3.1) gc calculator function
def gc_count(dna):
	return float((dna.count("G")+dna.count("C"))/len(dna))

#4.1) function that will return the number of unique vowels in a string
def vowel_count(string):
	vowel_num=len([x for x in set(string) if x.upper() in "AEIOU"])
	return vowel_num

#5.1) return complement of base given base
def complement(base):
	if base.upper()=="A":
		return "T"
	elif base.upper()=="T":
		return "A"
	elif base.upper()=="C":
		return "G"
	else:
		return "C"

#Test and show results
def main():

	#information given for testing comprehensions
	seq = "ATGNAZCGA"
	d1 = {'seq1':"ATCGA", 'seq2':"GCAGTA", 'seq3':"GCGCGCCGCGCTGACATCGA"}
	passage = "Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore— While I nodded, nearly napping, suddenly there came a tapping, As of some one gently rapping, rapping at my chamber door. “’Tis some visitor,” I muttered, “tapping at my chamber door— Only this and nothing more.”"
	min_vowel=3
	min_seq_length=7


	#1)comprehension to filter invalid bases (not ATGC) from a sequence
	seq2="".join([x for x in seq if x in "ATGC"])
	print(f"\n1) {seq} has been filtered to {seq2}")


	#2) generator comprehension that will yield sequences longer than a certain number from dictionary of header:sequence
	longer_than_seqs=(seq for header,seq in d1.items() if len(seq)>min_seq_length)
	print("\n Sequences to analyze:")
	for name,seq in d1.items():
		print(" - "+ name+" : "+seq)
	print(f"\n2) Sequences with length greater than minimum of {min_seq_length}:")
	for seq in longer_than_seqs:
		print(" - "+seq)


	#3) comprehension that will create a list of sequences with GC Content higher than 45% from dictionary of header:sequence
	high_gc_seqs=[seq for header,seq in d1.items() if gc_count(seq.upper())>0.45]
	print(f"\n3) Sequences containing more than 45% G and C:")
	for seq in high_gc_seqs:
		print(f" - {seq}")

	#4.2) comprehension that will build a list of words in given passage that contain at least 3 unique vowels
	#alternatively use .replace("'","") to replace with nothing if strip doesnt work
	words=[word for word in passage.strip(",").strip("—").strip("”").strip("“").strip("’").split() if vowel_count(word)>=min_vowel]
	print(f"\nPassage to analyze: \n{passage}")
	print(f"\n4) Words with at least {min_vowel} vowels:")
	for word in words:
		print(" - "+word)

	#5) comprehension that generates the reverse complement of a sequence. ex:"ATCGACGA" -> 'TCGTCGAT'
	#use rev function
	reverse_comp="".join([complement(base) for base in (seq2[::-1])])
	print(f"\n5) The reverse complement of {seq2} is {reverse_comp}\n")

if __name__ == '__main__':
	main()