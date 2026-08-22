---
title: "Format Gauge Label Dialog Box Properties"
id: 45203876365197
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203876365197-Format-Gauge-Label-Dialog-Box-Properties
updated_at: 2026-04-30T14:08:23Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Gauge Label Dialog Box Properties

You can use the Format Gauge Label dialog box to format the group labels in a gauge chart (excluding bubble gauge chart). This topic describes the properties in the dialog box.

This topic contains the following sections:

- General Tab Properties

- Font Tab Properties

- Format Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help

Select to view information about the dialog box.

## 
General Tab Properties

Specify the general properties of the labels.

Option

Specify the size and position of the labels.

- 
Width
    Specify the width of the labels, in inches.

- 
Height
    Specify the height of the labels, in inches.

- 
X
    Specify the horizontal coordinate of the upper-left corner of the labels, relative to their parent container. It takes effect when you have selected Show Gauge Group Name and set Position to customized on the Frame tab of the gauge's corresponding Format XXX Gauge dialog box. 

- 
Y
    Specify the vertical coordinate of the upper-left corner of the labels, relative to their parent container. It takes effect when you have selected Show Gauge Group Name and set Position to customized on the Frame tab of the gauge's corresponding Format XXX Gauge dialog box. 

- 
Alignment
    Select the alignment of the label text.

- 
Word Wrap
    Select to enable the word wrap function for the label text.

Fill

Specify the color and transparency of the labels.

- 
Color
    Specify the color to fill the labels. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

- 
Transparency
    Specify the transparency of the color to fill the labels.

Border

Specify the properties for the borders of the labels.

- 
Line Style

Select the line style of the border.

- 
Border Type

    Select the type of the border.

- 
Color

    Specify the color of the border. To change the color, select the color indicator to access the Select Color dialog box, and then specify a new color. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff.

- 
Transparency

  Specify the transparency for the color of the border.

- 
Thickness

    Specify the thickness of the border, in inches.

Orientation

- 
Angle
  Specify the rotation angle of the labels.

## 
Font Tab Properties

Specify the font properties of the label text.

Font

  Select the font face of the label text.

Size

  Specify the font size of the label text.

Fill Type

Select the fill type of the label text: none, color, texture, or gradient.

Color

Specify the color of the label text. It takes effect when Fill Type on this tab is color.

Transparency

  Specify the color transparency of the label text.

Font Style

Select the font style of the label text: plain, bold, italic, or bold italic.

## 
Format Tab Properties

Specify the data format of the labels.

Category

Select a category type to customize its format.

Format

Select a format, and then select Add to add it as the format of the specified category. You can add only one format for each category.

Properties

Server displays the properties of the format you select. If the formats listed in the Format box cannot meet your requirement, define the format in the Properties text box, and then select Add to add it as the format of the specified category.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart platform. When you set the property to true, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Report will ignore the Auto Scale in Number setting.

Sample

Server displays a preview sample of your settings.

Stack

Server displays all the formats you select for different categories.

Add

Select to add a format to the Stack box.

Remove

Select to remove a format from the Stack box.

Apply

Select to apply the specified format in the Stack box to the labels.
