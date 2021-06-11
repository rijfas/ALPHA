# Alpha : Simple Virtual Assistant 
Alpha is an simple virtual assistant built using Python.
## Requirements
___
You need Python 3.9 or later to run Alpha <br>
Libraries Used :
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)

## Installation
---
install requirements by running
```bash
pip install -r requirements.txt
```

## Example 
---
```python
from alpha import Alpha 

alpha = Alpha.instance(actions={
   'hi' : 'hello there',
   'who are you' : 'im alpha',
})
alpha.run()
```