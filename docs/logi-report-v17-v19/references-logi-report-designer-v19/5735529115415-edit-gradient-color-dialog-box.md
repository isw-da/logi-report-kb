---
title: "Edit Gradient Color Dialog Box"
id: 5735529115415
section: "References - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735529115415-Edit-Gradient-Color-Dialog-Box
updated_at: 2022-11-02T08:20:23Z
---

# Edit Gradient Color Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565634071-Edit-Filter-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522562071-Edit-Group-Dialog-Box)

# Edit Gradient Color Dialog Box

You can use the Edit Gradient Color dialog box to [specify the gradient color you want to apply to markers or areas of a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/5735512449175-Inserting-Geographic-Maps-in-a-Report#Color). This topic describes the options in the dialog box.

Designer displays the Edit Gradient Color dialog box when you select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/7933707090327/btn_colr.gif) beside the Color By or Fill By text box after adding an aggregation object to the text box in the Display screen of the [Create Geographic Map dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735513407639-Create-Geographic-Map-Dialog-Box#Web) or [Geographic Map Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735514503703-Geographic-Map-Wizard-Dialog-Box#Web).

![Edit Gradient Color dialog box](https://devnet.logianalytics.com/hc/article_attachments/7933729241879/edtgrdntclr.gif)

Designer displays these options:

**Gradient color drop-down list**

This drop-down list contains the gradient colors you can apply to markers or areas of the geographic map. Select the gradient color you need.

**Color bar**

The bar displays the colors in the selected gradient. You can customize the starting color, middle color, and ending color of the gradient by selecting the corresponding triangle below the color bar to select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette).

**Reversed**

Select to reverse the direction of the gradient.

**Middle Value**

Designer enables this option when the selected gradient has a middle color. When it is cleared by default, Designer maps the middle value between the start value and end value to the middle color. You can select it to customize the value you want to map to the middle color.

* **Auto Expand Start/End Value**  
  Designer displays this option when you set Middle Value to 0. Select it if you want to expand the start value and end value automatically. When you select this option, it means 0 is the separator of negative and positive values. Designer maps the negative and positive values of the maximum absolute value to the starting color and ending color, and 0 is always in the middle of the data range.

**Color of Null Values**

Specify the color for null values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/5735570054167-Menu-Tabs#Palette), or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Gradient By**

This drop-down list contains the algorithms you can apply to colors of the gradient. Select the algorithm you want to use.

* **Auto**  
  Select to use the default algorithm according to the type of the gradient. For single color, Designer applies the RGB linear algorithm; for start-end color, Designer applies the HSL linear algorithm; for start-middle-end color, Designer applies the HSL linear algorithm separately between the start-middle color and middle-end color.
* **RGB**  
  Select to use the RGB linear algorithm, which uses red, green, and blue as the algorithm parameters.
* **HSL**  
  Select to use the HSL linear algorithm, which uses hue, saturation, and lightness as the algorithm parameters.

**Opacity**

Specify the opacity of the gradient.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/7933644552087/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735565634071-Edit-Filter-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/7933656663191/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735522562071-Edit-Group-Dialog-Box)
