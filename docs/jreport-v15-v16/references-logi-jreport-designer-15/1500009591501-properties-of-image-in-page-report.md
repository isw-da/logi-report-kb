---
title: "Properties of Image in Page Report"
id: 1500009591501
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009591501-Properties-of-Image-in-Page-Report
updated_at: 2021-07-24T05:54:10Z
---

# Properties of Image in Page Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569622-Properties-of-Geographic-Map-Marker-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report)

# Properties of Image in Page Report

The properties of an image object in a page report are:

| Property Name | Description |
| --- | --- |
| General | |
| Class Type | Indicates the class type of the object. This property is read only. |
| Instance Name | Shows the instance name of the object. This property is read only. |
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
| Detail Report | Specifies the detail report that the object is linked to. Select  in the value cell to set the detail report. For details, refer to [Linking to a Detail Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label#Detail). Data type: String |
| Detail Target Frame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [Go To Detail](#GoToDetail) is set to true. Choose an option from the drop-down list.  * **<Server Setting>**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the detailed information into a new window. The window is not named. * **Whole Window**  Loads the detailed information into the full browser window. * **Same Frame**  Loads the detailed information into the same frame as the object. * **Parent Frame**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If selected, you can also directly input the name of the frame you have defined in the text box. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
| Export to Applet | Specifies whether to include the object when exporting the report to Applet. Data type: Boolean |
| Export to Excel | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
| Export to HTML | Specifies whether to include the object when exporting the report to HTML. Data type: Boolean |
| Export to PDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
| Export to PostScript | Specifies whether to include the object when exporting the report to PostScript. Data type: Boolean |
| Export to Report Result | Specifies whether to include the object when exporting the report to Report Result. Data type: Boolean |
| Export to RTF | Specifies whether to include the object when exporting the report to RTF. Data type: Boolean |
| Go to Detail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. For details about its usage, refer to [Obtaining Detailed Information from a Banded Object](https://devnet.logianalytics.com/hc/en-us/articles/1500009592841-Obtaining-Detailed-Information-from-a-Banded-Object). Data type: Boolean |
| Horizontal Alignment | Specifies the horizontal alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Invisible | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Link | Specifies to link the object to another report, a website, an e-mail address or a Blob data type field. Select  in the value cell to set the link target. For details, see [Binding a Link to a Label](https://devnet.logianalytics.com/hc/en-us/articles/1500009563442-Binding-a-Link-to-a-Label). Data type: String |
| Logic Column | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Choose an option from the drop-down list. Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
| [Position](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#Position) | Specifies the position of the object. Choose an option from the drop-down list.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration |
| [Record Location](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report#RecordLocation) | Specifies the calculation point for the properties which use formulas. Choose an option from the drop-down list.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
| Suppress | Specifies whether to show the object in the design area and in the report results. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppress properties of an object are set to true, Suppress has the higher priority. |
| Suppress When No Records | Specifies whether to display the object in the report results when no record is returned to its parent data component. Data type: Boolean |
| Transfer Style | Specifies whether the style group of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
| Vertical Alignment | Specifies the vertical alignment of the image in the container. Choose an option from the drop-down list. Data type: Enumeration |
| Excel | |
| [Column Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Column Number | Specifies the number of columns which will be the object's width in the exported Excel file. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| [Row Index](https://devnet.logianalytics.com/hc/en-us/articles/1500009569342-Properties-of-Banded-Object-in-Page-Report#Index) | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Row Number | Specifies the number of rows which will be the object's height in the exported Excel file. The [Columned](https://devnet.logianalytics.com/hc/en-us/articles/1500009591741-Properties-of-Page-Report-Tab#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
| Image Property | |
| Alternate Text | Specifies the text that will be displayed instead if the image cannot be displayed. Data type: String |
| Disabled | Specifies whether to disable the actions on the image. Data type: Boolean |
| Image Name | Specifies the file name of the image. The image can be one on your local file system or retrieved by using a URL. Data type: String |
| Maximum Scaling Ratio | Specifies the maximum ratio up to which the image can be scaled. Data type: Float |
| Name | Specifies the name of the image. Data type: String |
| Rotation | Specifies the angle at which to rotate the image, in degrees. The following is the meaning of different values:  * 0 - No rotation. * positive value - Rotates the image clockwise. * negative value - Rotates the image anticlockwise.   Data type: Float |
| Scaling Mode | Specifies the scaling mode of the image, which controls the image behavior when you try to adjust the image field size. Choose an option from the drop-down list.  * **actual size** - The image will remain its original size. If the image field size is smaller than the image size, part of the image will be cut off. * **fit image** - The image size will be automatically adjusted to fill up the image field, with its original perspective remained but under the limitation of Maximum Scaling Ratio. * **fit width** - The image will be automatically adjusted to fit the width of the image field but under the limitation of Maximum Scaling Ratio. * **fit height** - The image will be automatically adjusted to fit the height of the image field but under the limitation of Maximum Scaling Ratio. * **customize** - The image size will be automatically adjusted to fit the image field, regardless of the [Maximum Scaling Ratio](#Ratio)'s value.   Data type: Enumeration |
| Tab Index | Specifies the index that defines the tab order for the image. Data type: Integer |
| Title | Specifies the tip information about the image, which will be displayed when you hover the mouse pointer over the image in HTML result or Page Report Studio. Data type: String |
| Value | Specifies the initial value of the image. Data type: String |
| Event | |
| [On Blur](#Event) | Specifies the action when the object loses input focus. Data type: String |
| [On Select](#Event) | Specifies the action when the user selects the left mouse button on the object. Data type: String |
| [On Double Select](#Event) | Specifies the action when the user double-clicks the object. Data type: String |
| [On Focus](#Event) | Specifies the action when the object receives focus. Data type: String |
| [On Key Down](#Event) | Specifies the action when the user presses a key. Data type: String |
| [On Key Press](#Event) | Specifies the action when the user presses an alphanumeric key. Data type: String |
| [On Key Up](#Event) | Specifies the action when the user releases a key. Data type: String |
| [On Mouse Down](#Event) | Specifies the action when the user selects the object with either mouse button. Data type: String |
| [On Mouse Move](#Event) | Specifies the action when the user moves the mouse over the object. Data type: String |
| [On Mouse Out](#Event) | Specifies the action when the user moves the mouse pointer outside the boundaries of the object. Data type: String |
| [On Mouse Over](#Event) | Specifies the action when the user moves the mouse pointer into the object. Data type: String |
| [On Mouse Up](#Event) | Specifies the action when the user releases a mouse button while the mouse is over the object. Data type: String |
| [TOC](https://devnet.logianalytics.com/hc/en-us/articles/1500009570982-Editing-a-Page-Report#TOC) | |
| Anchor Display Value | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOC Anchor property must be set to true for this property to take effect. Data type: String |
| TOC Anchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Accessibility | |
| External AccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
| External CSS Class Selector | Specifies a class selector to be applied to the object when exported as HTML. Enter a valid class name from the CSS file. Data type: String |
| External ID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
| External Style | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
| HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
| Language | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
| LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |

## Event property values

The provided values are based on the image client API in Version 7. The following table lists their mapping values in current version. For information about the descriptions and parameters of the mapping values, see [Appendix 2: Parameters of User Defined Web Actions](https://devnet.logianalytics.com/hc/en-us/articles/1500009582961-Appendix-2-Parameters-of-User-Defined-Web-Actions).

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
| saveRst() |  |
| showExportExcelDlg() |  |
| showExportHTMLDlg() |  |
| showExportPDFDlg() |  |
| showExportPSDlg() | user\_showSaveResultDialog() |
| showExportRtfDlg() |  |
| showExportTextDlg() |  |
| showExportXmlDlg() |  |
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

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009569622-Properties-of-Geographic-Map-Marker-in-Page-Report)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009569642-Properties-of-Label-in-Page-Report)
