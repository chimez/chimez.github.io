+++
title = "使用 latexmk 自动执行编译"
date = 2019-09-20T00:00:00+08:00
tags = ["latex"]
categories = ["计算机"]
draft = false
+++

## 解释 {#解释}

```nil
$pdf_mode = 1;
```

默认使用 `pdflatex` 命令，下面重载命令的内容。

```nil
$pdflatex = "xelatex -file-line-error -halt-on-error -interaction=nonstopmode --shell-escape -src-specials -synctex=1 %O %S;cp %D %R.pdf";
```

实际使用 `xelatex` 命令，其中

1.  `-file-line-error` 使报错输出文件和行号；
2.  `-halt-on-error` 和 `-interaction=nonstopmode` 使编译遇到错误时立即停止；
3.  `-synctex=1` 则开启 synctex 的功能;
4.  `--shell-escape` 关闭 `\write18`;
5.  `-src-specials` 向 xdv 中插入代码;
6.  `%O` 选项
7.  `%S` tex 源文件
8.  `%D` 目标文件
9.  `%R` 根文件名，即源文件去掉后缀

<!--listend-->

```nil
$recorder = 1;
```

传递 `-recoder` 选项，生成 fls 文件，追踪生成文件的过程。

```nil
$pdf_previewer = "xdg-open %S";
```

```nil
$pdf_update_method = 0;
```

pdf 文件改变时让阅读器改变

```nil
$clean_ext = "synctex.gz acn acr alg aux bbl bcf blg brf fdb_latexmk glg glo gls idx ilg ind ist lof log lot out run.xml toc dvi";
```

需要清理的后缀文件名

```nil
$bibtex_use = 1.5;
```

自动决定运行一遍还是两遍 bibtex

```nil
$out_dir = "temp";
```

把所有中间文件都放到 temp 文件夹里


## 完整脚本 {#完整脚本}

```nil
$pdf_mode = 1;
$pdflatex = "xelatex -file-line-error -halt-on-error --shell-escape -src-specials -synctex=1 -interaction=nonstopmode %O %S;cp %D %R.pdf";
$recorder = 1;
$pdf_previewer = "xdg-open %S";
$pdf_update_method = 0;
$clean_ext = "synctex.gz acn acr alg aux bbl bcf blg brf fdb_latexmk glg glo gls idx ilg ind ist lof log lot out run.xml toc dvi";
$bibtex_use = 1.5;
$out_dir = "temp";
```
