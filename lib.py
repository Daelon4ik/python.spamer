import config

def main():

    file = open(r'C:\Users\anton\Desktop\Python\spamer\text.txt', encoding='UTF-8')
    text = file.read()
    lis = []
    num = 0
    end_num = 0
    for i in text:
        if i == config.new_text:
            lis.append(text[end_num:num])
            end_num = num+2

        num += 1

    return lis

if __name__ == '__main__':
    print(main())