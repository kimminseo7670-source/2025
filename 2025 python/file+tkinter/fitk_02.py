def counting(name,word):
    try:
        with open(name,'r',encoding='utf-8') as file:
            text = file.read()
            count = text.count(word)
            return count
    except FileNotFoundError:
        print('파일을 찾을 수 없습니다')
        return 0
    
filename=input('텍스트 파일 이름을 입력하세요 : ')
search=input('검색 문자열을 입력하세요 : ')

num=counting(filename,search)

print(f'{search}는 파일 내에서 {num}번 나타납니다')