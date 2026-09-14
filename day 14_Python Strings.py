# ----- Python strings -----
# name = "Kavi"

# ----- String indexing -----

name = "Kavi"
print(name[3])
print(name[-2])
print(name[0])

# ----- String slicing ----- 

word = "PYTHON"
print(word[0:3])
print(word[2:])

# ----- Reverse a string ------ 

word = "PYTHON"
print(word[::-1])

# ------ string are immutable -----

name = "Kavi"
name = "R" + name[1:]
print(name)

# ----- Len() -----

name = "Kavi"
print(len(name))

# ----- String Methods -----
# ----- Upper() -----

name = "Kavi"
print(name.upper())

# ----- Strip() -----

name = "    Kavi    " \
"print(name.strip())"

# ------ replace() -----

text = "I like java"
texy = text.replace("java", "python")
print(text)

# ------ find() ----- 

text = "I love python"
print(text.find("python"))

# ----- count() ------

text = "banana"
print(text.count("a"))

# ------ in operator ------

text = "I love python"
print("python" in text)

# ----- Strings concepts part 2 -----
# ----- split() ------

text = "my skill is python"
words = text.split()
print(words)

# ----- Join() -----

words = ["python", "is", "powerful"]
sentence = " ".join(words)
print(sentence)

# ----- Startwith() ------

email = "kavi@gmail.com"
print(email.startwith("kavi"))

# ----- Endwith() ------

file = "resume.pdf"
print(file.endwith(".pdf"))

# ------ isalpha() ------

name = "Kavi"
print(name.isalpha())

name = "kavi123"
print(name.isalpha())

# ------ isdigit() -----

age = "20"
print(age.isdigit())

age = "20years"
print(age.isdigit())

# ----- Looping through string -----

word = "PYTHON"
for char in word:
    print(char)
    







