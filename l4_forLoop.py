sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Write a for loop to print out each word in the sentence list, one word per line
for index in range(len(sentence)):
    word = sentence[index]
    print(word)

# OR
for i, word in enumerate(sentence):
    print(word)
    
   # Practice: Multiples of 5
   # Write a for loop below that will print out every whole number 
   # that is a multiple of 5 and less than or equal to 30.

   for count in list(range(30)):
       if count % 5 == 0:
       	    print(count)
    