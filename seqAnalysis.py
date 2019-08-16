"""Reading from the HIV-1 Reverse Transcript"""

#....This modules are needed for the program................
import os
import sys
import shutil

if __name__=="__main__":

#...This opens the file 'HIV-1 ReverseTranscriptaseSeq.txt' in a 'read' mode
	HIV = open(sys.argv[1], "r") 
	L=HIV.readlines()  #...List of 10 sequences from 'HIV' textfile in the readmode............
	
#....This prints out the list of commandlines..... 	
	print sys.argv
#.....This print out the second argument in the list	
	print sys.argv[1]
	
	i= 0      
	SEQ = []  #...This will contain all the sequences without the sequence names.........
	SEQ_names=[] #....This will contain the sequence names
	while i<=len(L)-1:
		if   L[i][0] ==">": #...This examine the first element '>' of all the sequence names
			SEQ_names.append(L[i])	#...all the sequence names are moved to SEQ_name list
			i = i+1
			str=''  #...This is for conversion to string

			while i<= len(L)-1 and L[i][0]!=">": 

#...This remove all the "\n" from the list and put each sequence(without names) into a string 			  
				str=str+L[i].rstrip()  
				i = i+1
			SEQ.append(str) #This moves all the strings into the SEQ list 	

#....This print out the length of the 'SEQ' List................
	print "The number N of DNA sequences is:%d" %(len(SEQ))
	
	for i in range(len(SEQ)-1):
		if len(SEQ[i])==len(SEQ[i+1]): #check if the length of the sequences
						#are equal
			continue          #if the are equal, the checking process continues
		else:			#otherwise the checking stops 
			break
	if i==len(SEQ)-2:
		print "same length and their coreesponding length is", len(SEQ[0])
	else:
		print"different length"
		
	
	Hamd = []	#this List will contain the hamming distance
	for i in range(len(SEQ)):
		A = []  #List will contain the count of different sequence parterns.
		for j in range(len(SEQ)):
			d = 0   #initial count
			
#This make comparisons in the pattern of sequences in the list 'SEQ'			
			for k in range(len(SEQ[i])):
				if SEQ[i][k]!=SEQ[j][k]: #This check for the hamming condition
					d = d+1
			A.append(d) #values 'd' move to List A
		Hamd.append(A)  #....this append A to Hamd List
	print Hamd
	
	M = open('matrix.csv','w') #This is the matrix of Hmd stored in 'csv' format
	for i in range(len(Hamd)): 
		M.write('%s' %Hamd[i]+'\n') #writing the Matrix of Hmd List
			
#this create the Temporary folder(TmpFolder) to store files 'seq_i' files			
	os.mkdir("tmpFolder") 
	for i in range(len(SEQ)):
		P=open("seq-%d.txt"%i, "w") 
		P.writelines(SEQ_names[i]+'\n'+SEQ[i]) #This write each sequence i 'seq_i' files
		shutil.move("seq-%d.txt"%i, "tmpFolder") #This move all 'seq_i' to TmpFolder
	M.close() 	#this close the openned file 'M'

	HIV.close() #this close the openned file 'HIV'
