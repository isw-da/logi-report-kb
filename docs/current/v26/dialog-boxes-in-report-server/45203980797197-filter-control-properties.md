---
title: "Filter Control Properties"
id: 45203980797197
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203980797197-Filter-Control-Properties
updated_at: 2026-04-30T14:09:40Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Filter Control Properties

This topic describes how you can use the Filter Control Properties dialog box to edit the properties of a filter control. Server displays the dialog box when you right-click a filter control and select Properties from the shortcut menu.

This topic contains the following sections:

- General Tab Properties

- Font Tab Properties

- Border Tab Properties

- Title Tab Properties

You see these elements on all the tabs:

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.

## 
General Tab Properties

Specify the general properties of the filter control.

Name

Specify the name of the filter control.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Format

Specify the value format of the field that you added in the filter control. 

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The value auto means that the setting follows that of the parent data container. When you set the property to true, the specified format will apply to the integer part of the values after being scaled. If the specified format conflicts with the Number data type, Report will ignore the Auto Scale in Number setting.

Filter On 

Server displays the fields that the filter control is based on. You can select the ellipsis button  to open the Edit Filter Control dialog box.

Width

Specify the width of the filter control.

Height

Specify the height of the filter control.

Background

Specify the background color of the filter control.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Foreground

Specify the foreground color of the filter control.

Show Title

Clear if you want to hide the title of the filter control. 

Artifact

Specifies whether to add an artifact tag when exporting to PDF.

## 
Font Tab Properties

Specify the font properties of the text in the filter control.

Font

Specify the font face of the text. 

Size

Specify the font size of the text. 

Bold

Select if you want to make the text bold.

Underline

Select if you want to underline the text.

Italic

Select if you want to make the text italic.

## 
Border Tab Properties

Specify the border properties of the filter control.

Color

Specify the border color.

Width

Specify the border width in inches.

Top Line

Select the style of the top border line.

Bottom Line

Select the style of the bottom border line.

Left Line

Select the style of the left border line.

Right Line

Select the style of the right border line.

## 
Title Tab Properties

Specify the title properties of the filter control. This tab is available when Show Title is selected in the General tab of the dialog box. 

Text

Server enables this property when you clear Auto Map Field Name. Type the text you want to display as the title.

When you add only one DBField to the text list filter control  and insert the On-screen Filter special field in a  data container that uses the same data resource as the DBField, Report also applies the text in the filter expression of the special field.

- 
Auto Map Field Name
  Select if you want to automatically map the title text to the dynamic display name of the field bound with the filter control.

Background

Specify the background color of the title.

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range. You can also type a hexadecimal RGB value to specify a color, for example, #9933ff. If you want to make the background transparent, type Transparent in the text box.

Foreground

Specify the foreground color of the title.

Font

Specify the font face of the text. 

Size

Specify the font size of the text. 

Horizontal Alignment

Specify the horizontal alignment mode of the text.

Title Height

Specify the height of the title, to ensure larger font sizes display without being cut off. Type a numeric value to change the height.

Bold

Select if you want to make the text bold.

Underline

Select if you want to underline the text.

Italic

Select if you want to make the text italic.
