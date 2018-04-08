[原文地址](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html)    
---
  
内容  
* [介绍](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#introduction)
* [是什么：Python,Python packages,Spyder,Anaconda](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#what-is-what-python-python-packages-spyder-anaconda)
    * [Python](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#python)
    * [Python packages(包)](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#python-packages)
    * [Spyder](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#spyder)
    * [Anaconda](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#anaconda)
* [安装](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#installation)
* [测试你的安装](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#test-your-installation)
    * [使用Spyder运行测试](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#running-the-tests-with-spyder)
    * [从控制台运行测试](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#running-the-tests-from-the-console)
    * [丢包](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#missing-packages)
* [在Anaconda安装中更新包](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#updating-packages-in-the-anaconda-installation)
* [相关教程](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#related-tutorials)
  
## [介绍](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id1)   
  

这些说明主要是为[南安普敦大学](https://www.southampton.ac.uk/)(UK)本科、研究生和[博士](http://ngcm.soton.ac.uk/)课程的学生提供的，以帮助他们在自己的计算机上安装Python 3，如果他们愿意的话，并支持他们学习编程和计算，以及随后的学习，特别是在工程、计算机科学和自然科学方面。  
这是2016/2017学年安装说明的**最新版本**。(我们在2014/2013中使用了Python2(！)的旧版本，[这里](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda-2014.html)有一个版本。)  
简而言之，我们建议使用[AnacondaPython发行版](https://www.anaconda.com/download/)。  
根据所提供信息的性质，随着时间的推移，这些信息可能会部分过时。供参考：这个迷你介绍是在9月份编写的，Anaconda4.1是可用的，Pythona3.5是默认的Python。  
  
## [是什么：Python,Python packages,Spyder,Anaconda](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id2)  
  
### [Python](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id3)  
  
Python 是
* *我们编写计算机程序的一种编程语言。这些程序将存储在结束<tt class="docutils literal">.py</tt>的文本文件中，例如<tt class="docutils literal">hello.py</tt>，其中可能包含：*  
    <pre class="literal-block">
    print("Hello World")
    </pre>    
Python 也是  
* 在Linux和OSX操作系统上，Python解释器程序称为<tt class="docutils literal">Python</tt>，因此我们可以以以下方式运行该程序 <tt class="docutils literal">hello.py</tt>：
    <pre class="literal-block">
    python hello.py
    </pre>  
这也适用于Windows，因为操作系统不需要<tt class="docutils literal">.exe</tt>扩展名。  
     
### [Python packages（包）](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id4)   
   
对于科学计算和计算模型，我们需要不属于Python标准库的其他库(所谓的_Packages_)。例如，这些允许我们创建原型，操作矩阵，并使用专门的数值方法。  
   
我们通常需要的包是
* <tt class="docutils literal">numpy</tt> (NUMeric Python)：矩阵与线性代数
* <tt class="docutils literal">scipy</tt> (SCIentific Python)：许多数值例程
* <tt class="docutils literal">matplotlib</tt>：(绘图库)创建数据图
  
为了我们的教学，我们还需要  
* <tt class="docutils literal">sympy</tt> (SYMbolic Python):符号计算
* <tt class="docutils literal">pytest</tt> (Python TESTing):代码测试框架 
  
<tt class="docutils literal">numpy</tt>、<tt class="docutils literal">scipy</tt>和<tt class="docutils literal">matplotlib</tt>包正在用Python构建计算工作的基石，并且非常广泛地传播。  
<tt class="docutils literal">Sympy</tt>有一个特殊的角色，因为它允许符号计算而不是数值计算。   
  
<tt class="docutils literal">pytest</tt>包和工具支持回归测试和测试驱动开发--这通常很重要，尤其是在计算研究和研究的最佳实践软件工程中。  
   
  
### [Spyder](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id5)  
  
Spyder ([主页](https://github.com/spyder-ide/spyder))是Python语言强大的交互式开发环境，具有高级编辑、交互测试、调试和内省功能。里面有一个单独的博客条目，提供了[Spyder的关键特性摘要](http://www.southampton.ac.uk/~fangohr/blog/spyder-the-python-ide.html)，这也可以作为Spyder的教程从内部Spyder(帮助->Spyder教程，英文（<tt class="docutils literal">Help</tt> -> 
<tt class="docutils literal">Spyder tutorial</tt>）)。   
   
名字“SPyDER”来自于"Scientific Python Development EnviRonment（科学Python开发环境）" (SPYDER)  
  
我们将使用它作为学习Python、编程和计算科学与工程的主要环境。有用的特性包括  
* 提供IPython(QT)控制台作为交互式提示符，它可以内联显示情节
* 能够从控制台中的编辑器执行代码片段
* 对编辑器中的文件进行连续解析，并提供有关潜在错误的可视警告
* 分步执行
* 可变资源管理器  
### [Anaconda](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id6)  
[Anaconda](http://docs.continuum.io/anaconda/） 是几个Python发行版之一。Python发行版提供Python解释器，以及Python包列表，有时还提供其他相关工具，如编辑器。AnacondaPython发行版最容易安装在南安普敦大学的学生计算机上，但其他发行版也提供了类似的功能。   
   

[AnacondaPython发行版提供的包](https://docs.continuum.io/anaconda/pkg-docs.html)包括我们需要的所有包，因此我们建议在这里使用Anaconda。    
   
   
AnacondaPython发行版的一个关键部分是[Spyder](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#spyder)，它是Python的交互式开发环境，包括一个编辑器。  
  
## [安装](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id7)  
一般来说，Python解释器的安装相当简单，但是安装额外的包可能有点繁琐。  
     
我们建议使用这些[安装说明](http://docs.continuum.io/anaconda/install.html)来安装[AnacondaPython发行版](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#anaconda)，而不是手动执行，它提供Python解释器本身和我们需要的所有包。  
  
Anaconda Python发行版可供Windows、OSX和Linux操作系统[下载](http://continuum.io/downloads)(免费)。  
    
对于Windows和OSX，您可以选择下载图形安装程序还是下一个基于图形的安装程序。如果您不知道终端(OSX)或命令提示符(Windows)是什么，那么最好选择图形版本。您希望安装默认建议(Python3.5，64位)。  
   
下载安装程序，启动它，然后按照说明执行。接受建议的默认值。  
  
(如果您正在使用Linux，并且很乐意使用您发行版的包管理器---您会知道您是谁---那么您可能会被建议在本地安装所需的软件包，而不是安装整个Anaconda发行版。)  
   
## [测试你的安装](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id8)  
一旦安装了[Anaconda](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#anaconda)或您选择的Python发行版，就可以下载这个测试程序并执行它。  
### [使用Spyder运行测试](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#running-the-tests-with-spyder)  
1. 启动Spyder
2. 下载文件 [http://www.soton.ac.uk/~fangohr/blog/code/python/soton-test-python-installation.py](http://www.southampton.ac.uk/~fangohr/blog/code/python/soton-test-python-installation.py)
3. 在Spyder里打开这个文件 <tt class="docutils literal">File</tt> -> <tt class="docutils literal">Open</tt> 
4. 运行文件并通过 <tt class="docutils literal">Run</tt> -> <tt class="docutils literal">Run</tt>.  
  如果您得到一个弹出窗口，您可以接受默认设置并单击 <tt class="docutils literal">run</tt> 按钮。     
   

你应该看到如下输出在Spyder的右下角（你也可以看到一个情节出现）：  
<pre class="literal-block">
Running using Python 3.5.1 |Anaconda 4.0.0 (x86_64)| (default, Dec  7 2015, 11:24:55)
[GCC 4.2.1 (Apple Inc. build 5577)]
Testing Python version-> py3.5 OK
Testing numpy...      -> numpy OK
Testing scipy ...     -> scipy OK
Testing matplotlib... -> pylab OK
Testing sympy         -> sympy OK
Testing pytest        -> pytest OK
</pre>   
如果测试程序生成这些输出，那么Python和列出的六个包很有可能正确安装。  
### [从控制台运行测试](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#running-the-tests-from-the-console)   
1. 打开控制台：  
      *  Windows:在搜索框（按键Windows键 + R）里敲出“ <tt class="docutils literal">cmd</tt> "
      *  Mac OS X: 在  <tt class="docutils literal">Applications</tt> 开启 <tt class="docutils literal">Terminal</tt>（在 <tt class="docutils literal">Utilities</tt> 文件夹里） 
      *  Linux:启动一个可用的shell，或者一个xTerm之类的shell。
2. 把这个[文件](http://www.southampton.ac.uk/~fangohr/blog/code/python/soton-test-python-installation.py)下载到你的机器上
3. 将目录更改为已下载文件的文件夹，然后键入：
    <pre class="literal-block">
    python soton-test-python-installation.py
    </pre>
  
如果所有测试都通过了，您应该看到类似于以下内容的输出：
    <pre class="literal-block">
    Running using Python 3.5.1 |Anaconda 4.0.0 (x86_64)| (default, Dec  7 2015, 11:24:55)
    [GCC 4.2.1 (Apple Inc. build 5577)]
    Testing Python version-> py3.5 OK
    Testing numpy...      -> numpy OK
    Testing scipy ...     -> scipy OK
    Testing matplotlib... -> pylab OK
    Testing sympy         -> sympy OK
    Testing pytest        -> pytest OK
    </pre>
 ### [丢包](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#missing-packages)  
   
如果您通过[Anaconda](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#anaconda)发行版以外的其他方式安装Python，并且例如，您只安装了<tt class="docutils literal">numpy</tt>,
<tt class="docutils literal">scipy</tt> 和
<tt class="docutils literal">matplotlib</tt> 包，程序的输出将是：
   
<pre class="literal-block">
Testing numpy...      -> numpy OK
Testing scipy...      -> scipy OK
Testing matplotlib... -> pylab OK
Testing sympy...      Could not import 'sympy' -> fail
Testing pytest...     Could not import 'pytest' -> fail
</pre>  
## [在Anaconda安装中更新包](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#updating-packages-in-the-anaconda-installation)  
 例如，要更新Spyder和python，请执行以下步骤：   
1. 打开终端（查看步骤一[从控制台运行测试](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#running-the-tests-from-the-console)）  
2. 通过在控制台中键入以下命令来更新<tt class="docutils literal">conda</tt> 程序(这将管理更新)：  
    <pre class="literal-block">
    conda update conda
    </pre>  
如果要求，请确认更新。可以列出多个包以进行更新。  
3.更新单个包，例如 <tt class="docutils literal">spyder</tt>:
  
<pre class="literal-block">
    conda update spyder
    </pre>
  
您可能需要更新的其他包包括 <tt class="docutils literal">ipython</tt>,
    <tt class="docutils literal"><span class="pre">ipython-qtconsole</span></tt> 和
    <tt class="docutils literal"><span class="pre">ipython-notebook</span></tt>. 。有关命令如下：
  
 <pre class="literal-block">
    conda update ipython ipython-qtconsole ipython-notebook
    </pre>
   
有关使用Conda包管理系统的详细信息，请参阅[Conda文档页](http://conda.pydata.org/docs/)。    
  

## [相关教程](http://www.southampton.ac.uk/~fangohr/blog/installation-of-python-spyder-numpy-sympy-scipy-pytest-matplotlib-via-anaconda.html#id13)  
  
2005年6月12日更新：如果你更喜欢通过Anaconda安装的视频，请查看[SteveHolden从2015开始的帖子](http://holdenweb.blogspot.co.uk/2015/02/how-to-get-almost-all-python-you-might.html)