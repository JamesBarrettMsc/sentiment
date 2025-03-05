 
sentence = input("what you massage : ")
sentence = sentence.lower().split()
 
positive_word= ["good","cool","bmazing", "brilliant"]
negative_word= ["bad","uncool","awful", "lame"]
 
positive_level=0
negative_level=0

 
sentiment = "Neutral"
 
for word in sentence:
    if word in positive_word:
        positive_level+=1
        
    elif word in negative_word:
        negative_level+=1
 
else:
    if positive_level-negative_level <0:
        sentiment = "Negative"
        
    elif(positive_level-negative_level >0):
        sentiment = "Positive"
        
print("="*20)

print(f"Total number of words  {len(sentence)}")
print(f"Number of positive words {positive_level}")
print(f"Number of positive negative {negative_level}")

print("="*20)
print(f"The Sentiment Analysis {sentiment}")
print("="*20)
 