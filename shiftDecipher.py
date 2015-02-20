from wordTest import is_word
import csv

def shift(text, shift):
    alphbet = "abcdefghijklmnopqrstuvwxyz"
    cAlphbet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    newText = ''
    for letter in text:
        if letter == letter.upper():
            newLetter = cAlphbet[cAlphbet.find(letter) - shift]
        else:
            newLetter = alphbet[alphbet.find(letter) - shift]
        newText += newLetter
    return newText

def decipher(text):
    result = []
    for i in range(26):
        newtext = shift(text, i)
        newtext = newtext.lower()
        ##print newtext
        if is_word(newtext):
            result.append(i)
            ##print i, newtext 
    return result
    
def splitter(sentence, shuffle=None):
    result = ''
   
    words = sentence.split()
    print 'word ', words[0]
    if shuffle != None:
        for word in words:
            result += shift(word, shuffle)
            result += ' '
            
        return shuffle, result
    else:
        de = decipher(words[0])
        print 'test ', de
       
        try:
            return splitter(sentence, shuffle=de[0])
        except IndexError:
            raise TypeError('CipherError')
            


def getCipher():
    reader = csv.reader(open(".../mitnick1"), delimiter='\t')
    fwrite = open(".../mitnickDecoded", 'w')
    
    for row in reader:
        row = ' '.join(row)
        
        if "ch" not in row:
            try:
                print 'row', row
                newStr = splitter(row)
                print 'newStr', newStr
                fwrite.write('shift of  : %i...\n' % (newStr[0]))
                fwrite.write(''.join(newStr[1]))
                fwrite.write('\n')
            except TypeError:
                fwrite.write('not a simple shift cipher')
                fwrite.write('\n')
            
        else:
            fwrite.write('\n')
            fwrite.write(str(row))
            fwrite.write('\n')
        
    fwrite.close()
    ##print textList
    ##print decipheredStr
  

getCipher()                      
##print splitter ('Yjcv ku vjg pcog qh vjg uauvgo wugf da jco qrgtcvqtu vq ocmg htgg rjqpg ecnnu')
