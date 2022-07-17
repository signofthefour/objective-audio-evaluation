import os
from types import new_class

from attr import validate

raw_texts = [l.strip().split('|') for l in open('metadata.txt').readlines()]
clean_texts = [l.strip().split('|') for l in open('clean_filelist.txt').readlines()]

validate_files = [l.strip().split('|')[0] for  l in open('validate.txt').readlines()]
train_500 = [l.strip().split('|')[0] for  l in open('training_500.txt').readlines()]
train_400 = [l.strip().split('|')[0] for  l in open('training_400.txt').readlines()]

raw_texts = [ [path.split('/')[0] + '_f_' + path.split('/')[1]+'.wav', s] for path, s in raw_texts]

file_to_raw = {path: s for path, s in raw_texts}
print(file_to_raw.keys())
file_to_clean = {path: s for path, s in clean_texts}

new_filelist = []

for f in file_to_clean:
    new_filelist.append([f, ' '.join([s.lower() for s in file_to_raw[f] if s != ' '])])
    
new_filelist = [[f, f'pitch/{f}'.replace('wav', 'pt'), s, '0'] for f, s in new_filelist]
validate_filelist = [f for f in new_filelist if f[0] in validate_files]
train_filelist = [f for f in new_filelist if f[0] not in validate_files]
train_500_filelist = [f for f in new_filelist if f[0] in train_500]
train_400_filelist = [f for f in new_filelist if f[0] in train_400]
open('raw_validate.txt', 'w+').write('\n'.join(['|'.join(t) for t in validate_filelist]))
open('raw_training.txt', 'w+').write('\n'.join(['|'.join(t) for t in train_filelist]))
open('raw_training_500.txt', 'w+').write('\n'.join(['|'.join(t) for t in train_500_filelist]))
open('raw_training_400.txt', 'w+').write('\n'.join(['|'.join(t) for t in train_400_filelist]))
# print(len(new_filelist), new_filelist[0])
# print(len(validate_filelist), validate_filelist[0])

g_set = [s[-2].split() for s in new_filelist]
from itertools import chain
g_set = list(set(list(chain(*g_set))))
open('g_set.txt', 'w+').write(' '.join(g_set))