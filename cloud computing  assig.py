import string
book_string1 =open('/home/ahmed/Documents/cloud_assig/Beyond the Wall of Sleep').read().lower()
book_string2 =open('/home/ahmed/Documents/cloud_assig/Pride and Prejudice').read().lower()


un_used_words = ['i', 'you', 'he', 'she', 'it', 'we', 'they','mine', 'yours', 'his', 'hers', 'ours', 'theirs',
'which', 'who', 'that','this', 'these', 'those','is','are','after', 'before', 'in','on','at','of','a','the',
'us','the','an']

new_book1 = set(book_string1.translate(str.maketrans('', '', string.punctuation)).split())
new_book2 = set(book_string2.translate(str.maketrans('', '', string.punctuation)).split())


for x in new_book1:
    if x in new_book2:
        if x not in un_used_words:
            print(x)


