def read_file(name):
    try:
        with open(name,'r',encoding='utf-8') as file:
            text=file.read()
            print(text)

    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')


read_file(input('텍스트 파일 이름을 입력하세요 : '))