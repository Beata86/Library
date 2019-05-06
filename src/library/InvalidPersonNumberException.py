class InvalidPersonNumberException(Exception):
   def __init__(self):
       super().__init__("Wrong number")
