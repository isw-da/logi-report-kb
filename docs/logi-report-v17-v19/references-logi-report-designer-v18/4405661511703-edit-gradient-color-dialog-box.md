---
title: "Edit Gradient Color Dialog Box"
id: 4405661511703
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661511703-Edit-Gradient-Color-Dialog-Box
updated_at: 2022-01-27T20:35:57Z
---

# Edit Gradient Color Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664459031-Edit-Filter-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661516183-Edit-Group-Dialog-Box)

# Edit Gradient Color Dialog Box

You can use the Edit Gradient Color dialog box to [specify a gradient color for the markers or areas in a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/4405661387159-Inserting-Geographic-Maps-in-a-Report#Color). This topic describes the options in the dialog box.

Designer displays the Edit Gradient Color dialog box when you select ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4420542157335/btn_colr.gif) beside the Color By or Fill By text box after adding an aggregation object to the text box in the Display screen of the [Create Geographic Map dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661484311-Create-Geographic-Map-Dialog-Box#Web) or [Geographic Map Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664512151-Geographic-Map-Wizard-Dialog-Box#Web).

![Edit Gradient Color dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556203287/edtgrdntclr.gif)

You see the following options in the dialog box:

**Gradient color drop-down list**

This drop-down list contains the gradient colors that you can apply to the markers or areas of the geographic map. Select the gradient color you need.

**Color bar**

The bar displays the colors in the selected gradient color.

You can customize the gradient start color, middle color, and end color. Select the corresponding triangle below the color bar to select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette). Select the trash can icon ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4420556203799/icon_trashcan.gif) to delete the middle color or start color if not needed. If you delete the start color, Designer applies a default start color automatically. Select the plus sign icon **+** to specify the start color or middle color again. You cannot delete the middle color or add it when there is no start color. After you change a default gradient color, Designer saves it as a customized gradient color and you can find its name changed to Customize in the color drop-down list.

**Reversed**

Select to reverse the direction of the gradient color.

**Middle Value**

This option takes effect only when the middle color is not null. When it is cleared by default, Designer maps the center value between the start value and end value to the middle color. You can select it and customize the value you want to map to the middle color (Designer ignores the value you specify if it is not between the start value and end value).

* **Auto Expand Start/End Value**  
  Designer displays this option when you set Middle Value to 0. Select it if you want to expand the start value and end value automatically. When you select this option, it means 0 is the separator of positive values and negative values. Designer maps the negative and positive values of the maximum absolute value to the start color and end color, and 0 is always in the center of the data range.

**Color of Null Values**

Specify the color for null values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/4405661953175-Menu-Tabs#Palette) or type the hexadecimal value of a color (for example, 0xff0000) in the text box.

**Gradient By**

This drop-down list contains the gradient color algorithms that you can apply between two colors. Select the algorithm you want to use.

* **Auto**  
  Select to use the default algorithm according to different kinds of gradient colors automatically. For single color, Designer applies the RGB linear algorithm; for start-end color, Designer applies the HSL linear algorithm; for start-middle-end color, Designer applies the HSL linear algorithm separately between the start-middle color and middle-end color.
* **RGB**  
  Select to use the RGB linear algorithm, which uses red, green, and blue as the algorithm parameters.
* **HSL**  
  Select to use the HSL linear algorithm, which uses hue, saturation, and lightness as the algorithm parameters.

**Opacity**

Specify the opacity of the gradient color.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664459031-Edit-Filter-Control-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661516183-Edit-Group-Dialog-Box)
