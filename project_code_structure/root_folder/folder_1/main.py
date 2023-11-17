from folder_2.folder_3 import helper


def main_func():
    print('This is the main function.')
    helper.helper_func()


if __name__ == '__main__':
    input = input("Plz insert 1: ")

    if input == '1':
        main_func()

# python -m folder_1.main  