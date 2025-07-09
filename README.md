
# Mandarin Chatbot

This is a beginner-friendly Python chatbot that translates common English phrases into Mandarin using a JSON file (`phrases.json`).

### 🔸 How it works:
- You type a phrase in English (like "hello", "thankyou", etc.)
- The chatbot returns its Mandarin translation with Pinyin.

### 🔸 To run:
Make sure you have a `phrases.json` file in the same folder with this structure:

```json
{
  "phrases": [
    {"English": "hello", "Mandarin": "你好", "Pinyin": "nǐ hǎo"},
    ...
  ]
}
```

Then run:
```bash
python Chatbot.py
```

---
Made with ❤️ by Ishika (Aeshika's Mandarin Chatbot)
