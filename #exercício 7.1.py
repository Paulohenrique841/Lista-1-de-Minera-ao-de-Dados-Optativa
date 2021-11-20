x=['Pedro','Andre','Maria','Luana']

Pedro=x.count('Pedro')
Andre=x.count('Andre')
Maria=x.count('Maria')
Luana=x.count('Luana')

d={'Pedro':Pedro, 'Andre':Andre,'Maria':Maria,'Luana':Luana,}

for i,j in d.items():
    print('Nome', i,' : ',j,'vezes')
