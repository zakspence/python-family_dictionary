

family = {
            'sister': {
                'name': 'Sheena',
                'age': 32
            },
            'mother': {
                'name': 'Marilyn',
                'age': 57
            },
            'father': {
                'name': 'Donald',
                'age': 57
            },
            'brother': {
                'name': 'Ryan',
                'age': 26
            }
        }


family_details = ['My {}\'s name is {} and they are {}'.format(key, value['name'], str(value['age'])) for (key, value) in family.items()]

[print(statement) for statement in family_details]

