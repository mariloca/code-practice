'''
Remove a/some particular chars from a string
Ex: string="student", remove "u" and "n", output="stdet"
'''
def remove_char(string, input):
    '''
    i is slow pointer, j is fast pointer
    Move j and i, if [j]!=char,swap(i,j); if [j]==char, move j, i stays
    [0,i):processed chars, returned
    [i,j]:don't care
    (j,size-1):area to explore
    Return string[0:i]
    '''
    if len(string)==0:return string
    size=len(string)
    i,j=0,0
    while j<size:
        if string[j] not in input:
            string=swap(string,i,j)
            i+=1
            j+=1
        else:
            j+=1
    return string[0:i]


def swap(string,i,j):
    #strings are immutable, so can't modify slices like string[i]
    strlst=list(string)
    strlst[i],strlst[j]=strlst[j],strlst[i]
    return "".join(strlst)




def main():
    '''
    Testcases:
    #no duplicate chars in the string
    string="student"
    #has duplicate chars in the string
    string="stuuunt"
    #empty string
    string=""
    #single char string
    string="u"
    string="s"
    '''
    string="student"
    input=["u","n"]
    res=remove_char(string,input)
    print(res)

if __name__=="__main__":
    main()
