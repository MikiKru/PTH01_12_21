full_name = "World Health Organization"
shortcut = ""
print(full_name.split())
for word in full_name.split():      # domyślnie split dzieli po znakach białych
    if word[0].isupper():
        shortcut += word[0]

print(shortcut)