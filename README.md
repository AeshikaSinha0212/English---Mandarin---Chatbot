
# Pinyin Chatbot

This is a beginner-friendly Python chatbot that translates common English phrases into Pinyin using a JSON file (`phrases.json`).

### 🔸 How it works:
- You type a phrase in English (like "hello", "thankyou", etc.)
- The chatbot returns its with Pinyin.

## 🚀 Getting Started

### Requirements
- Python 3.x

---

### 🛠 Installation & Execution

1. Download or clone this repository.
2. Ensure both `Chatbot.py` and `phrases.json` are located in the same directory.
3. Open a terminal/command prompt in that directory.
4. Run the chatbot using:

```bash
python Chatbot.py

```{
  "phrases": [
    { "English": "hello", "Pinyin": "nǐ hǎo" },
    { "English": "thank you", "Pinyin": "xièxiè" }
  ]
}
```
```
---

### 💻 Full Code: `Chatbot.py`

```python
import json

with open('phrases.json', 'r', encoding='utf-8') as Myfile:
    data = json.load(Myfile)

print("\nHii!! Most Welcome to Aeshika's Mandarin Chatbot")
print("You can type one of these English phrases:")
for phrase in data["phrases"]:
    print("-", phrase["English"])

user_input = input("\nType something in English: ").strip().lower()
found = False

for phrase in data["phrases"]:
    if phrase["English"].strip().lower() == user_input:
        print("Pinyin:", phrase["Pinyin"])
        found = True
        break

if not found:
    print("I am not able to process it. Try a valid English phrase.")

---
Made with ❤️ by Aeshika (Aeshika's Pinyin  Chatbot)
