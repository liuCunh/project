## display: list-item  
设置为该属性值得盒子，本质上仍然是一个块盒，但同时该盒子会附带另外一个盒子。元素本身生产的盒子叫做主盒子。附带的盒子称为次盒子，次盒子和主盒子水平排列  
调整次盒子属性：
  
	list-style-type: none; 设置次盒子中内容的类型
	list-style-position: outside; 设置次盒子相对于主盒子的位置
	list-style: 样式 位置; 速写属性。两个一起写
	list-style: none; 清空次盒子

## 图片失效时的宽高问题  
如果img元素的图片链接无效，img元素的特性和普通行盒一样，无法设置宽高

## 行盒中包含行块盒或可替换元素  
行盒的高度与他内部的行块盒或可替换元素的高度无关

## text-align: justify

	text-align: left; 左对齐
	text-align: right; 右对齐
	text-align: center; 居中
	text-align: justify; 除最后一行外，分散对齐

## 制作一个三角形

	.triangle{
		width: 0;
		height: 0;
		border: 100px solid transparent;
		border-left-color: chocolate;
	}
	
## direction 和 writing-mode  
	
	direction: rtf; 文字从右边往左边排列
	writing-mode: rl; 从右侧开始排列

## uft-8字符  

`&#x5218;&#x6625;`
