import re
import fitz

path = "pymupdf.pdf"

def search(target, path, context=10):
    doc = fitz.open(path)
    text = ""
    for page in doc:
      text+=page.get_text()
    words = re.findall(r"[\w']+|[.,!?;]", text)
    matches = []
    #print(words)
    for i,w in enumerate(words):
      if w.lower() == target:
        matches.append(i)
    search_results=[]
    for index in matches:
        if index < context //2:
            search_results.append(" ".join(words[0:context+1]))
        elif index > len(words) - context//2 - 1:
            search_results.append(" ".join(words[-(context+1):]))
        else:
            search_results.append(" ".join(words[index - context//2:index + context//2 + 1]))
    return search_results

print(list(search(input("Enter the string:"), path)))