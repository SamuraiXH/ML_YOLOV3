import os
max_height=1040
max_weight=2008
def create_str_to_txt(name, data):
    path_file_name = './trans/%s.txt' % name
    if not os.path.exists(path_file_name):
        with open(path_file_name, "w") as f:
            print(f)

    with open(path_file_name, "a") as f:
        f.write(data)
        f.write('\r')

def read(filename):
    with open(filename, encoding='utf-8') as f:
        data = f.readlines()
        for line in data:
            odom = line.split()
            lst = (list(odom))
            print(lst)
            lst_new = []
            if lst[1] == '带电芯充电宝':
                lst_new.append(1)
            elif lst[1] == '不带电芯充电宝':
                lst_new.append(0)

            x_center = (float(lst[2]) + float(lst[4])) / 2
            y_center = (float(lst[3]) + float(lst[5])) / 2
            width = float(lst[4]) - float(lst[2])
            height = float(lst[5]) - float(lst[3])

            lst_new.append(round(x_center / max_weight,5))
            lst_new.append(round(y_center / max_height,5))
            lst_new.append(round(width / max_weight,5))
            lst_new.append(round(height / max_height,5))

            input =str(lst_new).replace("[","").replace("]","").replace(","," ")
            print(input)
            name = filename
            create_str_to_txt(name, input)

os.chdir("./Anno_core_coreless_battery_sub_2000_500")
for filename in os.listdir():
    print(filename)
    read(filename)