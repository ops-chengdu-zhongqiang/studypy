基础命令安装
---
**1. 获取pip**
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
配置：
vim ~/.pip/pip.conf
`[global]
index-url = http://pypi.douban.com/simple
trusted-host = pypi.douban.com
`
**验证**：下载一个包，查看是否从douban获取的

**2.安装ipython**
pip install ipython

**3.安装virtualenv**
pip install virtualenv
**功能：**为每个项目建立不同的/独立的Python环境，为每个项目安装所有需要的软件包到它们各自独立的环境

**4.安装virtualenvwrapper**
pip install virtualenvwrapper
**功能：**virtualenvwrapper 是一个建立在 virtualenv 上的工具，通过它可以方便的创建/激活/管理/销毁虚拟环境
**配置：**
 Vim ~/.bashrc或者(/etc/profile)  # 追加以下内容
>if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
fi
source ~/.bashrc 
>

项目管理
---

新建/激活/关闭/删除虚拟空间需要执行下面的命令：
> * mkvirtualenv IDC      新建虚拟空间
> * workon IDC               激活进入空间，标识为对应的命令空间里（IDC）Air%
> * deactivate                 关闭空间
> * rmvirtualenv IDC      删除释放空间


命令行中在对应的虚拟空间中运行项目：
 > * workon IDC
 > * cd IDC
 > * cd demo_app
 > * pip install -r requiremenets.txt
 > * python manage.py runserver  0.0.0.0:8080

**多项目管理**
•	安装当前项目中所有所需要的依赖文件应用
-	pip install -r requiremenets.txt
•	导出当前项目中所有所需要的依赖文件应用
-	pip freeze > requirements.txt（覆盖前最好先备份）
•	查看当前项目中所有所需要的依赖文件应用
-	pip list
- pip uninstall

**GitHub使用**
0.安装git
1.自己账户申请，加入到对应的组里面
2.fork对应项目到自己的git里面
3.通过 git clone  https://github.com/ttxgoto/IDC.git  拉取项目到本地环境中  （github有两种同步方式，http和ssh）


Eclipse+Pydev安装
---
1.安装jdk，双击运行jdk-8u40-macosx-x64.1427945120.dmg完成
2.解压运行eclipse-jee-mars-2-macosx-cocoa-x86_64.tar完成
3.安装pydev：help->Install New Software->work with(pydev - http://pydev.org/updates)选择安装完成
4.配置环境：

* 创建项目运行虚拟空间： mkvirtualenv IDC ；注意查看生成文件路径，下面会使用 ,可通过workon来查看已有的工作空间
* 添加虚拟环境：Eclipse->偏好设置->Pydev->Python interpreter-New-Save  (这里的环境路径为自定义的虚拟空间.virtualenvs/IDC/bin/python)
![py01](./images/py01.jpg)
* 项目中使用虚拟空间，在对应项目中点击右键：Properties-PyDev-Interpreter
![py02](./images/py02.jpg)























