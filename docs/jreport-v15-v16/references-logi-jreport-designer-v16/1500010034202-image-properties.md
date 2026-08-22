---
title: "Image Properties"
id: 1500010034202
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010034202-Image-Properties
updated_at: 2021-07-24T10:37:55Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069961-GMarker-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034222-KPI-Properties)

# Image Properties

This topic lists the properties of an Image object. The availabilities of the properties vary for the [supported report types](https://devnet.logianalytics.com/hc/en-us/articles/1500010069521-Report-Object-Properties#ReportType): Page Report, Web Report and Library Component.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Indicates the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Enter a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Enter a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [Position](#Position) property is set to static. Enter a numeric value to change the position. Data type: Float |
| CSS | | |
| [Class](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
| [ID](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
| [Style](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#CSS) | Page Report, Web Report, Library Component | The property can be used in two ways.  * Specifies a style to be applied to the object. Choose a style from the drop-down list which is available when a Style Group has been selected at the page report tab or web report or library component level and when there are styles in the Style Group that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object. Enter a valid class name from the CSS file.   Data type: String |
| Others | | |
| Detail Report | Query Page Report | Specifies the detail report that the object is linked to. Select  in the value cell to set the detail report. For details, refer to [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports#Detail). Data type: String |
| [Detail Target Frame](https://devnet.logianalytics.com/hc/en-us/articles/1500010069841-DBField-Properties#DetailTargetFrame) | Page Report | Specifies the target window or frame in which to display the detailed information. Choose an option from the drop-down list. This property is supported on images in the group header/footer panel of a banded object and enabled when [Go to Detail](#GoToDetail) is set to true. Data type: String |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel result of the report. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML result of the report. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF result of the report. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript result of the report. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when previewing the report in Page/Web Report Result and running the report in Page/Web Report Studio, or when the library component is used in JDashboard. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF result of the report. Data type: Boolean |
| Go to Detail | Query Page Report | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. For details about its usage, refer to [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500010028622-Obtaining-Detailed-Information-from-a-Banded-Object). Data type: Boolean |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to show the object in the design area and in the results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Link | Page Report, Web Report, Library Component | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500010034822-Adding-Links-in-Reports). Data type: String |
| Logic Column | Page Report, Web Report, Library Component | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. This property is supported when the object is in a table. Choose an option from the drop-down list. Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500010070821-Editing-Reports#Position) | Page Report, Web Report, Library Component | Specifies the position of the object. Choose an option from the drop-down list. Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500010070041-Label-Properties#RecordLocation) | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object which are controlled by formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Query Page Report | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Query Page Report | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
| Transfer Style | Page Report, Web Report, Library Component | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Excel | | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Column Number | Page Report, Web Report | Specifies the number of columns which will be the object's width in the exported Excel file. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#Index) | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Row Number | Page Report, Web Report | Specifies the number of rows which will be the object's height in the exported Excel file. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500010070201-Page-Report-Tab-Properties#Column) property at the page report tab or web report level must be set to true for this property to take effect. Data type: Integer |
| Image Property | | |
| Alternate Text | Page Report, Web Report, Library Component | Specifies the text that will be displayed instead if the image cannot be displayed. Data type: String |
| Disabled | Page Report, Web Report, Library Component | Specifies whether to disable the actions on the image. Data type: Boolean |
| Image Name | Page Report, Web Report, Library Component | Specifies the file name of the image. The image can be one on your local file system or retrieved by using a URL. Data type: String |
| Maximum Scaling Ratio | Page Report, Web Report, Library Component | Specifies the maximum ratio up to which the image can be scaled. Data type: Float |
| Name | Page Report, Web Report, Library Component | Specifies the name of the image. Data type: String |
| Rotation | Page Report, Web Report, Library Component | Specifies the angle at which to rotate the image, in degrees. The following is the meaning of different values:  * 0 - No rotation. * positive value - Rotates the image clockwise. * negative value - Rotates the image anticlockwise.   Data type: Float |
| Scaling Mode | Page Report, Web Report, Library Component | Specifies the scaling mode of the image, which controls the image behavior when you try to adjust the image field size. Choose an option from the drop-down list.  * **actual size** - The image will remain its original size. If the image field size is smaller than the image size, part of the image will be cut off. * **fit image** - The image size will be automatically adjusted to fill up the image field, with its original perspective remained but under the limitation of Maximum Scaling Ratio. * **fit width** - The image will be automatically adjusted to fit the width of the image field but under the limitation of Maximum Scaling Ratio. * **fit height** - The image will be automatically adjusted to fit the height of the image field but under the limitation of Maximum Scaling Ratio. * **customize** - The image size will be automatically adjusted to fit the image field, regardless of the [Maximum Scaling Ratio](#Ratio)'s value.   Data type: Enumeration |
| Tab Index | Page Report, Web Report, Library Component | Specifies the index that defines the tab order for the image. Data type: Integer |
| Title | Page Report, Web Report, Library Component | Specifies the tip information about the image, which will be displayed when you hover the mouse pointer over the image in HTML result or at runtime. Data type: String |
| Value | Page Report, Web Report, Library Component | Specifies the initial value of the image. Data type: String |
| Event | | |
| [On Blur](#Event) | Page Report, Web Report, Library Component | Specifies the action when the object loses input focus. Data type: String |
| [On select](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user selects the left mouse button on the object. Data type: String |
| [On Double click](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user double-clicks the object. Data type: String |
| [On Focus](#Event) | Page Report, Web Report, Library Component | Specifies the action when the object receives focus. Data type: String |
| [On Key Down](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user presses a key. Data type: String |
| [On Key Press](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user presses an alphanumeric key. Data type: String |
| [On Key Up](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user releases a key. Data type: String |
| [On Mouse Down](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user selects the object with either mouse button. Data type: String |
| [On Mouse Move](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user moves the mouse over the object. Data type: String |
| [On Mouse Out](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user moves the mouse pointer outside the boundaries of the object. Data type: String |
| [On Mouse Over](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user moves the mouse pointer into the object. Data type: String |
| [On Mouse Up](#Event) | Page Report, Web Report, Library Component | Specifies the action when the user releases a mouse button while the mouse is over the object. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500010069541-Banded-Object-Properties#TOC) (only supported on images in a banded object) | | |
| Anchor Display Value | Page Report | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Page Report | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | | |
| External AccessKey | Query Page Report | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Query Page Report | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | Query Page Report | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | Query Page Report | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| HrefLang | Query Page Report | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | Query Page Report | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | Query Page Report | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

## Event Property Values

The provided values are based on the image client API in Version 7. The following table lists their mapping values in current version. For information about the descriptions and parameters of the mapping values, see [Appendix 3: Parameters of User Defined Web Actions](https://devnet.logianalytics.com/hc/en-us/articles/1500010028462-Appendix-3-Parameters-of-User-Defined-Web-Actions).

| Value | Mapping Name |
| --- | --- |
| exit(popwin) | user\_exit() |
| firstPage() | user\_firstPage() |
| lastPage() | user\_lastPage() |
| nextPage() | user\_nextPage() |
| oneStepfilter(columns, operators, values, logics) | user\_oneStepfilter(columnMappingNames, operators, values, logics, instanceName) |
| oneStepSearch(value, isContent, colName, isUp, matchcase, isWordOnly) | user\_oneStepSearch(value, isContent, colName, isUp, matchcase, isWordOnly) |
| oneStepSort(columns, sorts) | user\_oneStepSort(columnMappingNames, orders, instanceName) |
| prevPage() | user\_prevPage() |
| redo() | user\_redo() |
| refresh() | user\_refresh() |
| reset() | user\_reset(instanceName) |
| saveRpt() | user\_saveRpt() |
| searchNext(isFindTxt) | This API is not supported now. |
| saveRst() | - |
| showExportExcelDlg() | - |
| showExportHTMLDlg() | - |
| showExportPDFDlg() | - |
| showExportPSDlg() | user\_showSaveResultDialog() |
| showExportRtfDlg() | - |
| showExportTextDlg() | - |
| showExportXmlDlg() | - |
| showFilterPanel() | user\_showFilterDialog() |
| showHelp() | user\_showHelp(null) |
| showNavibar() | This API is not supported now. |
| showPageSetupDlg() | user\_showPageSetupDialog() |
| showPrintDialog() | user\_showPrintDialog() |
| showSearchDlg() | user\_showSearchDialog() |
| showSortPanel() | user\_showSortDialog() |
| showTOC() | user\_showTOC() |
| showUserPanel() | user\_showUserPanel() |
| undo() | user\_undo() |
| zoom(value) | user\_zoomTo(value) |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010069961-GMarker-Properties) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034222-KPI-Properties)
