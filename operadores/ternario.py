lockdown = False
grana = 300
status = 'em casa' if lockdown or grana <= 100 else 'uhuuuu'

print(status)
