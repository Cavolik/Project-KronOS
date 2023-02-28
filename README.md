# KronOS


Controlpanel schematic
![image](https://user-images.githubusercontent.com/101195373/213676072-0f77928e-b04e-41bc-a653-855acdb3036a.png)


Raspberry pi to control panel conetion

               3V3  (1) (2)  5V       
             GPIO2  (3) (4)  5V - exp1 10
             GPIO3  (5) (6)  GND - exp1 9
             GPIO4  (7) (8)  GPIO14
               GND  (9) (10) GPIO15
    exp1 3 - GPIO17 (11) (12) GPIO1
    exp1 5 - GPIO27 (13) (14) GND   
   exp1 6 - GPIO22 (15) (16) GPIO23 - exp1 2
               3V3 (17) (18) GPIO24 - exp2 3 
   exp1 7 - GPIO10 (19) (20) GND   
      exp8 - GPIO9 (21) (22) GPIO25 - exp2 5
   exp1 4 - GPIO11 (23) (24) GPIO8 
               GND (25) (26) GPIO7 
             GPIO0 (27) (28) GPIO1 
             GPIO5 (29) (30) GND   
             GPIO6 (31) (32) GPIO12 - exp2 8
            GPIO13 (33) (34) GND   
            GPIO19 (35) (36) GPIO16
   exp1 1 - GPIO26 (37) (38) GPIO20
               GND (39) (40) GPIO21
