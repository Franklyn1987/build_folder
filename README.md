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

如果False改为True，则同时生成相应的txt注释文档
