@echo off
echo 开始安装
echo ***********************************安装库
echo 中国科技大学
echo 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
echo 升级pip*******************************************
python -m pip install --upgrade pip

pip install requests -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install tkinter -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install lxml -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install copyheaders -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install jsonpath -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install PyQt5 -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install fake_useragent -i https://pypi.mirrors.ustc.edu.cn/simple/
pip install aiohttp -i https://pypi.mirrors.ustc.edu.cn/simple/


echo 安装完成
pause

