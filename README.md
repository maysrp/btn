# btn
五向导航按键模块 micropython
# btn
五向导航按键模块 micropython

 说明  
 
0 上 1 下 2 左 3 右 4 中间按下 5 set 6 reset  

使用


|按键|esp32|
|-|-|
|COM|GND|
|UP|27|
|DWN|26|
|LFT|25|
|RHT|33|
|MID|32|
|SET|21|
|RST|19|



```
import btn
c=btn.Btn(27,26,25,33,32,21,19)
c.read()
#未按下为空列[],按下上[0],按下上+set [0,5]
```
