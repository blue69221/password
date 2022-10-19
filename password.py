key = 'a123456'
x = 0

while x < 3:
    password = input('請輸入使用密碼：')
    if password == key:
        print('登入成功')
    else:
        x += 1
        print(f'密碼錯誤! 還有 {3 - x} 次機會')
print('帳號鎖定，請洽詢相關人員')


