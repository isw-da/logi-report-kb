---
title: "Image Properties"
id: 4405661863319
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661863319-Image-Properties
updated_at: 2022-01-27T20:35:51Z
---

# Image Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661862039-Group-Control-Image-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661864599-KPI-Properties)

# Image Properties

This topic describes the properties of an [Image object](https://devnet.logianalytics.com/hc/en-us/articles/4405661381143-Working-with-Images).

Designer provides some properties only when you use the object in certain [report types](https://devnet.logianalytics.com/hc/en-us/articles/4405661831319-Report-Object-Properties#ReportType). You can get details from the Available For column in the property table.

| Property Name | Available For | Description |
| --- | --- | --- |
| General | | |
| Class Type | Query Page Report | Shows the class type of the object. This property is read only. |
| Instance Name | Query Page Report | Shows the instance name of the object. This property is read only. |
| Geometry | | |
| Height | Page Report, Web Report, Library Component | Specifies the height of the object. Type a numeric value to change the height. Data type: Float |
| Width | Page Report, Web Report, Library Component | Specifies the width of the object. Type a numeric value to change the width. Data type: Float |
| X | Page Report, Web Report, Library Component | Specifies the horizontal coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| Y | Page Report, Web Report, Library Component | Specifies the vertical coordinate of the object's top left corner, relative to its parent container, which Logi Report Engine applies when the object is not in static [position](#Position) in the container. Type a numeric value to change the coordinate. Data type: Float |
| CSS | | |
| Class | Page Report, Web Report, Library Component | Specifies the name of the Class Selector to apply to the object, which you define in the CSS file of [the style the report applies](https://devnet.logianalytics.com/hc/en-us/articles/4405661943319-Applying-Styles-to-Reports). For example, if you define the CSS file as follows:  `@charset "GBK";  TextField {Background: #ff0000}  /*Style=LabelX*/  TextField[Style="LabelX"]{Background: #0000FF}  /*ID=W*/  TextField#W{Background: #FFFF00}   /*class=C*/  TextField.C{Background: #00FFFF}`  To apply the Class Selector in the file to the object, type **C** in the value cell.  Data type: String |
| ID | Page Report, Web Report, Library Component | Specifies the name of the ID Selector to apply to the object, which you define in the CSS file of the style the report applies. For example, to apply the ID Selector in the preceding sample CSS file to the object, type **W** in the value cell. Data type: String |
| Style | Page Report, Web Report, Library Component | Specifies the style you want to apply to the object. You can specify the style in two ways:  * Type the style which should be an Attribute Selector whose attribute is "style" in the CSS file of the style the report applies.   For example, to apply the style in the preceding sample CSS file to the object, type **LabelX** in the value cell. * Choose a style from the drop-down list if you have specified the Style Group property for the [report tab](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#StyleGroup) or [web report](https://devnet.logianalytics.com/hc/en-us/articles/4405661909143-Web-Report-Properties#StyleGroup), and there are styles in the style group that are applicable to the object.   Data type: String |
| Others | | |
| Detail Report | Query Page Report | Specifies the detail report that you want to link the object to. Select the ellipsis Ellipsis button in the value cell to set the detail report. For more information, see [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports#Detail). Data type: String |
| Detail Target Frame | Query Page Report | Designer displays this property when the object is in the group header/footer panel of a banded object, and enables it after you set [Go to Detail](#GoToDetail) of the object to "true". You can use it to specify the target window or frame to display the detail information. Choose an option from the drop-down list.  * **<Server Setting>** Select to load the detail information according to setting of the Pop up New Window for Links option in the Profile > Configure Profile > Page Report Studio > Properties > Default tab on Server. * **New Window** Select to load the detail information into a new window. The window is not named. * **Whole Window** Select to load the detail information into the full browser window. * **Same Frame** Select to load the detail information into the same frame as the object. * **Parent Frame** Select to load the detail information into the parent frame of the frame in which the object is. * **Other Frame** Select to load the detail information into some other specified frame. Type the name of the frame you have defined in the value cell. If the frame name does not exist, Server loads the detail information into a new window.   Data type: String |
| Export to Excel | Page Report, Web Report, Library Component | Specifies whether to include the object in the Excel output. Data type: Boolean |
| Export to HTML | Page Report, Web Report, Library Component | Specifies whether to include the object in the HTML output. Data type: Boolean |
| Export to PDF | Page Report, Web Report, Library Component | Specifies whether to include the object in the PDF output. Data type: Boolean |
| Export to PostScript | Page Report, Web Report, Library Component | Specifies whether to include the object in the PostScript output. Data type: Boolean |
| Export to Report Result | Page Report, Web Report, Library Component | Specifies whether to include the object when you preview the report in the Page Report Result format for a page report or Web Report Result for a web report in Designer, and when users run the report in the same format or use the library component at runtime. Data type: Boolean |
| Export to RTF | Page Report, Web Report, Library Component | Specifies whether to include the object in the RTF output. Data type: Boolean |
| Go to Detail | Query Page Report | Designer displays this property when the object is in the group header/footer panel of a banded object. You can use it to specify whether to show the detail information about the group when users select the object in Page Report Studio. For more information, see [Obtaining the Group Details in a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/4405661346583-Obtaining-the-Group-Details-in-a-Banded-Object). Data type: Boolean |
| Horizontal Alignment | Page Report, Web Report, Library Component | Specifies the horizontal alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Invisible | Page Report, Web Report, Library Component | Specifies whether to hide the object in the design area and in the report. Logi Report Engine performs all calculations that involve the object regardless of whether the object is visible or not. Data type: Boolean |
| Link | Page Report, Web Report, Library Component | Specifies the target that you want to link the object to, which can be another report, a website, an email address, or a Blob data type field. Select the ellipsis Ellipsis button in the value cell to set the link target. For more information, see [Adding Links in Reports](https://devnet.logianalytics.com/hc/en-us/articles/4405661933591-Adding-Links-in-Reports). Data type: String |
| Logic Column | Page Report, Web Report, Library Component | Designer displays this property when the object is in a table. You can use it to specify whether to show the object in the next visible table cell in the same row when the column that holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration  Note icon   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When you set this property for several objects in the same row to "next visible column", and the columns holding these objects are all hidden, only the object in the rightmost column shows in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#Position) | Page Report, Web Report, Library Component | Designer enables this property when the object is in a flow layout container, such as the report body or a tabular cell, text box, or KPI. You can use it to specify the position of the object in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Record Location | Page Report, Web Report, Library Component | Specifies the calculation point for the properties of the object that are controlled by formulas. This property takes effect only when the object is in a banded object. Choose an option from the drop-down list.  * **default** Select to calculate values of the properties in the default location where the object is placed. * **page header** Select to calculate values of the properties in the banded page header panel. * **page footer** Select to calculate values of the properties in the banded page footer panel.   For more information, see [Example 2: Showing a Label on Every Page Except the Last](https://devnet.logianalytics.com/hc/en-us/articles/4405664601367-Using-Formulas-to-Control-Object-Properties#Example2).  Data type: Enumeration |
| Suppress | Query Page Report | Specifies whether to suppress the object in the design area and in the report. If you suppress an object, Logi Report Engine skips all formulas and calculations that involve the object. This property has higher priority over Invisible. Data type: Boolean |
| Suppress When No Records | Query Page Report | Specifies whether to suppress the object in the report when no record is returned to its parent data component. Data type: Boolean |
| Transfer Style | Page Report, Web Report, Library Component | Specifies whether to apply the style group of the primary report to the linked report, when the object is linked to another report. Data type: Boolean |
| Vertical Alignment | Page Report, Web Report, Library Component | Specifies the vertical alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Excel | | |
| Column Index | Page Report, Web Report | Specifies the X coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Column Number | Page Report, Web Report | Specifies the number of columns to determine the width of the object in the Excel output. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true". Type an integer value to change the number. Data type: Integer |
| Row Index | Page Report, Web Report | Specifies the Y coordinate of the object relative to its parent container in the Excel output, measured in cells. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true" and Position of the object is not "static". Data type: Integer |
| Row Number | Page Report, Web Report | Specifies the number of rows to determine the height of the object in the Excel output. This property takes effect when you set [Columned](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#Column) of the page report tab or web report to "true". Type an integer value to change the number. Data type: Integer |
| Image Property | | |
| Alternate Text | Page Report, Web Report, Library Component | Specifies the text you want to show instead when the image cannot display. Data type: String |
| Disabled | Page Report, Web Report, Library Component | Specifies whether to disable actions on the image. Data type: Boolean |
| Image Name | Page Report, Web Report, Library Component | Specifies the file name of the image. The image can be one on your local file system or retrieved by using a URL. Data type: String |
| Maximum Scaling Ratio | Page Report, Web Report, Library Component | Specifies the maximum scaling ratio of the image. By default, the scaling ratio of the image is not limited. If you set the ratio to any value greater than 0, the actual scaling ratio is less than or equal to it. Data type: Float |
| Name | Page Report, Web Report, Library Component | Specifies the name of the image. Data type: String |
| Rotation | Page Report, Web Report, Library Component | Specifies the angle at which to rotate the image, in degrees. 0 means no rotation; a positive value means to rotate the image clockwise; a negative value means to rotate the image anticlockwise. Data type: Float |
| Scaling Mode | Page Report, Web Report, Library Component | Specifies the scaling mode of the image, which controls the image behavior when you adjust the size of the area for displaying the image. Choose an option from the drop-down list.  * **actual size** - Select to show the image in its actual size. If the size of the area for displaying the image is smaller than that of the image, part of the image will be cut off. * **fit image** - Select to adjust the image to fill up the area for displaying the image, with its original perspective remained but under the limitation of [Maximum Scaling Ratio](#Ratio). * **fit width** - Select to adjust the image to fit the width of the area for displaying the image but under the limitation of Maximum Scaling Ratio. * **fit height** - Select to adjust the image to fit the height of the area for displaying the image but under the limitation of Maximum Scaling Ratio. * **customize** - Select to adjust the image to fit the area for displaying the image, regardless of Maximum Scaling Ratio.   Data type: Enumeration |
| Tab Index | Page Report, Web Report, Library Component | Specifies the index that defines the tab order for the image. Data type: Integer |
| Title | Page Report, Web Report, Library Component | Specifies the tool tip information of the image, which displays when you hover over the image in HTML output or at runtime. Data type: String |
| Value | Page Report, Web Report, Library Component | Specifies the initial value of the image. Data type: String |
| [Event](#Event) | | |
| On Blur | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the image loses input focus. Data type: String |
| On Click | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user selects the left mouse button on the image. Data type: String |
| On Double click | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user double-clicks the image. Data type: String |
| On Focus | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the image receives focus. Data type: String |
| On Key Down | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user presses a key. Data type: String |
| On Key Press | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user presses an alphanumeric key. Data type: String |
| On Key Up | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user releases a key. Data type: String |
| On Mouse Down | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user selects the image with either mouse button. Data type: String |
| On Mouse Move | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user moves the mouse over the image. Data type: String |
| On Mouse Out | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user moves the mouse pointer outside the boundaries of the image. Data type: String |
| On Mouse Over | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user moves the mouse pointer into the image. Data type: String |
| On Mouse Up | Page Report, Web Report, Library Component | Specifies the action you want to trigger from the image at runtime when the user releases a mouse button while the mouse is over the image. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/4405661931671-Editing-Reports#TOC) (available when the image is in a banded object) | | |
| Anchor Display Value | Page Report | Specifies the text you want to display as the object's TOC entry label. This property takes effect when you set TOC Anchor of the object to "true". Data type: String |
| TOC Anchor | Page Report | Specifies whether to include the object in the TOC of the report. Data type: Boolean |
| [Accessibility](https://devnet.logianalytics.com/hc/en-us/articles/4405664594583-Exporting-Reports-to-Accessible-HTML-and-PDF#HTML) | | |
| External AccessKey | Query Page Report | This property is mapped to the HTML attribute *accesskey*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External CSS Class Selector | Query Page Report | Specifies the name of the Class Selector for the object in the HTML output. Data type: String |
| External ID | Query Page Report | This property is mapped to the HTML attribute *id*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| External Style | Query Page Report | This property is mapped to the HTML attribute *style*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| HrefLang | Query Page Report | This property is mapped to the HTML attribute *hreflang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). You can use it to specify the base language of the resource designated by a link on the object, such as the target you define via the [Link](#Link) property. Data type: String |
| Language | Query Page Report | This property is mapped to the HTML attribute *lang*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |
| LongDesc | Query Page Report | This property is mapped to the HTML attribute *longdesc*, as specified by [w3.org](https://www.w3.org/TR/html401/index/attributes.html). Data type: String |

## Event

The values for this group of properties are based on the Image Client API in Version 7. The following table lists their mapping values in current version. For more information about the descriptions and parameters of the mapping values, see [Appendix 3: Parameters of User-Defined Web Actions](https://devnet.logianalytics.com/hc/en-us/articles/4405661328535-Appendix-3-Parameters-of-User-Defined-Web-Actions).

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661862039-Group-Control-Image-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661864599-KPI-Properties)
