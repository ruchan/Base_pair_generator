from sys import argv
from os.path import exists



print ">>>>> Base Pair restraint file generator for PHENIX"
print ">>>>> Currently this does not check if a previous restraint file is present."
print ">>>>> Any restraint file in this directory will be written-over!!!"
#if exists(secondary_restraints.txt):
#	print "Your previous restraint file will be overwritten. Would you like to continue?"
#	choice = raw_input("y/N? ")
#	if choice == 'y':
#		base_pair()
#	else:
#		exit()
#else:
#	base_pair()

text = open('secondary_restraints.txt', 'w')
text.write('# These parameters are suitable for use in phenix.refine.\nrefinement.secondary_structure {\n  nucleic_acids {')


def base_pair():
	bp1 = raw_input("First base? ")
	bp2 = raw_input("Second base? ")
	while True:
		if bp1[0].upper() == "A" and bp2[0].upper() == "U" or bp1[0].upper() == "U" and bp2[0].upper() == "A":
			saenger_class = "XIX"
		elif bp1[0].upper() == "G" and bp2[0].upper() == "C" or bp1[0].upper() == "C" and bp2[0].upper() == "G":
			saenger_class = "XX"
		elif bp1[0].upper() == "G" and bp2[0].upper() == "U" or bp1[0].upper() == "U" and bp2[0].upper() == "G":
			saenger_class = "XXVIII"
		elif bp1 == "exit":
			text.write("\n\t}\n}")
			text.close()
			print "Thanks for using this script!"
			exit()
		else:
			print "I'm sorry, could you try that again.'"
			base_pair()
		text.write('\n\tbase_pair {\n\tbase1 = "chain \"A\" and resseq  %s"\n\tbase2 = "chain \"A\" and resseq  %s"\n\tsaenger_class = "%s"\n\t}' % (bp1[1:], bp2[1:], saenger_class))
		base_pair()
#	text.write('\tbase_pair {\n\tbase1 = "chain \"A\" and resseq  %s"\n\tbase2 = "chain \"A\" and resseq  %s"\n\tsaenger_class = "%s"\n\t}' % (bp1, bp2, saenger_class))



base_pair()
