 
sentence = input("what you massage : ")
sentence = sentence.lower().split()
 
positive_word= ["good","cool"]
negative_word= ["bad","uncool"]
 
positive_level=0
negative_level=0

 
mood = "Neutral"
 
for word in sentence:
    if word in positive_word:
        positive_level+=1
    elif word in negative_word:
        negative_level+=1
 
else:
    if positive_level-negative_word <0:
        mood = "negative"

print(f"Total number of words  {len(sentence)}")
print(f"Number of positive words {positive_level}")
print(f"Number of positive negative {negative_level}")
    
    
    
 
print(mood)
 