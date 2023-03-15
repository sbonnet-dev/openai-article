import os
import openai
import re
import time

from md2pdf.core import md2pdf

OPENAI_KEY = "ENTER_YOUR_OPENAI_KEY"

def callOpenAI(text, token=150, temperature=0.3):
   openai.api_key = OPENAI_KEY
   model = "text-davinci-003"
   prompt = text

   response = openai.Completion.create(
        model="text-davinci-003",
	prompt=prompt,
        max_tokens=150,
        top_p=1.0,
        temperature=0.3,
        frequency_penalty=0.0,
        presence_penalty=0.0
   )
   return response["choices"][0]["text"]

############################################
################### MAIN ################### 
############################################

book = ""
os.system("clear")

language = input("Language: (french/english) : ")
thema = input("Enter the article thematic: ")

resp  = "n"
while(resp == "n"):
   question = "Create an outline for an essay with short terms about '" + thema + "' in " + language
   #response = getOutline(question)
   response = callOpenAI(question)
   response = re.sub(r'\n+', '\n', response).strip() 
   print(response + "\n")
   resp = input("Do you want to write an article with this table of contents  (y/n) ? ")

summary = response.splitlines()
book += "#" + thema + "\n"
cmpt = 0
type = ""

print("")
print("Writing document ...")
for chapter in summary:
   cmpt = cmpt + 1
      
   if cmpt % 3 == 1:
      print("Pause")
      time.sleep(20)

   if chapter:
      print("Writing paragraph => " + chapter)
      if cmpt == 1:
         type = "an introduction"
      else:
         type = "a paragraph"

      #paragraph = getParagraph("Write in " + language + " " + type  + " about '" + chapter + "' and make a transition with the previous paragraph : '" + summary[cmpt-1] + "' in a book context concerning '" + thema + "'")
      paragraph = callOpenAI("Write in " + language + " " + type  + " about '" + chapter + "' and make a transition with the previous paragraph : '" + summary[cmpt-1] + "' in a book context concerning '" + thema + "'", 4000, 0.9)
      if chapter[0] == "I" or chapter[0] == "V":
         book += "\n" + "###" + chapter + "\n"
      else:
         book += "\n" + "####" + chapter + "\n"
      book += paragraph + "\n\n"

md2pdf("./article.pdf", book, None, None, None)
#os.system("open ./article.pdf")