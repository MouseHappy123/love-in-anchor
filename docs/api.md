## 爱上N主播接口文档

#### url: `./love-in-anchor/api`

### recruit

#### 提交报名信息

调用方式：**POST**

#### 请求参数

| 名称    | 类型    | 说明   |
| ------- | ------- | ------ |
| name    | String  | 姓名   |
| gender  | Integer | 性别   |
| grade   | String  | 年级   |
| college | String  | 学院   |
| campus  | Integer | 校区   |
| tele    | String  | 手机号 |
| time    | Array   | 时间   |

#### 返回参数

| 名称    | 类型    | 说明     |
| ------- | ------- | -------- |
| errcode | Integer | 错误码   |
| errmsg  | String  | 错误信息 |

#### 错误信息

`400`：`{"type":[name,gender,...],"msg":[某项为空,...,名字不规范,号码不规范]}`

`402`：`{"msg":"已报名","name":姓名,"tele":号码}`

`403`：数据库报错信息

`0`：报名成功

### judgeRecruit

#### 判断是否报名

调用方式：**POST**

#### 请求参数

| 名称 | 类型   | 说明 |
| ---- | ------ | ---- |
| tele | String | 号码 |

#### 返回参数

| 名称    | 类型    | 说明     |
| ------- | ------- | -------- |
| errcode | Integer | 错误码   |
| errmsg  | String  | 错误信息 |

#### 错误信息

`403`：数据库报错信息

`401`：还未报名

`402`：`{"msg":"已报名","name":姓名,"tele":号码}`



### colleges

#### 获取学院

调用方式：**POST**

#### 请求参数

| 名称   | 类型   | 说明 |
| ------ | ------ | ---- |
| campus | Integer | 校区 |

#### 返回参数

| 名称    | 类型    | 说明     |
| ------- | ------- | -------- |
| errcode | Integer | 错误码   |
| errmsg  | String  | 错误信息 |

#### 错误信息

`400`：数据库报错信息

`401`：未查询到

`0`：`[“计算机科学与工程学院”,"设计学院",...]`

### checkTime

#### 活动时间

调用方式：**GET**

#### 返回参数

| 名称    | 类型    | 说明     |
| ------- | ------- | -------- |
| errcode | Integer | 错误码   |
| errmsg  | String  | 错误信息 |

#### 错误信息

`400`：活动还未开始

`401`：活动已结束

`0`：

### checkLogin

#### 判断是否微信授权登录

调用方式：**GET**

#### 返回参数

| 名称    | 类型    | 说明     |
| ------- | ------- | -------- |
| errcode | Integer | 错误码   |
| errmsg  | String  | 错误信息 |

#### 错误信息


`400`：未授权登录

`0`：openid

### checkSubscribe

#### 判断是否关注公众号

调用方式：**GET**

#### 返回参数

| 名称    | 类型    | 说明     |
| ------- | ------- | -------- |
| errcode | Integer | 错误码   |
| errmsg  | String  | 错误信息 |

#### 错误信息

`400`：未授权登录

`401`：未关注

`0`：已关注

### innerQuery

#### 内部查询

调用方式：**POST**

#### 请求参数

| 名称     | 类型   | 必填 | 说明   |
| -------- | ------ | ---- | ------ |
| username | String | 是   | admin  |
| password | String | 是   | 123456 |

#### 返回参数

| 名称    | 类型 | 说明   |
| ------- | ---- | ------ |
| errcode | Int  | 错误码 |

#### 错误信息

`400`：用户名或密码错误

`0`：`[{"name":name,"gender":gender,"grade":grade,"college":college,"campus":campus,"tele":tele,"time":time}]`



