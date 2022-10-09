def main(gl_name):
    global f_res
    with open(gl_name, "w", encoding='utf-8') as f_res:
        f_res.write('2.txt\n')
        wrt('2.txt')
        f_res.write('1.txt\n')
        wrt('1.txt')
        f_res.write('3.txt\n')
        wrt('3.txt')
def wrt(file):
    with open(file, encoding='utf-8') as f:
        len_f=str(len(f.readlines()))
        f.seek(0)
        list=f.readlines()
        f_res.write(len_f)
        f_res.write("\n")
        for file in list:
            f_res.write(file)
main(input('Задайте имя файла с разрешением. Пример: result.txt. Ответ напишите снизу\n'))
            

        
        
                    

    

        
