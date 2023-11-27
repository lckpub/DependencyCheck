使用说明：
首先，由于本作品是以web平台服务用户的，故源代码是面向我们使用的服务器的。若要运行源代码，需要修改内容。
1.将workspace设在app.py所在的目录下（默认是在codes），并确保UnRAR.exe在workspace目录存在。
2.在app.py中，import代码下面有一行是初始化base全局变量，存储的是app.py所在的目录，也就是workspace。下载代码后将base改成workspace目录。
3.由于html中的超链接是链接向服务器的外网IP的，故若需要在本地跑源代码，还需要修改html里的超链接，修改成127.0.0.1：（端口）的形式。

若要连接服务器进行测试，有两种方法，手动/自动测试。
手动测试1：
1.可以自己选定项目文件，根据报告中的说明或是网页主页面的说明，使用pipreqs在文件目录下生成requirements.txt，放在python代码项目的目录下，打包生成压缩文件，上传。
2.选择许可证类型（默认是gpl-2.0)，点击扫描按钮即可。
手动测试2：
1.也可以使用和源代码一起上传的test.rar，这是我们提供的测试文件，直接上传，使用默认的gpl-2.0许可证，点击扫描即可。
自动测试：
源代码中包含auto.py，此文件并非服务器的组成部分，而是自动化测试的代码文件。
1.将workspace设为auto.py所在的目录（不需要和其他代码文件共存），并将test.rar放在workspace目录下（和auto.py同一目录）
2.运行auto.py即可看到产生一个网页窗口，执行自动化测试，自动执行手动测试2的流程。

Instructions:
Firstly, since this work is web platform-based serving users, the source code is oriented towards the servers we use. To run the source code, modifications are necessary.

1.Set the workspace in the directory where app.py is located (default is in 'codes'), and ensure that UnRAR.exe exists in the workspace directory.
2.In app.py, there is a line under the import code that initializes the global variable 'base', which stores the directory of app.py, i.e., workspace. After downloading the code, change 'base' to the workspace directory.
3.As the hyperlinks in the HTML link to the server's external internet IP, if you need to run the source code locally, you also need to modify the hyperlinks in the HTML to the form of 127.0.0.1:(port).
To connect to the server for testing, there are two methods: manual/automatic testing.
Manual Testing 1:

1.You can select a project file on your own. According to the instructions in the report or the main page of the website, use pipreqs in the file directory to generate a requirements.txt, place it in the directory of the python code project, package it into a zip file, and upload.
2.Choose the license type (default is GPL-2.0) and click the scan button.
Manual Testing 2:
1.You can also use the test.rar that is uploaded along with the source code. This is a test file we provide. Upload it directly, use the default GPL-2.0 license, and click scan.
Automatic Testing:
The source code includes auto.py. This file is not part of the server but is for automated testing.
1.Set the workspace to the directory where auto.py is located (it does not need to coexist with other code files), and place test.rar in the workspace directory (in the same directory as auto.py).
2.Run auto.py to see a web page window generated, conducting automated testing, automatically performing the process of Manual Testing 2.
