---
title: "Properties of Image in Library Component"
id: 1500009569202
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009569202-Properties-of-Image-in-Library-Component
updated_at: 2021-07-24T05:54:18Z
---

# Properties of Image in Library Component

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590861-Properties-of-Geographic-Map-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569222-Properties-of-KPI-Component-in-Library-Component)

# Properties of Image in Library Component

The properties of an image object in a library component are as follows:

| Property Name | Description |
| --- | --- |
| Geometry | |
| Height | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| CSS | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#CSS) | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Horizontal Alignment | Specifies the horizontal alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Binding a Link to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label). Data type: String |
| Logic Column | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Transfer Style | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Vertical Alignment | Specifies the vertical alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Image Property | |
| Alternate Text | Specifies the text that will be displayed instead if the image cannot be displayed. Data type: String |
| Disabled | Specifies whether to disable the actions on the image. Data type: Boolean |
| Image Name | Specifies the file name of the image. The image can be one on your local file system or retrieved by using a URL. Data type: String |
| Maximum Scaling Ratio | Specifies the maximum ratio up to which the image can be scaled. Data type: Float |
| Name | Specifies the name of the image. Data type: String |
| Rotation | Specifies the angle at which to rotate the image, in degrees. The following is the meaning of different values:  * 0 - No rotation. * positive value - Rotates the image clockwise. * negative value - Rotates the image anticlockwise.   Data type: Float |
| Scaling Mode | Specifies the scaling mode of the image, which controls the image behavior when you try to adjust the image field size. Choose an option from the drop-down list.  * **actual size** - The image will remain its original size. If the image field size is smaller than the image size, part of the image will be cut off. * **fit image** - The image size will be automatically adjusted to fill up the image field, with its original perspective remained but under the limitation of Maximum Scaling Ratio. * **fit width** - The image will be automatically adjusted to fit the width of the image field but under the limitation of Maximum Scaling Ratio. * **fit height** - The image will be automatically adjusted to fit the height of the image field but under the limitation of Maximum Scaling Ratio. * **customize** - The image size will be automatically adjusted to fit the image field, regardless of the [Maximum Scaling Ratio](#Ratio)'s value.   Data type: Enumeration |
| Tab Index | Specifies the index that defines the tab order for the image. Data type: Integer |
| Title | Specifies the tip information about the image, which will be displayed when you hover the mouse pointer over the image at runtime. Data type: String |
| Value | Specifies the initial value of the image. Data type: String |
| Event | |
| [On Blur](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the object loses input focus. Data type: String |
| [On Select](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user selects the left mouse button on the object. Data type: String |
| [On Double Select](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user double-clicks the object. Data type: String |
| [On Focus](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the object receives focus. Data type: String |
| [On Key Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user presses a key. Data type: String |
| [On Key Press](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user presses an alphanumeric key. Data type: String |
| [On Key Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user releases a key. Data type: String |
| [On Mouse Down](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user selects the object with either mouse button. Data type: String |
| [On Mouse Move](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user moves the mouse over the object. Data type: String |
| [On Mouse Out](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user moves the mouse pointer outside the boundaries of the object. Data type: String |
| [On Mouse Over](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user moves the mouse pointer into the object. Data type: String |
| [On Mouse Up](https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report#Event) | Specifies the action when the user releases a mouse button while the mouse is over the object. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009590861-Properties-of-Geographic-Map-in-Library-Component)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569222-Properties-of-KPI-Component-in-Library-Component)
