# OPQBot原神微博插件
此插件是获取原神微博的插件，因为我不会用python来直接发送QQ消息，所以这个插件是python来获取，lua来发送qwq

<br>

（因为python我不是特别精通，所以写了和生成了很多文件，如果有大佬知道怎么优化还请能pull分支一下，非常感谢qwq）

## 路径
因为不是用python来直接发送QQ消息，而OPQBot的lua插件好像不能直接访问本地目录，所以我们是使用的访问网址来获取生成的图片

<br>

也就是说，稍等您需要修改py文件的**生成路径**,将您的**生成路径**修改到可以使用**IP/域名访问**的文件夹，然后再将**访问图片的URL**填写到相关位置

<br>

需要修改的文件分别是**weibo-genshin.lua**和**genshinweibo/getfull.py**，具体的操作可以看这两个文件的注解qwq，如果还不会可以issues！qwq

## 前置（针对于萌新，大佬可以跳过了qwq）
因为使用了一堆前置，所以还希望您能先以以下的流程来测试有没有缺少前置
<br>

(此命令基于centos7 **只有一个python2** 的情况，如果是 **python3** 或者是 **多个python** 请适当修改一下命令)

```sh
#1.运行getweibo.py

cd 你的OPQbot根目录下
cd ./Plugins/genshinweibo
pip install pyquery
python getweibo.py

#如果出现什么name什么的错误请复制错误并且上网百度来pip install这个前置

#2.运行changejson.py

pip install pytest-shutil
python changejson.py

#3.运行getfull.py

pip install bs4
python getfull.py
```
如果上述命令运行后没有错误了，那么说明已经可以使用了qwq

<br>

现在您就可以直接设置定时任务：比如每隔半个小时运行```run.sh```即可


## 文件目录及文件解释
|
|-weibo-genshin.lua
|-genshinweibo
    |-changejson.py
    |-getfull.py
    |-getweibo.py
    |-msyh.ttc
    |-run.sh
    |-runafter.sh
    |-weibo.json
    |-weibo.txt
    |-weibo1.json

其中，run.sh运行的是通过weiboAPI获得最新的博文，而runafter.sh则是运行的获取博文全文并且转换成图片

下面来说说**具体流程**

weibo.txt是getweibo.py通过weiboAPI获取的微博博文ID，然后运行changejson.py来规范json语法并且只读取最新的博文id（因为置顶占用最新的id所以只要获取第二行的id既是最新博文）

在changejson.py会对比weibo.json与weibo1.json的id（也就是看到底是不是最新的，这样有助于减少使用量）如果是最新的就不会进行操作并且输出提示，如果不是最新的则会将weibo.json复制成weibo1.json

而且运行runafter.sh，进而运行getfull.py，在getfull.py中，会通过weiboAPI获取正文并且转换成图片，提供给weibo-genshin.lua使用

## BUG反馈

您可以提交issues或者去往论坛[点击这里](http://sakura-forum.pysio.online/t/github-bug)来告诉我qwq

### readme统计

![统计](https://count.getloli.com/get/@misaka10843?theme=elbooru)
