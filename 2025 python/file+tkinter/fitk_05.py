import tkinter as tk
from tkinter import filedialog,messagebox

def count_stats(filename):
    space=0
    upper=0
    lower=0
    with open(filename,'r',encoding='utf-8') as file:
        for line in file:
            for ch in line:
                if ch==' ':
                    space+=1
                elif ch.isupper():
                    upper +=1
                elif ch.islower():
                    lower+=1
    return space,upper,lower

def select_file():
    filepath=filedialog.askopenfilename(
         title='파일을 선택하세요'
       ,filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")])
    
    if not filepath:
        return
    try:
        space,upper,lower=count_stats(filepath)
        file_label.config(text=f'선택된 파일: {filepath}')
        result_label.config(text=f'스페이스: {space},대문자: {upper}, 소문지: {lower}')
    except Exception as e:
        messagebox.showerror('에러',f'파일을 처리하는 중 오류가 발생했습니다.\n{e}')


root=tk.Tk()
root.title('문제 5')
root.geometry('520x220')
tk.Label(root,text='텍스트 파일을 선택하여 스페이스, 대문자, 소문자 개수를 세어보세요').pack(pady=10)

tk.Button(root,text='파일 선택',command=select_file).pack(pady=10)
file_label=tk.Label(root,text='선택된 파일: (없음)')
result_label=tk.Label(root,text='스페이스: 0, 대문자: 0, 소문자: 0')
file_label.pack(pady=10)
result_label.pack(pady=10)

root.mainloop()