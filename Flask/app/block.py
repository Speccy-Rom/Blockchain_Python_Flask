import json
import os



def get_hash(filename):
    blockchain_dir = os.curdir + '/blockchain/'


def write_block(name, amount, to_whom, prev_hash=' '):  # входные параметры
    blockchain_dir = os.curdir + '/blockchain/'

    files = os.listdir(blockchain_dir) # получение файлов папки
    files = sorted([i for i in files])

    last_file = files[-1]
    filename = str(last_file + 1)

    # print(filename)
    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash
            }
    with open(blockchain_dir + 'test', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block(name='Roman', amount=2, to_whom='Olga')


if __name__ == '__main__':
    main()
