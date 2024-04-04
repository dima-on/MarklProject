with open('test.txt', 'r', encoding='utf-8') as file:
    Lern_input = file.read()


words = Lern_input.split()

AllWords = []
AfterWords = []
AfterWordsCount = []

def checkFullStop(simvol):
    for oneSimvol in simvol:
        if oneSimvol == "." or oneSimvol == "?":
            return False
    return True
def checkSetWords(simvol):
    iCount = 0
    for sim in AllWords:
        if simvol == sim:
            return iCount
        iCount += 1
    return -1

def check_Set_Next_Words(simvol, indexWord):
    iCount = 0
    print(simvol, indexWord)
    for WordsIn in AfterWords[indexWord]:
        if simvol == WordsIn:
            return iCount
    return -1

def Write_New_Words(CountForInCheck, nextWord):


    AfterWords[CountForInCheck].append(nextWord)
    AfterWordsCount[CountForInCheck].append(1)
def Check_New_Words(CountForInCheck, Index_Word):

    IndexWords = check_Set_Next_Words(words[CountForInCheck + 1], Index_Word)
    print(IndexWords, CountForInCheck)
    if IndexWords >= 0:
        len(AfterWordsCount[Index_Word])
        AfterWordsCount[Index_Word][IndexWords] += 1
    else:
        AfterWords[Index_Word].append(words[CountForInCheck + 1])
        AfterWordsCount[Index_Word].append(1)



CountForInCheckAll = 0
CountForInCheckYes = 0
CountForInCheckNo = 0
for word in words:
    if checkFullStop(word):
        IndexWordSet = checkSetWords(word)
        if IndexWordSet >= 0:
            print(IndexWordSet)
            Check_New_Words(CountForInCheckAll, IndexWordSet)
            CountForInCheckYes += 1

        else:

            AllWords.append(word)
            AfterWords.append([])
            AfterWordsCount.append([])
            Write_New_Words(CountForInCheckNo, words[CountForInCheckAll + 1])

            CountForInCheckNo += 1
    CountForInCheckAll += 1


print(AllWords)
print(AfterWords)
print(AfterWordsCount)
