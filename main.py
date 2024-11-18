"""Main program"""

import src.textanalizer as textanalizer


text = textanalizer.read_file_by_ext("txt")
result = textanalizer.split_file_data(text)
print(f"Chars = {result[0]}\n Words = {result[1]}\n Phrases = {result[2]}")