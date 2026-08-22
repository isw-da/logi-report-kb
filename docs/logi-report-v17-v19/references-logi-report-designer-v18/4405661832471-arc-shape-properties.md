---
title: "Arc Shape Properties"
id: 4405661832471
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661832471-Arc-Shape-Properties
updated_at: 2022-01-27T20:35:51Z
---

# Arc Shape Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties)  [Next Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661833495-Banded-Object-Properties)[![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661833495-Banded-Object-Properties)

# Arc Shape Properties

This topic describes the properties of an [Arc Shape object](https://devnet.logianalytics.com/hc/en-us/articles/4405661379095-Working-with-Drawing-Objects) that you can use in page reports only.

| Property Name | Description |
| --- | --- |
| General **(available when the object is in a query-based page report)** | |
| Class Type | Shows the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Geometry | |
| Bottom Attach Pos X | Specifies the horizontal coordinate for the bottom right point of the focus box in the involved banded panel. Data type: Float |
| Bottom Attach Pos Y | Specifies the vertical coordinate for the bottom right point of the focus box in the involved banded panel. Data type: Float |
| Top Attach Pos X | Specifies the horizontal coordinate for the top left point of the focus box in the involved banded panel. Data type: Float |
| Top Attach Pos Y | Specifies the vertical coordinate for the top left point of the focus box in the involved banded panel. Data type: Float |
| Color | |
| Background | Specifies the background color of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | |
| Class | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| Style | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the [Style Group](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) property for the page report tab, and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | |
| Export to PDF | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when you preview the report in the Page Report Result format in Designer, and when users run the report in the same format at runtime. Data type: Boolean |
| Export to XML | Specifies whether to include the object in the XML output. Data type: Boolean |
| Invisible | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Record Location | Specifies the calculation point for the properties of the object that are controlled by formulas. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   For more information, see [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Suppress When No Records | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Arc Property | |
| Arc Angle | Specifies the angle of the arc, in degrees. The value ranges from 0 to 360. When you set the angle closer to 360, the arc begins to take on an elliptical shape. Data type: Float |
| Border Color | Specifies the color for the border of the object. Choose a color from the drop-down list or select **Custom** to customize a color in the [Pick a Color dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664544407-Pick-a-Color-Dialog-Box#Color). You can also type a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Style | Specifies the line style for the border of the object. Choose an option from the drop-down list. Data type: Enumeration |
| Border Thickness | Specifies the width for the border of the object. Type a numeric value to change the thickness. Data type: Float |
| Start Angle | Specifies the start angle of the arc, in degrees. The value ranges from 0 to 360. At 0, the vertex of the arc starts at 12:15 clock position. When you set the angle closer to 360, the arc travels in a counterclockwise motion. Data type: Float |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML)**(available when the object is in a query-based page report)** | |
| External CSS Class Selector | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Title | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| Language | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661833495-Banded-Object-Properties)
