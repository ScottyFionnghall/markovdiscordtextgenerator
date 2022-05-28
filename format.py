import re
import markovify

with open("filename.txt", encoding="utf8") as f:
    text = f.read()
    f.close()
lines = text.split("\n")
non_empty_lines = [line for line in lines if line.strip() != ""]
string_without_empty_lines = ""
for line in non_empty_lines:
    x = re.findall('\[|http|:|{|m!|None|-', line)
    if not x:
        string_without_empty_lines += line + "\n"
with open('filename_formatted.txt', 'w', encoding='utf-8') as f:
      f.write(string_without_empty_lines)
      f.close
with open('corpus.json','w',encoding='utf-8') as f:
    text_model = markovify.Text(text, state_size=2)
    model_json = text_model.to_json()
    f.write(model_json)
    f.close
