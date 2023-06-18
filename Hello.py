words=[]
num_words=int(input("How many words?"))

words=[ 0 for i in range (num_words)]

for i in range (num_words):
    words[i] = input("Input words:")  

for j in range (num_words):
  word = words[j]
  print("word>> ", words[j])

  word_len = int(len(words[j]))
  print("word_len:", word_len)

  num_vow = 0
  count_er=0
  start_index=0
  
  no_vow = word.find('a', start_index)
  if(no_vow!=-1):
    count_er+=1
  start_index = no_vow+1
  
  no_vow = word.find('e', start_index)
  if(no_vow!=-1):
    count_er+=1
  start_index = no_vow+1
  
  no_vow = word.find('i', start_index)
  if(no_vow!=-1):
    count_er+=1
  start_index = no_vow+1
  
  no_vow = word.find('o', start_index)
  if(no_vow!=-1):
    count_er+=1
  start_index = no_vow+1
  
  no_vow = word.find('u', start_index)
  if(no_vow!=-1):
    count_er+=1
  start_index = no_vow+1
  
  print("Total vowel are: ", count_er)
  characters = word_len - count_er
  print("Total character are:", characters)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    


  
