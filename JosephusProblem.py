def kill(n,p):

    if n == 1:
        return 0

    return (p + kill(n-1,p)) % n

print(kill(4,2))
