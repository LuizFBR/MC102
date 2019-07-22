# Luiz FErnando Bueno Roosa - RA 221197

punctuation = ',.?!:'

def adjust(string):
    return string.lower().translate(None, punctuation)

def has_punc(string):
    return string != string.translate(None, punctuation)

list_text = input().split()
list_adjusted = [adjust(x) for x in list_text]

quit = False

print(' '.join(list_text))

if len(list_text) <= 1000:

    while quit is False:

        text_edit = input()

        if text_edit == 'Q':
            quit = True

        elif text_edit == 'D':

            remove = adjust(input())

            i = 0
            max = len(list_text)

            while i < max:
                if remove == list_adjusted[i]:
                    del list_text[i]
                    del list_adjusted[i]
                    max -= 1

                else:
                    i += 1

            print(' '.join(list_text))


        elif text_edit == 'R':

            replaced = adjust(input())
            replace = input()
            replace_adjusted = adjust(replace)

            i = 0
            max = len(list_text)

            while i < max:
                if replaced == list_adjusted[i]:
                    list_text[i] = replace
                    list_adjusted[i] = replace_adjusted

                i += 1

            print(' '.join(list_text))

        elif text_edit == 'I':

            invert = adjust(input())

            i = 0
            max = len(list_text)

            while i < max:
                if invert == list_adjusted[i]:
                    if (has_punc(list_text[i])):
                        punc = list_text[i][-1]
                        list_text[i] = list_text[i][::-1][1:] + punc
                    else:
                        list_text[i] = list_text[i][::-1]
                    list_adjusted[i] = adjust(list_text[i])

                i += 1

            print(' '.join(list_text))
