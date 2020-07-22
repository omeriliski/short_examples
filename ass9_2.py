#Letters Count
sentence = input("Enter a sentence: ")
result={}
for i in set(sentence):
    result[i]=sentence.count(i)
print(result)