# PYST
Stand for **P*ut* Y*our* S*hit* T*ogether***. this is an Assistant that will try to help you out to reach a better version of yourself. Most of the people in they life have solve the best way to his/her development and i take my hat off to clap them, others no. Maybe you need a push or some ideas to do it, if this is the case this could help. 

I know there is a plenty solutions out there starting with Siri, Alexa, Cortana and others. But the idea is to have one really away from your phone and also be able to understand the code, improve it and personalize for yourself because we all have different need.

For start the main functions of the algorithm is to just create one simple new habit and keep track of it.

For the next steps the idea is to add AI to understand your behavior and make a better strategy to create and maintain the habits. This is why this project is open, and you should understand how it works because you don't want to give any app more sensitive data of yourself. **The mind is one of the most important part of you, don't trust them easily to a third party**, with this you will control every step of the process and maybe you will get interested more in the mind.

Also in the future you could add ChatGPT to ask questions, but this is not the main goal and Siri, Alexa or Cortana can perform this pretty well. Also you will be able to install this on your phone if you like, add some notifications and other things. But as i've said there is solutions for that.

For this you will need to have basic understanding of python because i will write the code in this language. Also we will use the microphone and the speakers in order to interact with the code.

### Current Status:

The code reply with a meme sound:
- if you say yes // will select a sound of the Sounds/Good
- if you say no // will select a sound of the Sounds/Bad
- if you say wait, hold on, i will // will select a sound of the Sounds/Waiting

**Something to fix:** with the current code if you say "yes" is classified as "Good" but if you say "yes i will" will also be classified as "Good" even if that is a "Waiting" reply (if you have any idea to solve this please let me know). For now i put "yes i will" ahead of "yes" in the csv file to avoid this.

You can put more answers, i will make them a function so it will be easy to use.

### For the next relase:

- Create an habit.
- Set reminders.
- Enable a countdown timer.
- Enable a pomodoro function.

### To be develop:

- Track habit.
- You can add your ChatGPT api in order to get your responses validates and save it in a csv file, then you will use it to train a model* and predict your answers.
- You will be able to ask directly to chatGPT and get an audio response.
- Make code of a model* that predict your answers for a better interaction with the Assistant.
- Ask information to Google and get an audio response. You will also need an api for that.
