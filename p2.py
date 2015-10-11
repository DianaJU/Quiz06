def stars(instars):
    nstars = ""
    control = 0
    while(control<instars):
        nstars = nstars + "*"
        control = control + 1
    return nstars
print (stars(5))
