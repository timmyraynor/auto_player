## YYS 阴阳师自动挂机
![Demo](GUI.png)
挂机逻辑编辑器，通过OpenCV 识别局部截图，然后利用如上的编辑器生成具体的脚本操作内容。
通过python来执行识别和模拟按键。


### 如何开始
本工具分为2个部分：
1. GUI图形界面部分帮忙创建配置自动工作流的json文件。
2. 实际的脚本执行模块，由python通过opencv库来做实际的图片截屏比对然后带动鼠标按键。

#### GUI 图形部分
需要安装nodejs。具体安装方法参考网上教程。
之后进入gui 文件夹

````shell
cd gui
npm install
node app.js
...
Example app listening at http://localhost:3000
````

这个时候通过浏览器进入 `localhost:3000` 即可进入编辑页面。

编辑页面很简单，您需要执行的逻辑都是由一个个node构成。拖动左侧的Node到画布上就可以看到对应的操作节点。
操作节点有如下属性：
1. screenshots - 需要捕捉的截图名称，可以有多个匹配，用逗号分隔（截图部分应该放在wanted文件夹中）
2. seqid - 自动生成的序列号，如果多个序列号出现在下游，序列号小的截图内容优先被识别
3. tick - 是否跳数，如果有固定次数限制的操作，可以通过tick = True来触发计数
4. sleep time - 此次操作结束后休息多久
5. response - 在命令执行到这一步的时候输出什么到屏幕上

每个节点有一个输入口和一个输出口，输入和输出决定了节点执行的顺序。 在第一次执行的时候，程序会将所有命令按顺序排序然后都探查一遍直到找到第一个符合的图片，所以可以在运行过程中的任意一环执行程序。

配置完成后，点击右上角的export按钮，就可以导出配置文件。这时候将会有2个json文件生成:
1. graph.json - 纯粹的图形逻辑json文件，用于下次变更的时候通过node下面的`choose file`按钮导入从而进行二次编辑，**不要用这个graph.json作为您的模板文件来执行后面的Python!!!!**
2. auto.json - 导出的配置文件，导出后放到logics文件夹下，就可以进行后面的python命令自动化了


#### python 执行部分
建议使用python的virtual env。
需要安装如下内容:

````shell
pip install opencv-python pyautogui pyscreenshot numpy imutils Pillow
````

安装完成后，可以通过python启动脚本。

````shell
python yys_desktop_auto.py
程序启动，当前时间 Tue May 25 18:08:27 2021

0: 获取当前屏幕截图

1: 自动刷图_御魂

2: 自动刷图_探险

3: 自动刷碎片

4: 自动结界突破

5: 自动日常

6: 动态读取配置

7: 测试

选择功能模式：6
已选择功能： 动态读取配置
选择读取模板：auto-tupo.json
````

在这里就输入您生成的配置文件，如例子中的`auto-tupo.json`.
