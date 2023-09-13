    path = '/etc/snort/rules/local.rules'

    sid = input("Enter sid : ")
    with open(path, "r") as file:
        file_content = file.read()
    print(file_content)

    lines = file_content.split('\n')

    for line in lines:
        if f'sid:{sid}' in line:
            print(line)
        

# original_cotent = []
# for line in file_content:
#     if f'sid:{sid}' in line:
#         original_cotent = line
#         break




path = '/etc/snort/rules/local.rules'
