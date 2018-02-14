# Windows系统基本配置查看器
## Summary
>使用Python编写的查看Windows系统CPU、安装内存大小(GB)、硬盘类型、本地硬盘大小(GB)、显卡型号以及显存(GB)的一个GUI小脚本程序。
## Note
> * 基于[`EasyGui`](http://easygui.sourceforge.net/)、[`wmi`](https://pypi.python.org/pypi/WMI)，确保这两个模块已经正确安装，其中，`wmi`依赖[`pywin32`](https://github.com/mhammond/pywin32/releases)
> * bin文件夹中的.exe文件可以**直接运行**，**不依赖Python环境**
> * EasyGUI建议使用最新版，我使用的是0.96，会出现点击右上角关闭按钮无反应情况，看论坛说用新版就没有问题，我并没有做测试
> * 程序能检测计算机已安装或已挂载的磁盘类型
> * 这是我学习Python的一个小程序
> * 参考资料：
> 1. [wmi官方文档](http://timgolden.me.uk/python/wmi/tutorial.html)
> 2. [wmi官方示例](http://timgolden.me.uk/python/wmi/cookbook.html)
> 3. [EasyGui学习文档【超详细中文版】鱼C工作室](http://bbs.fishc.com/thread-46069-1-1.html)
## Screen Shots
![](http://xxx.fishc.com/album/201802/01/000417pxdsd99xyy0lrd7l.png)
