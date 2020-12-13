# url_shortener
用flask建立一個簡單的短網址服務

## 使用方法
1. 建立venv，用pip or poetry導入套件
2. 建立mysql資料庫
3. 自訂.env檔案
``` 
FLASK_APP=url_shortener
FLASK_ENV=development
DATABASE_URL='mysql://使用者名稱:資料庫密碼@資料庫位址/資料庫名稱'
```
4. 啟動服務
``` 
flask run
```
5. 開啟網站就可以使用