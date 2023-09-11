capital = {'Thailand': 'Bangkok',
            'indonasia': 'Jakata',
            'India': 'New dehli',
            'America': 'Washington DC'}

capital.update({'Germany':'Berlin'})
capital.update({'Thailand':'Saraburi'})
capital.pop('India')
# print(Capital)
# print(Capital['America'])
# print(capital.get('Geramany'))
# print(capital.values())
# print(capital.keys())
# print(capital.items())

for key,value in capital.items():
    print(key,value)