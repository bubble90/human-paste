import time
from pynput.keyboard import Key, Controller


# maybe split lines by punctuation later idk

def get_text():
  # Prompt the user to enter multiple lines of text until they press Enter twice
  print("Paste your text below, then press Enter twice when done:")
  lines = []
  while True:
    line = input()
    if line == "":
      break
    lines.append(line)
  return "\n".join(lines)

text = get_text()
print(f"You entered: {text}")

def type_text(text: str, delay: float = 0.1) -> str:
  keyboard = Controller()
  time.sleep(3)
  for char in text:
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(delay)
  return text

def test():
  type_text(text, delay=0.1)

test()