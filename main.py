'''
Compteur de mot
Par Yul Kim
Groupe:405
Un compteur de mot
'''
def count_word(phrase):
    print('Il y a',len(phrase.split(" ")),'mot(s)')
phrase=input('Quel est votre phrase?:')
count_word(phrase)
