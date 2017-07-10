# VAST2017_MC3_Process_data
This project is used for pre-process the data of [VAST 2017 mini challenge 3.](http://vacommunity.org/VAST+Challenge+2017+MC3)

The source data is csv files in the *Data* dictionary.

The data after processing is in the *Result* dictionary.

The name of result file follows:

| File Type | Format & Example                         |
| :-------- | :--------------------------------------- |
| Gray File | The name shows its meaning, for example, "b1.jpg" is the image of b1 band |
| RGB File  | The name is sorted by R\G\B, for example, "b1b2b3.jpg" shows that R channel is b1 band, G channel is b2 band, B channel is b3 band |

**How to use**

You should install python & numpy & scipy & opencv on your device.

If you have installed them, just run the *process.py*.