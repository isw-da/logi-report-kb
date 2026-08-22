---
title: "Format Donut Dialog Box Properties"
id: 28891492806285
section: "Dialog Boxes in Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891492806285-Format-Donut-Dialog-Box-Properties
updated_at: 2026-02-26T02:12:50Z
source_host: docs-report.zendesk.com
---
# 
Format Donut Dialog Box Properties

This topic describes how you can use the Format Donut dialog box to format the donuts of a donut chart. Server displays the dialog box when you right-click a donut chart and select Format Graph from the shortcut menu.

Donut

Specify the properties of the donuts. 

- 
Show Donut Name
Select true if you want to show the names of the donuts.

- 
Donut Hole
Specify the percentage the hole's thickness will take from the total radius of the pie circle.

Static Data Label

Specify the properties of the static data labels on the donuts.

- 
Show Static Data Label
  Select true if you want to show the static data labels on the donuts. Only when it is true can the following static data label properties work.

- 
Style
  Select the display type for data values in the static data labels.
    
- 
Value
Select to display the value for each donut section.

- 
Category Name
Select to display the category name for each donut section.

- 
Percent
 Select to display the percentage of each donut section to the total.

- 
Value and Percent
 Select to display the value and the percentage for each donut section.

- 
Category Name, Value 
Select to display the category name and value for each donut section.

- 
Category Name, Percent 
        Select to display the category name and percentage for each donut section.

- 
Category Name, Value, Percent 
Select to display the category name, value, and percentage for each donut section.

- 
Position
    Select the position of the static data labels on the donuts.
    
- 
Autofit
 Select to display the static data labels automatically.

- 
Sticker
 Select to display the static data labels beside the donut sections.

- 
Slim Leg
 Select to display the static data labels beside the donut sections with thin lines.
		- 
Line Color
Specify the color of the thin lines that point to the static data labels.

- 
Best Fit
 Select to display the static data labels at the best fit position automatically.

- 
On Slices
 Select to display the static data labels on the donut sections (slices).

- 
Auto Scale in Number
When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart.

- Show Truncated Label
Select to truncate labels that would go beyond the boundaries on a donut chart paper instead of them being hidden altogether - the default behavior. Report displays an ellipsis (…) from the right side of the label, along with part of the name instead of the entire name, when you select this property. The truncated labels are also affected if you select the Position property of Best Fit (as seen above); where the label is cut off from the left or the right depending on the position of the label.

KPI Value

Specify the properties for the KPI values of the donuts.

- 
Show KPI Value
    Select to show KPI value for each donut and enable the two properties.
    
- 
KPI Value
          Specify the KPI value to display on each donut. By default, Server uses the total value of each donut as the KPI value. If you want to customize the KPI value, clear Auto, then type a value in the text box, or select  and select a formula or summary from the value list to use its value as the KPI value.

- 
Position
        Select the position of the KPI value at the center, top, bottom of each donut or customized which enables setting the X and Y properties to change the position.

Graph Border 

Specify the properties for the border of the donuts.

- 
Show Border

Select to show the border and enable the border properties.
  

- 
Line Style

Select the line style of the border.

- 
Color

Specify the color of the border.

- 
Thickness

Specify the thickness of the border.

- 
Transparency

Specify the transparency for the border color.

- 
Radius

Specify the radius size of the rounded corners of the border.

Hint

Specify the data marker hint properties.

- Show Category and Series

Select to include the category and series values in the data marker hint.

- 
Auto Scale in Number
When you select Auto fit, Outside Top Inside, Top or Inside Bottom as static data labels' position, you can customize the spacing between the data label and the bar.

The default value auto means that the setting follows that of the chart.

- 
Customize Chart Value Names
Select if you want to customize the names of the fields used as the values in the chart. Server uses the customized names in the data marker hint. Then select the ellipsis button  to open the Customize Chart Value Names dialog box.
	

OK

Select to apply any changes you made here and close the dialog box.

Cancel

Select to close the dialog box without saving any changes.

Help button

Select to view information about the dialog box.

Close button

Select to close the dialog box without saving any changes.
