key = 'a123456'
i = 3

while i > 0:
    password = input('請輸入使用密碼：')
    if password == key:
        print('登入成功')
        break # 離開迴圈
    else:
        i -= 1
        print(f'密碼錯誤! 還有 {i} 次機會')
        if i == 0:
            print('密碼錯誤3次，請洽詢相關人員')



