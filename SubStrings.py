def func(string, curr, idx):

    if idx == len(string):
        print(curr, end=" ")
        return
  
    # Either add a character or not
    func(string, curr, idx+1)
    func(string, curr+string[idx], idx+1)


func("abc", "", 0)
