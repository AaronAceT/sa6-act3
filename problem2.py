listing = ['bear', 'snake', 'tiger', 'panda', 'raven']

sorted_list = sorted(listing, key=lambda x: (len(x), x))

print(sorted_list)