#NOTES
# TYPING TOO SMOOTH RIGHT NOW, MAYBE ADD SOME RANDOMNESS TO THE DELAY BETWEEN CHARACTERS based off model
# ALSO MAYBE SPLIT LINES BY PUNCTUATION LATER IDK
# FOR NOW LETS JUST IMPLENT THE KEYBOARD TYPING FUNCTIONALITY

import time
from pynput.keyboard import Controller


def get_text() -> str:
  # Prompt the user to enter multiple lines of text until they press Enter twice
  print("Paste your text below, then press Enter twice when done:")
  lines = []
  while True:
    line = input()
    if line == "":
      break
    lines.append(line)
  return "\n".join(lines)

def get_time() -> float:
  # Prompt the user to enter the time they want to take to type the text
  print("Enter the time (in seconds) you want to take to type the text:")
  while True:
    try:
      time = float(input())
      if time < 0:
        print("Please enter a positive number.")
        continue
      return time
    except ValueError:
      print("Invalid input. Please enter a number.")


text = get_text()
duration = get_time()
print(f"You entered: {text}")

def type_text(text: str, delay: float = 0.1) -> str:
  # Simulate typing the text with a delay between each character
  keyboard = Controller()
  time.sleep(3)
  for char in text:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(delay)
  return text

def determine_delay(text: str, duration: float) -> float:
  # Determine the delay between each character based on the total duration and the number of characters
  num_chars = len(text)
  delay = duration / num_chars
  return delay

def test():
  delay = determine_delay(text, duration)
  type_text(text, delay=delay)

test()