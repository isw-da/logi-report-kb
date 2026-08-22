---
title: "Group Header Panel Properties"
id: 1500010033922
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010033922-Group-Header-Panel-Properties
updated_at: 2021-07-24T10:37:59Z
---

# Group Header Panel Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069621-Group-Footer-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069641-Group-Control-Image-Properties)

# Group Header Panel Properties

This topic lists the properties of a Group Header Panel object in a banded object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report and Web Report.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Data Inherit | Query Page Report | Indicates whether the dataset for this object is inherited from another object. This property is read only. |
| Dataset | Query Page Report | Indicates the dataset used by the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| Color | | |
| Background | Page Report, Web Report | Specifies the background color and fill effect of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the report tab level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | | |
| Cross Page | Page Report, Web Report | Specifies whether the panel can be split across a page break.  * If false, the panel will be shown in the Next Topic when it spans a large space vertically and cannot be wholly shown in a page. * If true, the panel will be split across a page break when it exceeds the page height.   This property is applied only when the report has page layout enabled.  Data type: Boolean |
| Export to CSV | Page Report, Web Report | Specifies whether to include the object in the CSV result of the report. Data type: Boolean |
| Export to Excel | Page Report, Web Report | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report | Specifies whether to include the object in the PDF result of the report.  Data type: Boolean |
| Export to PostScript | Page Report, Web Report | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio. Data type: Boolean |
| Export to RTF | Page Report, Web Report | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Export to Text | Page Report, Web Report | Specifies whether to include the object in the Text result of the report. Data type: Boolean |
| Export to XML | Page Report, Web Report | Specifies whether to include the object in the XML result of the report. Data type: Boolean |
| Fill Whole Page | Page Report, Web Report | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
| Invisible | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Label | Page Report, Web Report | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
| [Merge to Next Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties#Panel) | Page Report, Web Report | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
| [On New Page](#OnNewPage) | Page Report, Web Report | Specifies whether the panel starts on a new page. This property is only applied if the report has page layout enabled. The default is false which means the panel starts on a new page only if the Previous Topic is filled. Data type: Boolean |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#RecordLocation) | Page Report, Web Report | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| [Remove Blank Row](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties#Panel) | Page Report, Web Report | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
| [Repeat](#Repeat) | Page Report, Web Report | Specifies whether to make the group header appear in every page. Data type: Boolean |
| [Repeat in Detail Panel](https://devnet.logianalytics.com/hc/en-us/articles/1500010069661-Banded-Page-Header-Properties#Panel) | Page Report, Web Report | Specifies whether to make the objects in the panel repeated in the detail panel in the exported Excel file. Data type: Boolean |
| Show Bottom Line | Query Page Report | Specifies whether to include a horizontal line at the bottom of the panel. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
| Suppress | Page Report, Web Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress Blank Panel | Page Report, Web Report | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
| Suppress When No Records | Page Report, Web Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Underlay | Page Report, Web Report | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
| Border | | |
| Border Color | Page Report, Web Report | Specifies the color of the border of the object. Choose a color from the drop-down list or select Custom to customize a color. You can also use a formula or edit an expression that returns a color, or enter a hexadecimal RGB value (for example, 0xff0000) to specify a color. Data type: String |
| Border Joint | Page Report, Web Report | Specifies the joint style for the border lines of the object. Choose an option from the drop-down list.  * **miter** - Joins path segments by extending their outside edges until they meet. * **round** - Joins path segments by rounding off the corner at a radius of half the line width.   Data type: Enumeration |
| Border Thickness | Page Report, Web Report | Specifies the width of the border. Enter a numeric value to change the thickness. Data type: Float |
| Bottom Line | Page Report, Web Report | Specifies the line style of the bottom border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Left Line | Page Report, Web Report | Specifies the line style of the left border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Radius | Page Report, Web Report | Specifies the radius for the border line joint of the object. This property takes effect only when [Border Joint](#BorderJoint) is set to round. Data type: Integer |
| Right Line | Page Report, Web Report | Specifies the line style of the right border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Top Line | Page Report, Web Report | Specifies the line style of the top border of the object. Choose a style from the drop-down list. Data type: Enumeration |
| Accessibility | | |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |

## On New Page

If you want each group to start on a new page, you have two approaches. One is to configure with group header panel as follows, the other is to set the Fill Whole Page property for the group footer panel.

There is a problem when you only set On New Page to be true for the group header panel. You will find that the first page will have no details. Logi JReport Engine starts the detail panel from the second page. To solve this issue, you can use a formula to control this property. The formula will judge the property as being false for the first group, and being true for subsequent groups for displaying on a new page. However, if you feel this is too complicated, go to the group footer panel for the second approach.

1. Create three formulas as follows:

   **global:**  
   `global integer i=0;`

   **groupHD:**  
   `i=i+1;0`

   **FormulaControl:**  
   `@groupHD;  
    if (i>1)  
   return true  
   else  
   return false`
2. Insert the formula global into the banded page header panel and assign it an initial value 0.
3. Insert the formula groupHD into the group header panel so that for each group i will be calculated as i+1.
4. Select the group header panel and use the formula FormulaControl to control its On New Page property. This formula will only return true for the property if i>1.

## Repeat

The default value for Repeat is false. For one detail panel which spans a large space vertically to be shown in several pages, Logi JReport support the Repeat property if you want to see the group header information in each page. When the Repeat property is set true and group headers are visible, the group headers will duplicate on every page.

**Notes:**

* When a page split occurs in the bottom blank part of the detail panel (or margins in the detail panel) and the Cross Page property in the detail panel is set true, the output will be: repeated group header + a slice of blank detail panel + group footer. It appears as though the repeated group headers are followed only by group footers without any detail panel. In order to solve this problem, you can resize the detail panel.
* If the Repeat property is set true in both outer group header and inner group header, Logi JReport will treat the two group headers as a completely repeated object.
* If the outer and inner group headers are set to be one completely repeated object, then when the page can only hold the group headers or has no enough space for the group headers, both outer and inner group headers will not be duplicated.
* The Repeat property does not work for subreport.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069621-Group-Footer-Panel-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010069641-Group-Control-Image-Properties)
