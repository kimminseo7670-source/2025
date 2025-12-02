def merge(path1,path2,output_path):
    with open(path1,'r',encoding='utf-8') as file1:
        file1_text=file1.read()

    with open(path2,'r',encoding='utf-8') as file2:
        file2_text=file2.read()

    merge_text=file1_text + '\n'+file2_text

    with open(output_path,'w',encoding='utf-8') as output_file:
        output_file.write(merge_text)


file1_path='file1.txt'
file2_path='file2.txt'
output_path='output.txt'

merge(file1_path,file2_path,output_path)