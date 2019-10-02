+++
title = "如何在 labview 中使用 dotnet 库"
date = 2019-10-02T00:00:00+08:00
tags = ["labview", "实验", "嵌入式"]
categories = ["计算机"]
draft = false
+++

## <span class="section-num">1</span> 目录结构 {#目录结构}

首先要把 dll 文件放到 labview 能找到的地方。最佳操作是先创建一个项目，也就是 `lvproj` 文件，以后编程都先打开这个，在项目里创建 `vi` 。然后在同一个文件夹里创建个 `lib` 之类的子文件夹，把 dll 都放到里面去，但注意文件夹不要嵌套，不然也指不定会发生啥。


## <span class="section-num">2</span> 创建带 UI 的类的实例 {#创建带-ui-的类的实例}

在前面板里创建，右键 -> `.Net & ActiveX` -> `.Net Container` ，放到合适的位置，再右键 `Insert .Net Control...` ，找到 dll 和相应的类即可。


## <span class="section-num">3</span> 创建不带 UI 的类的实例 {#创建不带-ui-的类的实例}

在后面板里创建，右键 -> `Connectivity` -> `.Net` -> `Constructor Node` ，之后选择相应的 dll 和类即可。


## <span class="section-num">4</span> 调用类的静态方法 {#调用类的静态方法}

在后面板里， 右键 -> `Connectivity` -> `.Net` -> `Invoke Node(.Net)` ，放到合适的位置，之后在它上面右键 -> `Select Class` -> `.Net` -> `Browse..` ，找到 dll 和类，再单击图标上的 `Method` 选择要用的方法即可。


## <span class="section-num">5</span> 调用类的方法 {#调用类的方法}

在后面板里， 右键 -> `Connectivity` -> `.Net` -> `Invoke Node(.Net)` ，放到合适的位置，之后把左侧 `reference` 线连接上，再单击图标上的 `Method` 选择要用的方法即可。


## <span class="section-num">6</span> 读写类的属性 {#读写类的属性}

在后面板里， 右键 -> `Connectivity` -> `.Net` -> `Property Node(.Net)` ，放到合适的位置，之后把左侧 `reference` 线连接上，再单击图标上的 `Property` 选择要用的方法即可。

在图标上右键，选择 `Change To Write` 或 `Change To Read` 能选择读或者写。
