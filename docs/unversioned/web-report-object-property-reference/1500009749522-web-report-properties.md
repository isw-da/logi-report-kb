---
title: "Web Report Properties"
id: 1500009749522
section: "Web Report Object Property Reference"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009749522-Web-Report-Properties
updated_at: 2021-07-24T00:47:41Z
---

# Web Report Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749502-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009769701-Appendices)

# Web Report Properties

This topic describes the properties of a Web Report object.

| Property Name | Description |
| --- | --- |
| Others | |
| Page Background | Specifies the background color of the report page. Choose a color from the drop-down list or select Custom to define a color in the [Color Picker](https://devnet.logianalytics.com/hc/en-us/articles/1500009746842-Color-Picker-Dialog-Box-Properties) dialog box. You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Suppress Object Space If Not Exported | Specifies whether to suppress the space used for holding the object in the exported report result when you have specified not to include it for exporting. Data type: Boolean |
| Excel | |
| [Columned](#Columned) | If true, the engine performance will be improved when exporting the report to CSV and Excel formats. Data type: Boolean |

## Columned

Right after you set the property to true from false each time, Logi Report will recalculate the values of the following Excel properties of the [line objects](https://devnet.logianalytics.com/hc/en-us/articles/1500009749282-Line-Properties#Excel) in the report and reset the values to the defaults: Top Attach Column, Top Attach Row, Bottom Attach Column and Bottom Attach Row. The default values are calculated based on the position of each line object in the report. There is an exception: if both the Export to Excel and Export to CSV properties of a line object are false, the values of these properties will not be recalculated and will be preserved as before.

The property controls two things when it is true:

* Use the columned method to export the report to Excel when the option Column Format is selected in the corresponding export dialog box.
* You can specify values for the Excel properties mentioned above of a line object instead of using the default, so that they can be well-aligned in the exported Excel file.

When the property is false:

* The specified values for the above Excel properties of the line objects in the report are not applied when exporting to CSV or Excel.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749502-Tabular-Cell-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009769701-Appendices)
