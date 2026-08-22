---
title: "Format Scatter Dialog"
id: 1500009608582
section: "References - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009608582-Format-Scatter-Dialog
updated_at: 2021-07-24T16:04:33Z
---

# Format Scatter Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608562-Format-Rectangle-Title-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631601-Format-Series-Z-Axis-Dialog)

# Format Scatter Dialog

The Format Scatter dialog helps you to [format the scatter in a scatter chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009605962-Formatting-the-Scatter-in-a-Scatter-Chart). It appears when you right-click a scatter marker in a scatter chart and select Format Scatter from the shortcut menu, or double-click a scatter marker in a scatter chart.

The dialog contains the following tabs: [General](#General), [Fill](#Fill), [Data Label](#Data) and [Hint](#Hint).

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Apply**

Applies all changes and leaves the dialog open.

**Help**

Displays the help document about this feature.

## General

Specifies the general format of the scatter chart.

![Format Scatter - General](https://devnet.logianalytics.com/hc/article_attachments/4404904295191/fmtsctr_gnrl.gif)

**Layout**

Specifies the layout for scatter markers in the chart.

* **No line**  
   If selected, no lines will be used to joint scatter markers in the chart.
* **Straight line**  
   If selected, straight lines will be used to joint scatter markers in the chart.
* **Curved line**  
   If selected, curved lines will be used to joint scatter markers in the chart.

**Line**

Specifies properties for lines of the scatter chart.

* **Thickness**  
   Specifies the thickness for lines in the scatter chart, in pixels.

**Node**

Specifies properties for line nodes in the scatter chart.

* **Style**  
   Specifies the node style for line nodes.
* **Width**  
   Specifies the width for line nodes, in pixels.
* **Height**  
   Specifies the height for line nodes, in pixels.

## Fill

Specifies the color pattern to fill the scatter markers.

![Format Scatter - Fill](https://devnet.logianalytics.com/hc/article_attachments/4404904295447/fmtsctr_fill.gif)

**Color**

Specifies the color schema for the selected scatter markers in the same data series. To edit the color, select the color indicator and select a color from the [color palette](https://devnet.logianalytics.com/hc/en-us/articles/1500009613582-Menu-Tabs#Palette) or input the hexadecimal value (for example, 0xff0000) of a color in the text box.

**Transparency**

Specifies the transparency of the color schema.

**Self Settings**

Specifies whether to edit the color pattern for the scatter markers themselves. When the option is unselected, the color settings defined here will be synchronized to the [Pattern List property](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#Pattern) on the chart object in the Report Inspector, which can also be applied by data markers of other subtypes if the chart is a combo chart.

**Color List**

Opens the [Color List](https://devnet.logianalytics.com/hc/en-us/articles/1500009630161-Color-List-Dialog) dialog to modify the color pattern for scatter markers in the same data series respectively.

**Sample**

Displays a preview sample of your selection.

## Data Label

Specifies properties for data labels displayed on the chart. Not supported on scatter chart.

![Format Scatter - Data Panel](https://devnet.logianalytics.com/hc/article_attachments/4404904295959/fmtsctr_data.gif)

## Hint

Specifies properties for the hint of the scatter markers.

![Format Scatter - Hint](https://devnet.logianalytics.com/hc/article_attachments/4404904296599/fmtsctr_hint.gif)

**Show Category and Series**

Specifies whether to include the category and series values in the hint.

**Auto Scale in Number**

Specifies whether to automatically scale the values displayed in the hint that are of the Number data type when the values fall into the two ranges:

* When 1000 <= value < 10^15, the following quantity unit symbols of the International System of Units are used to scale the values: K (10^3), M (10^6), G (10^9), and T (10^12).
* When 0 < value < 0.001 or value >= 10^15, scientific notation is used to scale the values.

The option "auto" means that the property setting follows [that of the chart](https://devnet.logianalytics.com/hc/en-us/articles/1500009612122-Chart-Properties#AutoScale).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009608562-Format-Rectangle-Title-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009631601-Format-Series-Z-Axis-Dialog)
