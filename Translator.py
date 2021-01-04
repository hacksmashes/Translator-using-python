from translate import Translator

#mention the language correctly
translator=Translator(from_lang="french",to_lang="english")

# type the word here which word u want to translate
result=translator.translate("bonjour")
print("The translated word =",result)




        
