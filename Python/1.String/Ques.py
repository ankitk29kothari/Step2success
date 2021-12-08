You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM

Pythonist 2 → pYTHONIST 2 



















# sWAP cASE in Python - HackerRank Solution
def swap_case(s):

    # sWAP cASE in Python - HackerRank Solution START
    Output = '';
    for char in s:
        if(char.isupper()==True):
            Output += (char.lower());
        elif(char.islower()==True):
            Output += (char.upper());
        else:
            Output += char;
    return Output;
    # sWAP cASE in Python - HackerRank Solution END

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)