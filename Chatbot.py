
import json
# 1.load phrases.json file
with open('phrases.json','r',encoding = 'utf-8') as Myfile:
  data = json.load(Myfile)
 
# 2.Welcome message
print("\nHii!! Most Welcome to Aeshika's Mandarin Chatbot")
print("You can type: hello, Goodbye, Thankyou, I love you")
# 3. Get user input
user_input = input("Type something in English: ").strip().lower()
found= False
for phrase in data["phrases"]:
  if phrase["English"].strip().lower() == user_input:
    print("Pinyin:", phrase["Pinyin"])
    found = True
    break
if not found:
  print("I am not able to process it. Try a valid english phrase.")
