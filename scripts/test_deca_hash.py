import sys
sys.path.append(r'C:\Users\Bolt\.gemini\antigravity\brain\a364eab8-5d66-45d0-aa69-f8fb75050f46\scratch\deca\python\deca\deca')

# We can import rot, mix, final, hashlittle2 directly
def rot(x, k):
    return ((x << k) | (x >> (32 - k))) & 0xffffffff

def mix(a, b, c):
    a &= 0xffffffff; b &= 0xffffffff; c &= 0xffffffff
    a -= c; a &= 0xffffffff; a ^= rot(c,4);  a &= 0xffffffff; c += b; c &= 0xffffffff
    b -= a; b &= 0xffffffff; b ^= rot(a,6);  b &= 0xffffffff; a += c; a &= 0xffffffff
    c -= b; c &= 0xffffffff; c ^= rot(b,8);  c &= 0xffffffff; b += a; b &= 0xffffffff
    a -= c; a &= 0xffffffff; a ^= rot(c,16); a &= 0xffffffff; c += b; c &= 0xffffffff
    b -= a; b &= 0xffffffff; b ^= rot(a,19); b &= 0xffffffff; a += c; a &= 0xffffffff
    c -= b; c &= 0xffffffff; c ^= rot(b,4);  c &= 0xffffffff; b += a; b &= 0xffffffff
    return a, b, c

def final(a, b, c):
    a &= 0xffffffff; b &= 0xffffffff; c &= 0xffffffff
    c ^= b; c &= 0xffffffff; c -= rot(b,14); c &= 0xffffffff
    a ^= c; a &= 0xffffffff; a -= rot(c,11); a &= 0xffffffff
    b ^= a; b &= 0xffffffff; b -= rot(a,25); b &= 0xffffffff
    c ^= b; c &= 0xffffffff; c -= rot(b,16); c &= 0xffffffff
    a ^= c; a &= 0xffffffff; a -= rot(c,4);  a &= 0xffffffff
    b ^= a; b &= 0xffffffff; b -= rot(a,14); b &= 0xffffffff
    c ^= b; c &= 0xffffffff; c -= rot(b,24); c &= 0xffffffff
    return a, b, c

def hashlittle2(data, initval=0, initval2=0):
    length = lenpos = len(data)
    a = b = c = (0xdeadbeef + length + initval) & 0xffffffff
    c = (c + initval2) & 0xffffffff
    p = 0
    while lenpos > 12:
        a += (data[p+0] + (data[p+1]<<8) + (data[p+2]<<16) + (data[p+3]<<24)); a &= 0xffffffff
        b += (data[p+4] + (data[p+5]<<8) + (data[p+6]<<16) + (data[p+7]<<24)); b &= 0xffffffff
        c += (data[p+8] + (data[p+9]<<8) + (data[p+10]<<16) + (data[p+11]<<24)); c &= 0xffffffff
        a, b, c = mix(a, b, c)
        p += 12
        lenpos -= 12
    if lenpos == 12: c += ((data[p+8]) + ((data[p+9])<<8) + ((data[p+10])<<16) + ((data[p+11])<<24)); b += ((data[p+4]) + ((data[p+5])<<8) + ((data[p+6])<<16) + ((data[p+7])<<24)); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 11: c += ((data[p+8]) + ((data[p+9])<<8) + ((data[p+10])<<16)); b += ((data[p+4]) + ((data[p+5])<<8) + ((data[p+6])<<16) + ((data[p+7])<<24)); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 10: c += ((data[p+8]) + ((data[p+9])<<8)); b += ((data[p+4]) + ((data[p+5])<<8) + ((data[p+6])<<16) + ((data[p+7])<<24)); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 9:  c += ((data[p+8])); b += ((data[p+4]) + ((data[p+5])<<8) + ((data[p+6])<<16) + ((data[p+7])<<24)); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 8:  b += ((data[p+4]) + ((data[p+5])<<8) + ((data[p+6])<<16) + ((data[p+7])<<24)); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 7:  b += ((data[p+4]) + ((data[p+5])<<8) + ((data[p+6])<<16)); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 6:  b += (((data[p+5])<<8) + (data[p+4])); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24))
    if lenpos == 5:  b += ((data[p+4])); a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24));
    if lenpos == 4:  a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16) + ((data[p+3])<<24))
    if lenpos == 3:  a += ((data[p+0]) + ((data[p+1])<<8) + ((data[p+2])<<16))
    if lenpos == 2:  a += ((data[p+0]) + ((data[p+1])<<8))
    if lenpos == 1:  a += (data[p+0])
    a &= 0xffffffff; b &= 0xffffffff; c &= 0xffffffff
    if lenpos == 0: return c, b
    a, b, c = final(a, b, c)
    return c & 0xffffffff, b & 0xffffffff

def hash32(data):
    if isinstance(data, str):
        data = data.encode('ascii')
    c, b = hashlittle2(data, 0, 0)
    return c

import glob, struct
all_hashes = {}
for t in glob.glob(r'D:\SteamLibrary\steamapps\common\theHunterCotW\archives_win64\*.tab'):
    with open(t, 'rb') as f:
        data = f.read()
    for i in range(12, len(data), 12):
        if i + 12 <= len(data):
            h, off, sz = struct.unpack('<III', data[i:i+12])
            all_hashes[h] = (t, off, sz)

test_strings = [
    'settings/hp_settings/string_ids.stringlookup',
    'settings/hp_settings/animal_settings.bin',
    'settings/creatures.bin',
    'locations/world.bin',
    'settings/benchmarks.bin',
    'settings/factions.bin',
    'gdc/global.gdcc',
    'global.gdcc',
    'worlds/base/locations/hp_germany_farmlands_fall/features_germany_farmlands_fall'
]

for s in test_strings:
    h = hash32(s)
    if h in all_hashes:
        print(f'MATCH! {s} -> hash={hex(h)} in {all_hashes[h]}')
    h_lower = hash32(s.lower())
    if h_lower in all_hashes:
        print(f'MATCH lower! {s.lower()} -> hash={hex(h_lower)} in {all_hashes[h_lower]}')
