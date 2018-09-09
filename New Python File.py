easy="Life  is A __1__ Complex Organisation of  biomolecules  that Expresses ItselfThrough,__2__ Reactions  which lead to __3__  and adaptation for growth & __4__ ,to be able to __5__  and evolve with time for the continuity of life"

medium="A __1__ or __2__ organelle in the cytoplasm of nearly all __3__ cells, containing __4__ material and many enzymes important for cell metabolism, including those responsible for the conversion of food to usable energy. It consists of two membranes: an outer smooth membrane and an inner membrane arranged to form __4__."



hard=" an extremely long macromolecule that is the main component of __1__ and is the material that transfers genetic characteristics in all life forms, constructed of two __2__ strands coiled around each other in a ladderlike arrangement with the sidepieces composed of alternating phosphate and deoxyribose units and the rungs composed of the __3__ and __4__ bases adenine, __5__, cytosine, and thymine: the genetic information of DNA is encoded in the sequence of the bases and is transcribed as the strands unwind and replicate"

difficulty=raw_input("select difficulty:easy,medium,hard-")#takes in input and shows question accordingly using if 

def questionselector(difficulty):   #selects questions on basis of what user wants to answer
  if difficulty=="easy":
    return easy
  elif difficulty=="medium":
    return medium
  else:
    return hard
print questionselector(difficulty)
queslist=[easy,medium,hard]
answer_list1=["unique","chemical","responsiveness","devlopment","reproduce"]    
answer_list2=["spherical","elongated","eukaryotic","genetic","cristae"]     
answer_list3=["chromosome","nucleotides","purines","pyrimidine","guanine"]   
listoflists=[answer_list1,answer_list2,answer_list3]
difflist=["easy","medium","hard"]
blankslist=["__1__","__2__","__3__","__4__","__5__"]

def anscheck():                             #checks answers 
  global index                              #keeps count of where to check answer
  index=0
  while index<len(difflist):                #this loop slects the answer list according to the                                        #question
    if difficulty==difflist[index]:
      global answerlist
      answerlist=listoflists[index]        #gives the value of correct answer list to                                                 answerlistvarable 
      global xs                             #takes users answer
      xs=raw_input("enter:")               #checks the answer
      if xs==answerlist[index2]:
        return True
      else:                                 #this alse fuction uses loop to promp user to answer                                     again if wrong till  5 tries
        index1=0
        while index1<len(blankslist):
          ansagain=raw_input("answer again")
          if ansagain==answerlist[index2]:
            return True
          index1=index1+1  
    index=index+1
def stringreplace(n):                     #relaces the blanks with correct answers using .relace                                         function
  if n==True:
    if index2<1:
        reps=queslist[index].replace(blankslist[index2],answerlist[index2])
        return reps
    else:                                 #since strings are immutable objects in python if and                                      else statement was used to repatitively edit the                                           same eddited string
        reps=y.replace(blankslist[index2],answerlist[index2])
        return reps
        
          
          

def play():                      #this fuction loops over the blanks and uses stringreplace()                                   fuction over each blank replacing it
  global index2
  index2=0
  while index2<len(blankslist):
    x=stringreplace(anscheck())
    global y
    y=x
    print y
    index2=index2+1
  
play()  
  







        
     
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
