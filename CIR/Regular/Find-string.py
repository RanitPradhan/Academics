def count_substring(string, sub_string):
    count = 0
    for _ in range (len(string)):
        a = string.find(sub_string)
        if a==-1:
            break
        count+=1
        string = string[a+1:] #deleting the checked sub strings
    return(count)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)