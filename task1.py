
card="4716 1089 9971 6531"
def verify(card):
    card_numb = card.translate(str.maketrans({'-': '', ' ': ''}))
    if len(card_numb)!=16: 
        return(False)
    else:
        list_odd, list_even = [], []
        sum_odd, sum_even = 0, 0

        for i in range(0,len(card_numb),2):
            list_even.append(int(card_numb[i]))
            list_odd.append(int(card_numb[i+1]))

        sum_odd = sum(list_odd)
        
        for i in range(len(list_even)):
            numb = list_even[i] * 2
            if numb >= 10:
                numb = (numb//10) + (numb%10)
            sum_even += numb

        if (sum_odd + sum_even) % 10 == 0:
            return(True)
        else:
            return(False)
        