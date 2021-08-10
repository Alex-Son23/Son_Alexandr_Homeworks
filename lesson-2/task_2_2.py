weather = ['в', '5', 'часов', '7', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
wLength = len(weather)
i = 0
while i < wLength:
    try:
        numb = abs(int(weather[i]))
        if numb < 10:
            weather[i] = weather[i].replace(str(numb), '0' + str(numb))
        weather.insert(i, '"')
        weather.insert(i + 2, '"')
        wLength += 2
        i += 2
    except ValueError:
        None
    i += 1

print(' '.join(weather))
