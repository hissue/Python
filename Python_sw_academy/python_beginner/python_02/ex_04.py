'''
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

출력
Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.
'''
st='Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
mo='aeiou'

di=[ i for i in st if i not in mo]
print('{}'.format(''.join(di)))


# data_str = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# serch = 'aeiou'
# result = [i for i in data_str if i not in serch]
# print(''.join(result))

