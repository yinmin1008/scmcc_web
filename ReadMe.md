基于selenuim2的web自动化测试框架

1.项目简介



2..环境依赖：
pip install -r requirements.txt


3.项目结构：

    scmcc_web:
    |---- config层                   配置层，放项目配置文件
    |---- data层                     数据层，放数据文件，把testcase参数化的文件放到这里，一般用xml、excel，好处是把数据与代码隔离开，数据驱动测试原则）
    |---- drivers层                  驱动层，放selenium2所需驱动，如ChromeDriver、FirefoxDrider等
    |---- log层                      日志层，放执行日志文件，如xxx.log,png等
    |---- report层                   报告层，放测试执行报告，后期自动发送Email功能所需文件的目录
    |---- scr层                      代码层，各种执行代码
    |       |---- test                      测试代码
    |       |       |---- case              测试用例
    |       |       |---- common            测试共用方法
    |       |       |---- page              po层，放页面对象，便于维护页面元素
    |       |       |---- suite             测试集合，用于组织测试用例
    |       |---- utils
    |---- ReadMe.md                  项目介绍文件，可以用于项目介绍和后期项目功能备注
    |---- run.py                     项目执行入口
