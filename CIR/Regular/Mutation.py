def mutate_string(string, position, character):
    n=list(string) #converted to list
    n[position] = character #character position assigned
    string = "".join(n) #character replaced in particular position
    return(string)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)