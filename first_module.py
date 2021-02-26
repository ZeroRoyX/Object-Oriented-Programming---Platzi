# tema: if __name__ == '__main__'

# def main():
#     print("First Module's Name: {}".format(__name__))

# # There is code that you want to run whenever you run  as main file.
# if __name__ == '__main__':
#     print('Run directly')
# # There is code that you want to run when  it is being imported.
# else:
#     print('Run from import')


print('This will be always be run')

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    main()