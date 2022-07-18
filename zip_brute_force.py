# If you remember that your pass contains exact patterns, but you don't remember the order or kind of the patterns
pass_pos = ['qwerty', '123123', '123qwe']
# Another possible solution is to use baseN, for instance base62(abc,ABC,123 -> 26+26+10=62)

from itertools import chain, combinations
def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(3, len(ss)+1)))

# for subset in all_subsets(pass_pos):
#     print(''.join(subset))

from zipfile import ZipFile
subb = all_subsets(pass_pos)
norm_subb = []
for subset in all_subsets(pass_pos):
    stt = ''.join(subset)
    # If you remember that your pass starts from exact symbols, otherwise remove the statement
    if stt.startswith('qwe'):
        # If you know aprx length
        if 8 <= len(stt) <= 12:
            norm_subb.append(stt)

            
path_from = '/Volumes/FLASH/path_to_your_zip.zip'
path_to = 'Downloads/zip_opened'
            
for subset in norm_subb:
    try:
        print(''.join(subset))
        ZipFile(path_from).extractall(path=path_to, pwd=''.join(subset))
        print(subset)
        exit()
    except Exception:
        continue
