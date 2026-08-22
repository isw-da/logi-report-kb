---
title: "Properties of Area in Page Report Shape Map"
id: 1500009591541
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591541-Properties-of-Area-in-Page-Report-Shape-Map
updated_at: 2021-07-24T05:54:10Z
---

# Properties of Area in Page Report Shape Map

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569662-Properties-of-Shape-Map-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591561-Properties-of-Label-in-Page-Report-Shape-Map)

# Properties of Area in Page Report Shape Map

You can set these properties globally for all the map areas, or respectively for each specific map area.

The properties of a shape map area object in a page report are listed as follows:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Data Inherit | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
| Use Global Setting | Specifies whether to apply the settings that you have set globally for all the map areas to this object.  * **true** - If selected, the object will take the global settings, and all the properties for the object will become read only. * **false**- If selected, the properties for the object can be edited if required.   Data type: Boolean |
| Area | |
| Alternate Text | Specifies the tip of the area, which is displayed when you hover the mouse pointer over the area in HTML result or in Page Report Studio. This property takes effect only when [Alternate Content Type](https://devnet.logianalytics.com/hc/en-us/articles/1500009569662-Properties-of-Shape-Map-in-Page-Report#Type) on the map object is set to customized and the area has data. Data type: String |
| Detail Report | Specifies the detail report that the object is linked to. Select  in the value cell to set the detail report. For details, refer to [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label#Detail). Data type: String |
| Fill Color | Specifies the color with which to fill the area which has records. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Binding a Link to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label). Data type: String |
| Name | Specifies the name of the area. Data type: String |
| Shape | |
| Coordinates | Indicates the coordinates of the area for laying out the map. The coordinates are displayed as: X1,Y1,X2,Y2,X3,Y3... (X/Y: The X/Y coordinate of one of the polygon's corner.) This property is read only. |
| Type | Indicates the shape of the area. This property is read only. |
| Boundary | |
| Boundary Color | Specifies the color of the area border. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Boundary Style | Specifies the line style of the area border. Choose an option from the drop-down list. Data type: Enumeration |
| Boundary Width | Specifies the width of the area border. Enter a numeric value to change the width. Data type: Float |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External TabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Enter an integer equal to or greater than 0 and less than 65535. Data type: Integer |
| External Title | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569662-Properties-of-Shape-Map-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009591561-Properties-of-Label-in-Page-Report-Shape-Map)
