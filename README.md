# AI Chatbot Project  

Welcome to my AI Chatbot project! This repository shows how a simple chatbot can evolve from a **rule-based bot** to a more **intelligent machine-learning-based bot** that understands user intent.  

---

## Week 1: Rule-Based Chatbot 

In Week 1, I created a basic chatbot:

- Responds to greetings like "Hi" or "Hello".  
- Can say goodbye politely.  
- Code is located in `chatbot/week1_chatbot.py`.  

Think of it as a chatbot that **fol assssssssslows a script** — it only knows what you explicitly tell it.  


## Week 2: ML-Based Chatbot (Intent Recognition) 

In Week 2, I upgraded the bot to **understand user intent** using machine learning.  

- Uses `intents.json` to store **patterns** (user messages) and **responses** (bot replies).  
- Makes the bot **more flexible** and able to handle different ways people ask the same thing.  
- Code is in `chatbot/week2_chatbot.py`.  
- `intents.json` is in the project root folder. 


## How to Run the Chatbot:
1.Open a terminal and navigate to the project root:
   cd "C:\Users\Admin\Desktop\my_chatbot_project"
2.Run the Week 2 chatbot:
   python chatbot\week2_chatbot.py
3.Chat with the bot! Try typing:
   Hi 
   Thanks
   Bye

Example from `intents.json`:

```json
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello", "Hey"],
  "responses": ["Hello!", "Hi there!", "Hey! How can I help?"]
}
