my_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for new in my_text:
    if new.isdigit():
        new_list.extend(['"', f'{int(new):02}', '"'])
    elif (new.startswith('+') or new.startswith('-')) and new[1:].isdigit():
        new_list.extend(['"', f'{new[0]}{int(new[1:]):02}', '"'])
    else:
        new_list.append(new)

out_info = ' '.join(new_list)
print(out_info)





