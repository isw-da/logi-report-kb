---
title: "Select Color Dialog Box Properties"
id: 28891527070605
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891527070605-Select-Color-Dialog-Box-Properties
updated_at: 2026-02-26T02:11:51Z
source_host: docs-report.zendesk.com
---
# 
Select Color Dialog Box Properties 

You can use the Select Color dialog box to specify a color. This topic describes the properties in the dialog box.

This topic contains the following sections:

- Swatches Tab Properties

- Color Picker Tab Properties

You see these elements on both tabs:

OK

Select to apply the color you specified here.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
Swatches Tab Properties

Select a color from the web safe color swatches.

Web Safe Colors

Select a web safe color.

Transparent

Select to make the object transparent.

Color indicator

Server displays the upper part in the color you selected from Web Safe Colors and labels the hexadecimal value of the color (or "Transparent" if you select the Transparent swatch). The lower part is always the original color. Selecting the lower part restores the color to the original.

## 
Color Picker Tab Properties

Customize the color in Page Report Studio.

Select Color

Select anywhere in the color matrix. Change saturation horizontally or change brightness vertically.

Color slider

Select a color on the bar to change the hue of the color matrix.

Color indicator

Server displays the upper part in the color you have newly defined. The lower part is always the original color. Selecting the lower part restores the color to the original.

R

Specify the amount of red in a color, from 0 to 255.

G

Specify the amount of green in a color, from 0 to 255.

B

Specify the amount of blue in a color, from 0 to 255.

Alpha

Server enables this property when you are setting the background color for a label or field. Specify the amount of transparency, from 0 to 255. When Alpha is 255, the color code contains 6 digits. When Alpha is not 255, Server displays the color code with 8 digits, and the first two digits indicate the alpha or transparency value.

The property value that is not 255 only works on the Text display type.

#

Specify the hexadecimal value of the color.
