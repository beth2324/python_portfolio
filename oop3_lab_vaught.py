#!/usr/bin/env python
# Name: beth vaught
# Email: evaught@uncc.edu
# OOP Lab 3
# 3/27/2024
"""
detailed justification for how I chose to structure my classes:

Should the method for converting the file information be an instance, class, or static method?
    - it should be an instance method because it will be applied to all instances individually in the class
Does it make sense to create FileSequenceReader objects?
    - yes it does make sense to create file sequence reader objects
    - it allows for the process of making other objects to be automated from each file
    - it allows for the generator object that it makes to be given a name
If so, will it need instance variables?
    - yes each file will be an instance
    - we will need to output the generator from these instances
Does this class need class variables? What would those be?
    - no there arent any overarching aspects of the class
would any class or static methods would be helpful?
    - no becuase each instance will be completely different due to the file 
Should any of your other methods be a part of this class instead of where you originally wrote them?
    - yes the sequence bases test for dna can be moved to assign sequences as dna or protein
"""
#class FileSequenceReader
class FileSequenceReader:
    def __init__(self,file):
        self.file=file
    #control how FASTA (and other format) files are read and converted into our SequenceRecord objects
    def fastaParser(self):
        with open(self.file) as file_op:
            #make variables to store info before yeild
            header = None
            bases = ""
            #go through each line
            for line in file_op:
                #isolate header or data
                line = line.strip()
                if line.startswith(">"):
                    header = line.lstrip(">")
                else:
                    bases += line.strip()
                    #ensure correct bases only
                    #save header with sequence as record
                    for base in bases:
                        if base in "ATGC":
                            dna_check=1
                        else:
                            dna_check=0
                            break
                    if dna_check==1:
                        yield sequenceRecord(header,dna(bases))
                    else:
                        yield sequenceRecord(header,protein(bases))
                    #empty sequence variable
                    bases = ""
    def __str__(self):
        for x in self.fastaParser(self.file):
            return f"\nThe first record from the file is:\n{x}\n"
    def __repr__(self):
        output=""
        for x in self.fastaParser(self.file):
            output+="\n"+str(x)
        return output
"""
how to use the classes to read a FASTA file step by step
    - make an instance of each file with filesequencereader class
    - class method fastaParser will make generator object of sequence records
    - use for loop to go through data output by object_name.fastaParser()
    - objects can then be compared and used with their own methods and attributes
describe the objects' attributes and methods and uses
    - file sequence reader
        - attribute: file name
        - method: fastaParser - outputs generator of file sequence records objects
            - chooses type of sequence object in record based on base values
        - method: str - outputs preview of first sequence record of the file without any method calls
        - method: repr - outputs all of sequence records of file
    - sequence record
        - attribute: label - name of sequence
        - attribute: seq - all bases in the sequence, ensures that this is a sequence object
        - method: str - outputs label and seq in format "label:seq" when object is called
        - method: repr - outputs label and seq in tuple format (label,seq)
    - sequence
        - attribute: bases - all bases in the sequence
        - method: repr - outputs all bases in sequence when called
        - method: add - defines addition of sequences to be concating sequences together
        - method: len - defines length measure of sequences to be number of bases in sequence
    - dna(sequence)
        - inherits sequence methods and attributes
        - method: translate - converts sequence in to protein sequence
        - method: str - prints information about percentage of protien coding dna
        - method: eq - declares measure of equality of dna objects is based on percentage of protien coding dna
        - method: lt - declares measure of less than comparability of dna objects is based on percentage of protien coding dna
    - protien(sequence)
        - inherits sequence methods and attributes
        - method: str - prints preview of sequence
        - method: eq - measures equality of protein sequences by length of sequence
        - method: lt - measures less than comparability of protein sequences by length of sequence
"""
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

#dictionary to help facilitate DNA translation:
aa_dict = {'M':['ATG'], 'F':['TTT', 'TTC'], 'L':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'C':['TGT', 'TGC'], 'Y':['TAC', 'TAT'], 'W':['TGG'], 'P':['CCT', 'CCC', 'CCA', 'CCG'], 'H':['CAT', 'CAC'],
'Q':['CAA', 'CAG'], 'R':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'I':['ATT', 'ATC', 'ATA'], 'T':['ACT', 'ACC', 'ACA', 'ACG'],
'N':['AAT', 'AAC'], 'K':['AAA', 'AAG'], 'S':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'V':['GTT', 'GTC', 'GTA', 'GTG'],
'A':['GCT', 'GCC', 'GCA', 'GCG'], 'D':['GAT', 'GAC'], 'E':['GAA', 'GAG'], 'G':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}
#subclass DNA
class dna(sequence):
    def __init__(self,bases):
         self.bases=bases
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

#test the classes
# type file name and, if needed, file location path here:
path = ""
filename="homemade_records.fasta"
name=path+filename
file_info = FileSequenceReader(name)
for output in file_info.fastaParser():
    print(output.label)
    print(output.seq)



"""
*THE REST IS NOT PART OF THIS LAB
--------------------------------------------------------------------------------------------------------------------
LAST WEEK'S WORK DESCRIPTION - provided now due to failure to submit lab work within allocated time last week
Plan:
Enforce sequence appearances 
- check for letters other than atgc with comprehension and condition
- override str and repr if needed
common elements:
- Sequences - parent class
    -  it is only a consistent line of letters
    - can measure total length and compare based on length
- DNA Sequence
    - limited to ATCG letters *edited to have letters test in RileSequenceReader class
    - can be evaluated and compared by number of protein coding triplets
- Protein Sequence
    - not limited to ATGC
    - does not need to be evaluated for number of triplets
"""