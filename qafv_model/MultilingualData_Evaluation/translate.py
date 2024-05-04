import csv
from googletrans import Translator
from googletrans.constants import LANGUAGES

# # Install googletrans first using one of the methods below:
# # pip install googletrans==4.0.0-rc1
# # pip install googletrans==3.1.0a0
# # pip install google_trans_new

# Init
translator = Translator()

# List of target languages
target_languages = ['te', 'zh-cn', 'hi', 'es']

def translateData(filename):
  # Open the CSV file
  with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
      print(filename)
      # Create a reader object
      reader = csv.DictReader(csvfile)
      
      # Read all rows into a list
      rows = list(reader)
      
      # Calculate the number of rows per language
      num_rows_per_language = len(rows) // len(target_languages)
      print(num_rows_per_language)
      remaining_rows = len(rows) % len(target_languages)
      print(remaining_rows)
      # Iterate over target languages
      for i, lang in enumerate(target_languages):
          print(f"Translating to {LANGUAGES[lang]}:")
          # Determine the start and end index for the current language group
          start_index = i * num_rows_per_language
          end_index = (i + 1) * num_rows_per_language

          # If it's the last language, include remaining rows
          if i == len(target_languages) - 1:
              end_index += remaining_rows

          # Open a file for writing the translated output
          with open(f'translated_output_{lang}.txt', 'w', encoding='utf-8') as outfile:
              # Translate sentences for the current group
              for row in rows[start_index:end_index]:
                  # Extract text from the first column
                  text_to_translate = row['claim']
                  # Call to translate and get output
                  output = translator.translate(text_to_translate, src='en', dest=lang)
                  # Write the translated text to the file
                  outfile.write(output.text + '\n')
          print(f"Translation to {LANGUAGES[lang]} completed and written to 'translated_output_{lang}.txt' file.\n")


# translateData("2-hop-lang.csv")
# translateData("3-hop-lang.csv")
# translateData("4-hop-lang.csv")
# translateData("fev_train-lang.csv")
