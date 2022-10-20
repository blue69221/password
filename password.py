password = 'a123456'
i = 3 # 剩餘機會

while i > 0:
    i -= 1
    pwd = input('請輸入密碼：')
    if pwd == password:
        print('登入成功')
        break # 離開迴圈
    else:
        print('密碼錯誤')
        if i > 0:
            print(f'還有 {i} 次機會')
        else:
            print('密碼錯誤過多，請洽詢相關人員')



