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
location /love-in-anchor/ {
	proxy_pass http://127.0.0.1:port/;
}
```

---

#### 安装依赖

```
pip install -r requirements.txt
```

---

#### 运行

```
python init.py
nohup gunicorn -w 4 -b 127.0.0.1:port app:app >/dev/null 2>&1 &
```