---
title: "Format Platform"
id: 1500009721842
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009721842-Format-Platform
updated_at: 2021-07-25T07:19:20Z
---

# Format Platform

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748621-Format-Pie)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721862-Format-Pointer-Label)

# Format Platform

The Format Platform dialog box is used to format the platform of a chart. It appears when you right-click a chart and select Format Platform from the shortcut menu.

There are the following tabs in this dialog box: [General](#General), [Border](#Border) and [Data](#Data).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Cancels the settings and closes this dialog box.

![Help button](https://devnet.logianalytics.com/hc/article_attachments/4404936816535/btn_help.gif)

Displays the help document about this feature.

![Close button](https://devnet.logianalytics.com/hc/article_attachments/4404942519575/btn_close.gif)

Ignores the setting and closes this dialog box.

## General

Specifies the color schema to fill the platform.

![Format Platform dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404942534807/fmtpltfrm_gnrl.gif)

**Color**

Specifies the color with which to fill the platform.

To change the color, select the color indicator to select a color from the color palette. You can select More Colors in the color palette to access the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009721402-Color-Picker-) dialog box in which you can select a color within a wider range, or select More Fill Effects to access the [Fill Effects](https://devnet.logianalytics.com/hc/en-us/articles/1500009748401-Fill-Effects) dialog box to specify a gradient or an image as the fill effect. You can also type a color string in the format #RRGGBB directly in the text box. If you want to make the background transparent, type Transparent in the text box.

**Transparency**

Specifies the transparency of the color.

## Border

Specifies the properties for borders of the chart platform.

![Format Platform dialog - Border tab](https://devnet.logianalytics.com/hc/article_attachments/4404942535063/fmtpltfrm_border.gif)

**Border Type**

Specifies the type for border of the platform.

* **None**  
   The object has no visible border lines.
* **Raised**  
   The object has 3D borders that appear as if they are raised off the page.
* **Recess**  
   The object has 3D borders that appear as if they are pressed into the page.
* **Shadow**  
   The object has two shadowed borders, beneath and to the right of the object.
* **Solid**  
   The object has single-line borders (default value).

**Color**

Specifies the color for border of the platform.

**Transparency**

Specifies the transparency for color of the border.

**Line Style**

Specifies the line style to apply to the border of the platform.

**Thickness**

Specifies the thickness of the border.

**End Caps**

Specifies the ending style of the border line.

* **Butt**  
   Ends unclosed subpaths and dash segments with no added decoration.
* **Round**  
   Ends unclosed subpaths and dash segments with a round decoration that has a radius equal to half of the width of the pen.
* **Square**  
   Ends unclosed subpaths and dash segments with a square projection that extends beyond the end of the segment to a distance equal to half of the line width.

**Line Joint**

Specifies the line joint style for the border line.

* **Miter**  
   Joins path segments by extending their outside edges until they meet.
* **Round**  
   Joins path segments by rounding off the corner at a radius of half the line width.
* **Bevel**  
   Joins path segments by connecting the outer corners of their wide outlines with a straight segment.
* **Joint Round**  
   Joins path segments by rounding off the corner at a specified radius.

**Radius**

Specifies the radius for the border joint of the platform border line. Available only when Line Joint is set to Joint Round.

**Dash**

Specifies the dash size of border line.

* **Auto Adjust Dash**  
   If selected, the dash size will be adjusted automatically.
* **Fixed Dash Size**  
   If selected, the dash size will be fixed size.

## Data

Available to heat maps only. In this tab, you can specify whether to calculate the size-by/color-by summary based on logarithm functions.

![Format Platform dialog - Data tab](https://devnet.logianalytics.com/hc/article_attachments/4404936843799/fmtpltfrm_dt.gif)

**Size by Logarithm**

Specifies whether to calculate the size-by summary based on logarithm function.

* **None**  
   Returns the real value of the field instead of any logarithmic value.
* **log x**  
   Gets the logarithm of the field with base 10.
* **ln x**  
   Gets the logarithm of the field with base e.

**Color by Logarithm**

Specifies whether to calculate the color-by summary based on logarithm function.

* **None**  
   Returns the real value of the field instead of any logarithmic value.
* **log x**  
   Gets the logarithm of the field with base 10.
* **ln x**  
   Gets the logarithm of the field with base e.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009748621-Format-Pie)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009721862-Format-Pointer-Label)
