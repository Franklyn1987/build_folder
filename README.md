# 用于批量生成文件夹

### 安装方法

下载setup.py和build_folder.py在同一文件夹,在terminal对话框中输入

```cmd
Python setup.py install
```

库的使用方法

```python
import build_folder as bd
bd.build_folder(r"D:\note.txt","D:\test",False)
```

**参数1**为需要生成的文件夹名称列表所在txt文档地址；

**参数2**为生成所有的文件夹所在的总目录；

**参数3**为选择是否生成对应的注释文档，False改为True，则同时生成相应的txt注释文档。