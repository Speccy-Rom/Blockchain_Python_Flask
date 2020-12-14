import json
import os
import hashlib


def get_hash(filename):
    blockchain_dir = os.curdir + '/blockchain/'
    file = open(blockchain_dir + filename, 'rb').read()

    return hashlib.md5(file).hexdigest()


def check_integrity():
    # 1.Считать хэш предыдущего блока
    # 2.Вычислить хэш предыдущего блока
    # 3.Сравнить полученные данные

    blockchain_dir = os.curdir + '/blockchain/'
    files = os.listdir(blockchain_dir)
    files = sorted([int(i) for i in files])

    for file in files[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash']
        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        print('block {} is: {}'.format(prev_file, res))



def write_block(name, amount, to_whom, prev_hash=''):  # входные параметры
    blockchain_dir = os.curdir + '/blockchain/'

    files = os.listdir(blockchain_dir)  # получение файлов папки
    files = sorted([int(i) for i in files])

    last_file = files[-1]

    filename = str(last_file + 1)

    prev_hash = get_hash(str(last_file))

    # print(filename)

    data = {'name': name,
            'amount': amount,
            'to_whom': to_whom,
            'hash': prev_hash}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    # write_block(name='Roman', amount=2, to_whom='Olga')
    check_integrity()


if __name__ == '__main__':
    main()
