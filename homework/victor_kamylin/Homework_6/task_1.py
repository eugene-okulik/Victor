text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel.'
        ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')

ending = "ing"

finish_text = []

for word in text.split():
    if word[-1] in ',.!?':
        finish_text.append(word[:-1] + ending + word[-1])
    else:
        finish_text.append(word + ending)
        
print(' '.join(finish_text))
