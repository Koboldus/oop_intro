s = 'ala ma kota'
s = s.title()
s = s.upper()
s = s.lower()
s = s.capitalize()
s = s[:-1].lower() + s[-1].upper()
s = s.replace('ala', 'roman')
#print(s.startswith('ala'))
#print(s.endswith('kotA'))
s = s.replace('ma ', 'ma 2 ')
#print(s)
l = s.split()
l.append('wszy')
l.insert(-1, 'i')
l.remove('roman')
l.insert(0, 'ala')
id_ = l.index('kotA')
#print(id_)
l.pop(id_)
l = [int(word) if word.isdigit() else word for word in l]
s1 = ' '.join([str(word) for word in l])
#print(s1)
#print(dir(s1))
#print(dir(l))

class A(object, metaclass = type):
    pass

class B(A, metaclass = type):
    pass