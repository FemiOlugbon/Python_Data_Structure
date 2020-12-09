
def Anagram_Check_Off(s_1, s_2):
    OK = True
    if len(s_1) != len(s_2):
        OK = False
    
    list_s_2 = list (s_2)
    pos_1 = 0

    while pos_1 < len(s_1) and OK:
        pos_2 = 0
        found = False
        while pos_2 < len(list_s_2) and not found:
            if s_1[pos_1] == list_s_2[pos_2]:
                found = True
            else:
                pos_2 = pos_2 + 1

        if found:
            list_s_2[pos_2] = None
        else:
            OK = False

        pos_1 = pos_1 + 1
    return OK


def Anagram_Sort_Compare(s_1, s_2):
    list_s_1 = list(s_1)
    list_s_2 = list(s_2)

    list_s_1.sort()
    list_s_2.sort()

    pos = 0
    OK = True

    while pos < len(s_1) and OK:
        if list_s_1[pos] == list_s_2[pos]:
            pos = pos + 1
            
        else:
            OK = False
            
    return OK


def Anagram_Counts(s_1, s_2):
    count_1 = [0] * 26
    count_2 = [0] * 26

    for alph in range(len(s_1)):
        pos = ord(s_1[alph]) - ord("a")
        count_1[pos] = count_1[pos] + 1

    for alph in range(len(s_2)):
        pos = ord(s_2[alph]) - ord("a")
        count_2[pos] = count_2[pos] + 1

    index = 0
    OK = True
    while index < 26 and OK:
        if count_1[index] == count_2[index]:
            index += 1
        else:
            OK = False

    return OK



        



