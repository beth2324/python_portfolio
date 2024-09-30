#!/usr/bin/env python
# Name: beth vaught
# Email: evaught@uncc.edu
"""
Plan:
Enforce sequence appearances 
- check for letters other than atgc with comprehension and condition
- override str and repr if needed
common elements:
- Sequences - parent class
    -  it is only a consistent line of letters
    - can measure total length and compare based on length
- DNA Sequence
    - limited to ATCG letters
    - can be evaluated and compared by number of protein coding triplets
- Protein Sequence
    - not limited to ATGC
    - does not need to be evaluated for number of triplets
"""
#dictionary to help facilitate DNA translation:
aa_dict = {'M':['ATG'], 'F':['TTT', 'TTC'], 'L':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'C':['TGT', 'TGC'], 'Y':['TAC', 'TAT'], 'W':['TGG'], 'P':['CCT', 'CCC', 'CCA', 'CCG'], 'H':['CAT', 'CAC'],
'Q':['CAA', 'CAG'], 'R':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'I':['ATT', 'ATC', 'ATA'], 'T':['ACT', 'ACC', 'ACA', 'ACG'],
'N':['AAT', 'AAC'], 'K':['AAA', 'AAG'], 'S':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'V':['GTT', 'GTC', 'GTA', 'GTG'],
'A':['GCT', 'GCC', 'GCA', 'GCG'], 'D':['GAT', 'GAC'], 'E':['GAA', 'GAG'], 'G':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}

class sequence:
    # define one attribute - string that represents a DNA Sequence
    def __init__(self,bases):
        self.bases= bases    
    #define formal value to be used called with repr
    def __repr__(self):
        return self.bases
    #define how to add sequences together
    def __add__(self,other):
        self.bases += other.bases
        return self.bases
    #define how to measure length of sequence
    def __len__(self):
        return len(self.bases)

#subclass DNA
class dna(sequence):
    def __init__(self,bases):
        for base in bases:
            if base in "ATGC":
                self.bases=bases
            else:
                raise ValueError("DNA sequences may only contain 'A','G','C', or 'T'. Try protein sequence class or fix the mutation.")
    #translate sequence into protein sequence
    def translate(self):
        #convert sequence string into codons list
        max=len(self.bases)
        triplets=[]
        seq=self.bases
        for start in range(0,max,3):
            triplets.append(seq[start:start+3])
        #make protien code
        protein_sequence=""
        #loop through dictionary
        for p_base,codon_options in aa_dict.items():
            #loop through each protein code list of codons
            for codon in codon_options:
                #loop through bases that have been grouped into codons and test if codon
                for group in triplets:
                     if group==codon:
                        #save protein code
                        protein_sequence+="".join(p_base)
                        #move on to the next protein base option and its list
        return protein_sequence
    # define casual printing output
    def __str__(self):
        return f"Fraction of protein coding dna: {(len(self.translate())*3)/len(self.bases)}"
    # define how to compare if sequences are equal
    def __eq__(self,other):
        if (len(self.translate())*3)/len(self.bases)==(len(other.translate())*3)/len(other.bases):
            return True
        else:
            return False
    #define how to compare if sequences are less or greater
    def __lt__(self,other):
        if (len(self.translate())*3)/len(self.bases)<=(len(other.translate())*3)/len(other.bases):
            return True
        else:
            return False

#subclass Protein
class protein(sequence):
    def __init__(self,bases):
        self.bases = bases
        # define casual printing output
    def __str__(self):
        return f"Protein sequence preview: {self.bases[0:10]}"
    # define how to compare if sequences are equal
    def __eq__(self,other):
        if len(self.bases)==len(other.bases):
            return True
        else:
            return False
    #define how to compare if sequences are less or greater
    def __lt__(self,other):
        if len(self.bases)<=len(other.bases):
            return True
        else:
            return False

class sequenceRecord: 
    # two attributes - label (FASTA file header line) and sequence 
    def __init__(self,label,seq):
        self.label = label
        # confirm second attribute is a sequence with isinstance(object,type)
        if isinstance(seq,sequence):
            #bypass the str output of the sequence
            self.seq = repr(seq) #seq.bases could also be used
        else:
            raise TypeError ("information does not contain a sequence")
    # also add a __str__ and __repr__ method
    def __str__(self):
        return(f"{self.label}: {self.seq}")
    def __repr__(self):
        return (self.label,self.seq)

#testing
pig=dna("ATGCGTCATTCGCGGGTTTTTT")
cow=dna("GCGCG")
cat=protein("GHTGHSHSDKFCTCT")
mouse=protein("AGTC")
farm=sequenceRecord("dna",pig)
farm2=sequenceRecord("protein",cat)
print(farm,farm2)
"""
# type file name and, if needed, location path here
path = ""
filename="homemade_records.fasta"

#parse through fasta file
def fastaParser(file):
	#open file
	with open(file) as file_op:
		#make variables to store info before yeild
		header = None
		bases = ""
		#go through each line
		for line in file_op:
			#get rid of space on ends of line
			line = line.strip()
			#save if header
			if line.startswith(">"):
				header = line.lstrip(">")
			#save as sequence if not header
			else:
				bases += line.strip()
				#output header with sequence
				yield (header,bases)
				#empty sequence variable
				bases = ""
def main():
    #name future records
    val1,val2,val3=("","","")
    #call parsing of file
    for i,total in enumerate(fastaParser(path+filename)):
        name,info=total
        if i==0:
            val1=sequenceRecord(name,sequence(info))
        elif i==1:
            val2=sequenceRecord(name,sequence(info))
        else:
             val3=sequenceRecord(name,sequence(info))
if __name__ == '__main__':
    main()
"""