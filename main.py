def main(name):
    files = ['1.txt', '2.txt', '3.txt']
    inf_f = {}
    for file in files:
        with open(file, encoding = 'utf-8') as f:
            supp_inf_f = {file : [len(f.readlines())]}
            f.seek(0)
            supp_inf_f[file].append(f.readlines())
            inf_f.update(supp_inf_f)
    sorted_dict = dict(sorted(inf_f.items(), key = lambda x: x[1][1], reverse = True))
    with open(name, 'w', encoding = 'utf-8') as wr_f:
        for key in sorted_dict.keys():
            wr_f.write(key)
            wr_f.write('\n')
            wr_f.write(str(sorted_dict[key][0]))
            wr_f.write('\n')
            for element in sorted_dict[key][1]:
                wr_f.write(element)
main(input('Введите название файла: '))


