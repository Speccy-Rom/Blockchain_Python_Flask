import json


def write_block():
    data = {'name': 'ivan',
            'amount': 5,
            'to_whom': 'vasja',
            'hash': '1234'
            }
    with open ('test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block()

if __name__ == '__main__':
    main()
