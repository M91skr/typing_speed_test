#Typing Speed Test

## Description
In this code, a desktop application is created that evaluates the user's typing speed.

### How it works?
A text is displayed for the user to type. The user must type them within 60 seconds.
By pressing the start button, the challenge time starts and after 60 seconds the points will be displayed to the user.

### What are the points?
We will have two points CPM and WPM.
They're short for Characters Per Minute, and Words Per Minute.
The "CPM" is the actual number of characters you type per minute, including all the mistakes.
"Corrected" scores count only correctly typed words. 
"WPM" is just the corrected CPM divided by 5. That's a de facto international standard.
The structure of this test is inspired by the site https://typing-speed-test.aoeu.eu/.


## How to run
run following:
```bash
python -m venv env
. env/bin/activate
python main.py
```