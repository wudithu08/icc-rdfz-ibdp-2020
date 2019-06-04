# 黑洞成像原理

## 黑洞是什么

* 巨大质量的物体 强大引力场 
* 没有物体可以逃逸 - 甚至是光

## 黑洞大概长什么样

* zoom into the radio wavelength 
    * we expect to see a ring of light casued by the gravitational lensing of hot plasma zipping around the black hole
    * black hole cast a shadow on the background of light matrial

## 黑洞真的不可见么

* 由于没有光能从黑洞中逃逸出来 我们看的的黑洞呈现的颜色 其实并不是黑洞本身的颜色(黑洞本身并没有颜色apparently)
* 现在看到的黑洞的颜色 是根据测量黑洞发射出的不可见电磁波 分析patch形成定量的信息数据 再用可见光进行illustrate(染色)后形成的

## 给黑洞拍照的困难

### 困难一： 拍摄
* 选取距离合适的黑洞进行观察
* 黑洞距离我们的距离非常的远 according to diffraction 我们需要直径比地球还大的望远镜进行直接观测
* 因此 通过连接全球的8架天文望远镜 并以原子钟统一时间 黑洞被拍摄成了200万GB的零散的画面

### 困难二： 冲洗

* 在获得了无数黑洞的小照片后 我们需要讲这些照片拼接成原本的黑洞 再将缺失的部分通过算法进行补全
* 算法的本质 损坏图像的修复
* Katie Bouman 
* Reconstract 黑洞的算法
    ![avatar](min.png)
    * 最小二乘法
    * 加入正则项 处理观测噪音
    * 根据多组不同图片 机器学习优化正则项
    
