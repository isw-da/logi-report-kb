---
title: "Format Legend Dialog Box Properties"
id: 45203956767117
section: "Dialog Boxes in Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203956767117-Format-Legend-Dialog-Box-Properties
updated_at: 2026-04-30T14:09:45Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Format Legend Dialog Box Properties

This topic describes how you can use the Format Legend dialog box to format the legend of a chart. Server displays the dialog box when you right-click a chart and select Format Legend (unavailable to org charts and gauge bubble charts) from the shortcut menu.

This topic contains the following sections:

- General Tab Properties

- Placement Tab Properties

- Border Tab Properties

- Font Tab Properties

- Label Tab Properties

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

Specify the general properties of the chart legend.

Name

Specify the display name of the chart legend.

Show NLS Value

Select to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it, and when you have not modified the display name of the object.

Width

Specify the width of the chart legend.

Height

Specify the height of the chart legend.

Fill Type

Specify the type for filling the chart legend. It can be one of the following: None, Color, Texture, Gradient, and Image. If you select Gradient or Image, you can specify the gradient or image by the Fill Type property in the Background category of the chart legend in the Inspector. 

Color

Specify the background color of the chart legend. It takes effect only when Fill Type in this tab is Color. 

To change the color, select the color indicator. Server displays the color palette. Select a color, or select More Colors to access the Color Picker dialog box in which you can specify a color within a wider range. 

Transparency

Specify the transparency of the legend background color.

Show Value 

Select if you want to show the value of each legend.

Show Percent 

Select if you want to show the percentage of each legend.

Show Tips

Select if you want to show the corresponding data information when you hover over a target in the chart legend.

Show Scrollbar

Select if you want to show a scroll bar on the legend to fully view the legend contents when the contents do not fit into the legend. 

Truncate

Select if you want to truncate the legend entry label text when the text overflow the labels.

## 
Placement Tab Properties

Specify the position-related properties of the chart legend.

Placement

Specify the position of the legend in the platform.

Secondary Placement

Specify the position of the legend on the basis of the Placement property.

Top Margin

Specify the distance between the legend labels and the top border of the legend.

Bottom Margin

Specify the distance between the legend labels and the bottom border of the legend.

Left Margin

Specify the distance between the legend labels and the left border of the legend.

Right Margin

Specify the distance between the legend labels and the right border of the legend.

Label Vertical Spacing

Specify the vertical distance between two adjacent legend labels.

Label Horizontal Spacing

Specify the horizontal distance between two adjacent legend labels.

Reverse Labels

Select if you want to arrange the legend labels in a reverse order.

## 
Border Tab Properties

Specify the border properties of the chart legend.

Line Style

Select the line style of the border.

Border Type

Select the type of the border.

Color

Specify the color of the border.

Transparency

Specify the transparency for the color of the border.

Thickness

Specify the thickness of the border, in inches.

## 
Font Tab Properties

Specify the font properties of the chart legend. 

Font

Specify the font face for the legend labels.

Size

Specify the font size for the legend labels.

Fill Type

Specify the fill type for the legend labels. It can be one of the following: None, Color, Texture, and Gradient. If you select Gradient, you can specify the gradient or image by the Fill Type property in the Label category of the chart legend in the Inspector.

Color

Specify the color for the legend labels. It takes effect only when Fill Type in this tab is Color.

Transparency

Specify the transparency for the legend labels, in percent.

Font Style

Specify the font style of the text. It can be one of the following: Plain, Bold, Italic, and Bold Italic.

Font Rotation

Specify the rotation angle of each legend label around its center, in degrees.

Word Wrap

Select if you want to enable word wrapping for the label text.

## 
Label Tab Properties

Specify the text of the legend entry labels. This tab is available only when the legend entry labels show the values of the field displayed on the category or series axis of the chart.

Auto

Select if you want the legend entry labels to display the values of the category/series field. You can clear Auto if you want to customize the label text.

- 
Label Text
    Specify the text of the legend entry labels. Type the label text manually, or select  and then select a field from the drop-down list to use its values as the label text.

Auto Scale in Number

When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart.
