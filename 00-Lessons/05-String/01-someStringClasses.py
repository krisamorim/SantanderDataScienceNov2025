course = "pYtHon"
print(f"Variable course with value {course}","with .upper() it becomes " + course.upper())  
print(f"Variable course with value {course}","with .lower() it becomes " + course.lower())
print(f"Variable course with value {course}","with .title() it becomes " + course.title())
print(f"Variable course with value {course}","with .capitalize() it becomes " + course.capitalize())

#remove white space from text
email = "    n ame@provider . com    "
print(f"variabel with value '{email}' after using .strip() it becomes '{email.strip()}' (remove from the beginning and the end)'")
print(f"variabel with value '{email}' after using .lstrip() it becomes '{email.lstrip()}' (remove from the beginning)'" )
print(f"variabel with value '{email}' after using .rstrip() it becomes '{email.rstrip()}' (remove from the end)'" )

#find and replace
text = "Hello, welcome to the world of Data Science. Data Science is fun!"
print(f"In the text: '{text}' the word 'Data' starts at index {text.find('Data')}")

new_text = text.replace("Data Science", "Machine Learning")
print(f"After replacing 'Data Science' with 'Machine Learning': '{new_text}'")

#center text between hastag
word = "Python"
print(word.center(20, '#'))

#using split and join
print(".".join(word))  # Joins each character with a dot
sentence = "Data Science is amazing"
words = sentence.split()  # Splits by whitespace
