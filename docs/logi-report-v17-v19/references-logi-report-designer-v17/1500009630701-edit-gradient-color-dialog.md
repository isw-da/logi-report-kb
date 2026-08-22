---
title: "Edit Gradient Color Dialog"
id: 1500009630701
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009630701-Edit-Gradient-Color-Dialog
updated_at: 2021-07-24T16:04:47Z
---

# Edit Gradient Color Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630681-Edit-Filter-Control-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630721-Edit-Group-Dialog)

# Edit Gradient Color Dialog

The Edit Gradient Color dialog helps you to [specify a gradient color for the markers or areas in a geographic map](https://devnet.logianalytics.com/hc/en-us/articles/1500009629161-Inserting-Geographic-Maps-in-a-Report#Color). It appears when you select the button ![Color button](https://devnet.logianalytics.com/hc/article_attachments/4404904276119/btn_colr.gif) beside the Color By or Fill By text box when an aggregation field has been added to the text box in the Display screen of the map wizard.

![Edit Gradient Color dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916806551/edtgrdntclr.gif)

The following are details about options in the dialog:

**Gradient color drop-down list**

Specifies the gradient color to be used.

**Color bar**

Displays the colors in the selected gradient color.

The gradient start color, middle color and end color can be customized. Select the corresponding triangle below the color bar to select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette). Select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404904350743/btn_rmv2.gif) to delete the middle color or start color if not needed. If the start color is deleted, a default start color will be applied automatically. Select **+** to specify the start color or middle color again. The middle color cannot be deleted or added when there is no start color. After you change a default gradient color, it will be saved as a customized gradient color and you will find the name changed to Customize in the color drop-down list.

**Reversed**

Reverses the direction of the gradient color.

**Middle Value**

Specifies whether to set the middle data value mapping to the middle color. It takes effect only when the middle color is not null. If the option is unselected, the center value between the start value and end value will be used to map to the middle color. If the option is selected, the value you specify will be used to map to the middle color. Note that the value will be ignored if it is not between the start value and end value.

* **Auto Expand Start/End Value**  
  Specifies whether to expand the start value and end value automatically. Available only when the Middle Value is set to 0. If the option is selected, it means 0 is the separator of positive values and negative values. The negative and positive values of the maximum absolute value will be used to map to the start color and end color, and 0 will always be in the center of the data range.

**Color of Null Values**

Specifies the color for null values. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Gradient By**

Specifies the gradient color algorithm between two colors.

* **Auto**  
  Specifies to use the default algorithm according to different kinds of gradient colors automatically. For single color, RGB linear algorithm will be used. For start-end color, HSL linear algorithm will be used. For start-middle-end color, HSL linear algorithm will be used separately between the start-middle color and middle-end color.
* **RGB**  
  Specifies to use RGB linear algorithm, which uses red, green, and blue as the algorithm parameters.
* **HSL**  
   Specifies to use HSL linear algorithm, which uses hue, saturation, and lightness as the algorithm parameters.

**Opacity**

Specifies the opacity of the gradient color.

**OK**

Applies the specified gradient color to the markers or areas and closes the dialog.

**Cancel**

Cancels the operation and closes the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009630681-Edit-Filter-Control-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009630721-Edit-Group-Dialog)
