text = "Ala ma kota a kot ma Ale"

print(text[0], text[1])
# niezmienność
# text[0] = 'X'
# niemutowalność
upper_text = text.upper()
print(upper_text, text)

quote = "\"I\'m your father!\""
url = "www.xyz.pl\\abc\\new"
print(quote, url)
print('abnormal', 'a\bnormal')

s = 'a'
print(s, ord(s))
print(ord(s), chr(ord(s)))

s1 = "alaaaaaaaa"
s2 = "ala\n"
print(s1 == s2, s1 > s2)

for character in s1:
    print(character)


name = "Anna"
age = 30
status = True
salary = 12_323.33221
print("name={}\nage={}\nstatus={}".format(name, age, status))
print(f"name={name:>10}\nage={age:5}\nstatus={status}\nsalary={salary:10.2f}zł")

print(f"|{name:>20}|{age:>5}|{status:>10}|{salary:>20.2f}zł|")
print(f"|{name:>20}|{age:>5}|{status:>10}|{salary:>20.2f}zł|")
print(f"|{name:>20}|{age:>5}|{status:>10}|{salary:>20.2f}zł|")
print(f"|{name:>20}|{age:>5}|{status:>10}|{salary:>20.2f}zł|")


s = "abc"
print(s.capitalize())
print(s.join(s), s + s)

