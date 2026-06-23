def look_say(number):
    s = []
    for n in number:
        if len(s) == 0:
            s.append(n)
        else:
            if s[-1] == n:
                s.append(n)
            else:
                print(len(s), s[-1])
                s = [n]

    print(len(s), s[-1])

look_say('11221')