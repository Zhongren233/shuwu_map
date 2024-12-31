## [抱抱美食记](https://space.bilibili.com/3494372146416178/) 视频内探店可视化项目

杭州有美食探店UP，很好

UP贴心的给自己去过的店做了表格，很好

但还不够好，我想去之前打电话确认营业状态，并且规划一下吃完之后的行程，看看附近有什么。

于是我根据UP提供的表格，从高德地图获取了所有店铺的经纬度和电话（如果存在的话），将它维护成了结构化的JSON数据。

接下来只需要在[高德地图控制台](https://console.amap.com/dev/index)申请个key，就可以把所有的店铺扔在地图里了！

效果：
![image](https://github.com/user-attachments/assets/05d1fa55-9eb3-4951-bde4-6439a313b337)

### 如果你不想研究申请Key和部署网页

高德地图也有一个[地图小程序](https://wia.amap.com/) （感谢抱抱粉丝群群友@BIG余杰的发掘），可以允许批量导入数据。[（帮助文档）](https://lbs.amap.com/api/wia/tutorial/content/import)

我这里提供了一个`convert.py` 文件，可以把`store_data.json`里的数据转换成高德地图地图工作台要求的Excel格式。

可以登录高德地图账号，在[地图小程序](https://wia.amap.com/)里创建组织，然后导入python文件执行产出的Excel文件，然后手机端登录同一个高德账号，在【我的】->【更多工具】->【地图小程序】功能里即可看到所有地点。

导入后PC端查看效果：
![image](https://github.com/user-attachments/assets/f3a50257-5d00-43c5-ad1a-cb8c2b9ac356) 

APP端查看效果：
![acc7dd49fd58930c825ed7130270f429_720](https://github.com/user-attachments/assets/6396c387-6943-44d9-bc49-f9db3b6f93ab)

### 如何部署
- 在[高德地图控制台](https://console.amap.com/dev/index)申请一个有Web端(JS API)服务平台的key
- 替换`map.html`里`https://webapi.amap.com/maps?v=2.0&key=` 后面高德地图的key为你自己的key
- 找一个Web服务器并将`store_data.json`和`map.html`放到服务器的根目录 (例如在这两个文件所在目录执行`python -m http.server`)
- 浏览器打开`map.html`即可

### 如何贡献内容
首先在右上角fork这个仓库到你自己的账号里，然后开始修改：

#### 勘误
如果说实地探查，这个仓库里的店铺倒闭、转让、搬家，可以把错误信息加到`fix.txt`里，并且删掉`store_data.json`里对应的条目。

接下来提交pull request就可以了。

#### 补齐单个店铺
只需要 在`store_data.json`的数组里加一个新的对象，将店铺名称、地址填入对应的字段。

然后登录[高德地图坐标拾取器](https://lbs.amap.com/tools/picker)对店铺进行检索，如果检索不到也可以按地址检索，即可获取经纬度。

然后再从拾取器的接口返回、或者美团之类的App找到店铺电话。

最后把经纬度、电话、抱抱的视频地址、以及视频里提到的人均金额一起放到这个新对象。

接下来提交pull request就可以了。

#### 一次性补充很多店铺

我这里也有一个半成品爬虫可以用。

可以创建一个新的JSON文件，按`store_data.json`的字段格式，将你想补全的店铺的名字、地址维护到文件里。

你需要做的是从浏览器请求里抓取对`https://lbs.amap.com/AMapService/v3/place/text` 的**JSONP**请求。

并根据这个请求的param、header来补完项目里的`amap.py`文件，运行脚本，脚本会针对`store_data.json`里的name字段，发起批量检索并输出结果。

**你可以把读取的`store_data.json`改为你创建的文件名，避免重复检索已有的结果**。

接下来你需要做的是人工校对一下这些检索结果，确保地址和店名都和视频一样，而不是什么同名的分店，或者压根就是模糊搜索出来的错误结果。

最后，把新的名称、地址，以及对应的检索出来的经纬度、电话保存到`store_data.json`，再逐个找到对应的视频地址，把视频地址和视频里的人均金额（如有）合并到`store_data.json`。

提交pull request就可以了。


