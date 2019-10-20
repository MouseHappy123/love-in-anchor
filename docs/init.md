### 初始化

#### 配置文件 

`./config.py`

- ##### 数据库配置：host,username,password,database 

- ##### 活动时间：begin,end

---

#### secret_key：

```py
import os
os.urandom(12).hex()
```

---

#### nginx配置：

```
location /love_in_anchor/api/ {
	proxy_pass http://127.0.0.1:port/;
}
```

---

#### 运行

```
python init.py
gunicorn -w 4 -b 127.0.0.1:port app:app
```