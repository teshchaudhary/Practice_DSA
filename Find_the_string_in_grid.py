#Given a 2D grid of n*m of characters and a word, find all occurrences of given word in grid. A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form). The 8 directions are, horizontally left, horizontally right, vertically up, vertically down, and 4 diagonal directions.

Note: The returning list should be lexicographically smallest. If the word can be found in multiple directions starting from the same coordinates, the list should contain the coordinates only once. 

def check_left(x,y,word,grid,word_i):
        if y<0:
            return False
        if grid[x][y]!=word[word_i]:
            return False
        if word_i==len(word)-1:
            return True
        return check_left(x,y-1,word,grid,word_i+1)
     
def check_up(x,y,word,grid,word_i):
    if x<0:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_up(x-1,y,word,grid,word_i+1)
    
def check_right(x,y,word,grid,word_i):
    if y>len(grid[0])-1:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_right(x,y+1,word,grid,word_i+1)
    
def check_down(x,y,word,grid,word_i):
    if x>len(grid)-1:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_down(x+1,y,word,grid,word_i+1)
    
def check_left_up(x,y,word,grid,word_i):
    if x<0 or y<0:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_left_up(x-1,y-1,word,grid,word_i+1)
    
    
def check_right_up(x,y,word,grid,word_i):
    if x<0 or y>len(grid[0])-1:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_right_up(x-1,y+1,word,grid,word_i+1)

def check_down_left(x,y,word,grid,word_i):
    if x>len(grid)-1 or y<0:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_down_left(x+1,y-1,word,grid,word_i+1)


def check_down_right(x,y,word,grid,word_i):
    if x>len(grid)-1 or y>len(grid[0])-1:
        return False
    if grid[x][y]!=word[word_i]:
        return False
    if word_i==len(word)-1:
        return True
    return check_down_right(x+1,y+1,word,grid,word_i+1)
    
def searchWord(grid, word):
		row=len(grid)
        l1=[]
        column=len(grid[0])
        for i in range(row):
            for j in range(column):
                if grid[i][j]==word[0]:
                    ans=False
                    ans=ans or check_left(i,j,word,grid,0)
                    ans=ans or check_up(i,j,word,grid,0)
                    ans=ans or check_right(i,j,word,grid,0)
                    ans=ans or check_down(i,j,word,grid,0)
                    ans=ans or check_left_up(i,j,word,grid,0)
                    ans=ans or check_right_up(i,j,word,grid,0)
                    ans=ans or check_down_left(i,j,word,grid,0)
                    ans=ans or check_down_right(i,j,word,grid,0)
                    if ans==True:
                        l1.append([i,j])
        if not l1:
            return [[-1]]
        else:
            return l1
