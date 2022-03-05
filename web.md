/*
 * Filename: d:\allworkspace\web\web.md
 * Path: d:\allworkspace\web
 * Created Date: Monday, February 28th 2022, 3:54:13 pm
 * Author: Dive
 * 
 * Copyright (c) 2022 Sequence Group
 */
########################### [head] ###########################

# base 基础位置
href = "https://www.google.com" 基础链接
target = "_blank" 新界面打开方式

# meta 元数据
charst = "utf-8" 字符集
name = "keywords" 关键字 content = "keywords"
name = "description" 描述 content = "description"

# link 链接文档和css，js
rel = "stylesheet" href = "sample.css"

# 实体
空格 = "&nbsp;"
大于 = "&gt;"
小于 = "&lt;"
乘号 = "&times;"
除号 = "&divide;"
双引号 = "&quot;"
单引号 = "&apos;"
度数 = "&deg;"
版权 = "&copy;"
注册商标 = "&reg;"


########################### [body] ###########################

# p 段落

# h1 h2 h3 h4 h5 h6 标题

# hr 分割线
# br 换行

# i 斜体
# b strong 加粗

# sup sub 上标 下标
# del ins 删除线 插入线

# pre 预格式化

# <ol type = "a,A,i,I,1"> li 有序列表
# <ul type = "disc实心,circle空心,square方形"> li 无序列表
# <dl> <dt词条> <dd词条定义> 定义列表

# img 图片
src = "https://www.google.com/images/color_272x92dp.png"
src = "sample.png"

# a 链接
href = "https://www.google.com"
herf = "#内部区域名"
name = "区域名"
target = "_blank" 新界面
target = "_self" 当前界面
target = "_parent" 父界面
target = "_top" 顶层界面

# table 表格
# tr 行
# th 表头
# td 单元格
# caption 标题

# iframe 嵌入
src = "https://www.google.com"

# <div id = "id_name"></div> 容器

# span 文本容器 内联标签

# header 页眉
# footer 页脚
# nav 导航
# section 节
# atricle 文章
# aside 侧边栏

# mark 强调
# progress 进度条
# <meter value = "实际数值" min = "最小值" max = "最大值" low = "较低范围" high = "较高范围" optimum = "最佳值"></meter> 计量器


########################### [css] ###########################

# #id_name {} id选择器
# .class_name {} class选择器
# a[href]{} 属性选择器  

# px 像素 vw 视窗宽度 vh 视窗高度

# [position]
absolute 绝对定位 top left right bottom
relative 相对定位

# padding-top padding-bottom padding-left padding-right 内边距
# border-width 边框宽度
# border-style 边框样式
# border-color 边框颜色
# margin 外边距

# color: #000000; 字体颜色
# background-color: #000000; 背景颜色

# background-image: url(sample.png); 背景图片
# background-repeat: no-repeat不平铺 repeat-x水平平铺 repeat-y 垂直平铺 repeat 双向平铺; 背景重复
# background-size: cover; 背景填充
# background-position: center居中 top置顶 bottom置底 left左 right右; 背景位置 可以使用%
# background-attachment: fixed固定 scroll滚动; 背景固定

# width: 100px; 宽度
# height: 100px; 高度


# font-size: 12px; 字体大小
# font-family: 字体; 字体
# font-weight: bold; 加粗
# font-style: italic; 斜体

# text-decoration: underline; 下划线
# text-decoration: line-through; 删除线

# text-align: left; 左对齐
# text-align: right; 右对齐
# text-align: center; 居中
# text-align: justify; 两端对齐
# text-indent: 10px; 文本缩进

# line-height: 1.5; 行高
# letter-spacing: 1px; 字间距
# word-spacing: 1px; 单词间距

# text-transform: uppercase; 字母转换为大写

# [a]
a:link {color: #0000FF;} 未被访问的链接
a:visited {color: #0000FF;} 已被访问的链接
a:hover {color: #FF0000;} 鼠标指针移动到链接上
a:active {color: #0000FF;} 正在被点击的链接


