基于selenuim2的web自动化测试框架

1.项目简介



2.环境依赖：

    pip3 install -r requirements.txt


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
        |---- venv层                     环境层，放windows环境下的虚拟环境
        |---- ReadMe.md                  项目介绍文件，可以用于项目介绍和后期项目功能备注
        |---- requirements.txt           项目依赖文件，使用pip3 install -r requirements.txt
        |---- run.py                     项目执行入口







4.case执行思路
    
    1. runner -> testsuites -> testcase -> page -> runcase
    2. page中创建并保存各个页面的元素对象,重构各个操作业务流代码
        其中，__init__：识别并保存页面对象
    3. testcase中调用具体的业务流函数就OK了
    4. 数据驱动，利用ddt框架实现，具体见test_searche
    5. 业务流测试，无须做参数化

5.后期优化

    1. 增加日志功能，测试每一个步骤记录日志
    2. _增加失败自检功能（异常处理）_，如，失败三次时录日志和截图，避免出现不必要的代码bug 类似于testng失败重跑 *
        - 已完成，参照https://github.com/GoverSky/HTMLTestRunner/ 并修改源码实现，已修改其中某些BUG和某些样式问题
    3. _增加测试结果截图 * 修改htmlTestRunner实现
    4. _使用xmlrunner对接jenkins，使用jenkins自带模板 （-XXXX 废弃，改用htmltestrunner，实现单文件快速浏览和定位问题）
    5. 配置email模块，（具体是使用jenkins还是自己实现，待思考）
    6. _实现数据驱动 -- 利用ddt框架实现 *
    7. _统一异常处理 （-XXXX 废弃，异常时重跑case实现）
    8. 写大量case测试框架稳定性
    

6.参考
1. htmltestrunner参考： https://github.com/GoverSky/HTMLTestRunner/