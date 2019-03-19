"""目标：扩展绝对路径"""

import os

print("获取当前文件所在的目录：", os.getcwd())
# os.sep :获取/或\ 根据操作系统不同获取不同的/
print("获取当前文件所在的目录：", os.getcwd()+os.sep)

