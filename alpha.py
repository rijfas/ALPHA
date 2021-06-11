import speech_recognition as sr
import pyttsx3


class Alpha:
   _instance = None
   _input    = None 
   _output   = None 
   _actions  = None
   DEBUG     = None

   def __init__(self):
      raise RuntimeError('call instance() instead')

   @classmethod
   def instance(cls, actions : dict, debug=False):
      """
      Creates a new ``Alpha`` instance.
      The ``actions`` parameter is a dictionary which contains action phrase and action word.

      The ``debug`` parameter can be set to True to enable debug messages.
      """
      if cls._instance is None:
         cls._instance = cls.__new__(cls)
         cls._input    = sr.Recognizer()
         cls._output   = pyttsx3.init()
      cls._actions = actions
      cls.DEBUG    = debug
      return cls._instance

   @staticmethod
   def log_action(action : str):
      if Alpha.DEBUG:
         print(action)

   @classmethod 
   def say(cls, phrase : str):
      cls._output.say(phrase)
      cls._output.runAndWait()

   @staticmethod 
   def get_voice_input(input_scource):
      return Alpha._input.listen(input_scource)
   
   @staticmethod
   def get_command_from_voice(voice):
      return Alpha._input.recognize_google(voice)

   @staticmethod
   def resolve_command(command):
         if command in Alpha._actions.keys():
            Alpha.say(Alpha._actions[command])
         else:
            Alpha.log_action('EVENT: Unknown Command')
            Alpha.say('sorry, i didnt got it')

   def run(self):
      """
      Start alpha instance  
      """
      while True:
         try:
            with sr.Microphone() as microphone:
               print('Say Something, say quit to stop (or use CTR+C)')
               voice = Alpha.get_voice_input(microphone)
               command = Alpha.get_command_from_voice(voice)
               Alpha.resolve_command(command)

         except KeyboardInterrupt:
            print('Thank You')
            Alpha.log_action('EVENT: KeyboardInterrupt')
            break

         except sr.UnknownValueError:
            Alpha.say('sorry, i didnt got it')
            Alpha.log_action('ERROR: UnknownValueError')

         except:
            Alpha.log_action('FATAL: UnHandled Exception')
            Alpha.log_action(f'''
            Core Dump:
            _instance = {Alpha._instance}
            _input    = {Alpha._input} 
            _output   = {Alpha._output} 
            _actions  = {Alpha._actions}
            DEBUG     = {Alpha.DEBUG}
            ''')

