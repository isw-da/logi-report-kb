---
title: "Getting Property Information"
id: 1500009562502
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562502-Getting-Property-Information
updated_at: 2021-07-24T05:56:17Z
---

# Getting Property Information

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562442-Inserting-Moving-and-Deleting-an-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582841-Getting-Report-Metadata-Information)

# Getting Property Information

All the methods mentioned in this topic are provided in the API class. Use the corresponding method to get the property information which you want.

Below is a list of the sections covered in this topic:

> * [Getting Property Value](#Value)
> * [Getting Property Name, Type, and Checking Property Name](#Name)
> * [Changing Property Value](#Change)

## Getting Property Value

The following methods are used for getting the property values of different types and return the property value:

* getInt(String handle, String name)
* getLong(String handle, String name)
* getFloat(String handle, String name)
* getDouble(String handle, String name)
* getString(String handle, String name)
* getBool(String handle, String name)
* getColor(String handle, String name)
* getControlFields(String handle, String name)

**Parameters**

* handle - Object handle.
* name - Property name.

**Note:** The getControlFields(String handle, String name) method is used for getting fields that can control property values at runtime.

## Getting Property Name, Type, and Checking Property Name

* **getPropType(String handle, String name)**  
   Gets and returns the property type defined in the Designer class.
* **getPropnames(String handle)**  
   Gets property names and returns a name array.
* **containPropName(String handle, String name)**  
   Checks whether the property name exists. If it exists, it will return true.

**Parameters**

* handle - Selected object handle.
* name - Name of the property.

## Changing Property Value

The following methods are used for changing the property values of different types. They will return true if the value is changed.

* set(String handle, String name, Boolean value)
* set(String handle, String name, int value)
* set(String handle, String name, long value)
* set(String handle, String name, float value)
* set(String handle, String name, double value)
* set(String handle, String name, String value)
* set(String handle, String name, Color value)
* setReference(String handle, String name, String refHandle)
* setControlFields(String handle, String prop, String field)

**Parameters**

* handle - Target object handle.
* name - Property name.
* value - Property value.
* refHandle - Referenced object handle.
* prop - Property name.

**Note:** The setControlFields(String handle, String prop, String field) method is used for setting a field to control the property value at runtime. The setReference(String handle, String name, String refHandle) method is used for changing the reference property value of an object.

Below table lists the properties of the most commonly used objects and their descriptions:

| Object | Property Name | Description |
| --- | --- | --- |
| Report | AfterInitParameter | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called after you set parameters in the pop-up parameter dialog when running the report. Data type: String |
|  | AfterRun | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called immediately after Logi JReport Engine has finished running the report result. Data type: String |
|  | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AppletHeight | Specifies the applet height for running an exported applet in a web browser. Data type: Float |
|  | AppletWidth | Specifies the applet width for running an exported applet in a web browser. Data type: Float |
|  | BeforeRun | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called at the point Logi JReport Engine is about to run the report. Data type: String |
|  | Columned | If true, the engine performance will be improved when exporting the report to CSV or Excel format. Only after the Columned property is set to true, it is meaningful to specify values to the following Excel properties of objects in the report, otherwise the specified values for these Excel properties cannot take effect.   * ColumnIndex/RowIndex * ColumnNumber/RowNumber. The properties are for chart platforms, images and UDOs. * TopAttachCol/TopAttachRow/BottomAttachCol/BottomAttachRow. The properties are for drawing objects.   Data type: Boolean |
|  | ColumnWidthList | Specifies the width of columns beginning from the first column for the exported Excel sheet. The Columned property must be set to true for this property to take effect. Use semicolon (;) to separate each width, for example: 12;8;15;10;9  The example specifies the width of the first 5 columns. For the other columns, they take the default width of Microsoft Excel sheet.  8 indicates the default column width in Microsoft Excel sheet. It can be omitted. The above example can also be written as 12;;15;10;9  Data type: String |
|  | DataDriver | Specifies the cached query result file as the data resource. Usually used for support purpose. The input format for cached query result file is as follows: `jrquery:/jet.universe.resultfile.UResultFileResultSet;Fullpath_of_cached_query_result`  Data type: String |
|  | EmbeddedFonts | Specifies the True Type Fonts that have been used in the report so as to embed them if you want to export the report result to a PDF file. Data type: String |
|  | ExcelBufferSize | Specifies the number of report result sheets which will be stored in the buffer when exporting the report to Excel. Data type: Integer |
|  | FastPass | If true, the engine performance will be improved when running the report to CSV format in multiple threads on Logi JReport Server. To make fast pass work, the property Columned should be true.  Data type: Boolean |
|  | ImportJavaScript | Specifies the name of a JavaScript file you develop to apply customized functions in Page Report Studio, for example, user1.js. Your JavaScript file should be located in `<server_install_root>\public_html\javascript\dhtml`.  Data type: String |
|  | ImportParamValues | Specifies the name of a class file from which to import default values for parameters used in the report, for example, TestParamList. Then when viewing the report, the displayed Enter Parameter Values dialog will only list the imported default parameters. To make the property work, you need specify the ParaListAuto property to false.  Data type: String |
|  | MaxPageNumber | Specifies the maximum number of pages in the data buffer. Data type: Integer |
|  | MaxRecords | Specifies the maximum number of records you want to display for all of the data components using this dataset. The default is to display all the records. Data type: Integer |
|  | NoTempFile | Specifies whether or not to create temporary files.  * **true** - Not to create temporary files. Gains faster engine performance. * **false** - To create temporary files. Gains better accuracy in calculating data.   Data type: String |
|  | PageBackground | Specifies the background color of the report page. Data type: String |
|  | ParaListAuto | Specifies whether to get the default values for parameters used in the report from values defined in the catalog.  * **true** - Gets parameter default values from values defined in catalog. * **false** - Gets parameter default values from the class file specified by the ImportParamValues property.   Data type: String |
|  | RecordsPerPage | Specifies the number of records in each page in the data buffer. Data type: Integer |
|  | ResultBufferSize | Specifies the number of report result pages which will be stored in the buffer. Data type: Integer |
|  | RowsPerSheet | Specifies the maximum number of rows for every worksheet when exporting the report to Excel. For the Excel version Excel 97-2003 Workbook (\*.xls), the value ranges from 0 to 65000. Any value out of the range will be considered as 65000. For the Excel version Excel Workbook (\*.xlsx), the value ranges from 0 to 1048000. Any value out of the range will be considered as 1048000.  Data type: Integer |
|  | ShowSubHeaderFooter | Specifies whether or not to show the page header and footer panels of subreports in the report.  * **true** - The page header and page footer panels of subreports in the report will be displayed when the panels are set to be visible in the subreports. * **false** - The page header and page footer panels of subreports in the report will not be displayed.   Data type: String |
|  | ShrinkFooter | Specifies whether to hide the group footer panel when collapsing a group in Page Report Studio. Only works in continuous page mode. Data type: Boolean |
|  | StyleGroup | Specifies the style group for the report. If the report is to be used as a subreport, specify any style group to turn on the style group feature for the report and it will inherit the styles of the primary report; do not set this property or specify it as None to turn off the style group feature for the report and it will not inherit styles from the primary report  Data type: String |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Page | BottomMargin | Specifies the distance in inches or centimeters between the bottom page edge and the data area. Data type: Float |
|  | Height | Specifies the height of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Data type: Float |
|  | LeftMargin | Specifies the distance in inches or centimeters between the left page edge and the data area. Data type: Float |
|  | Orientation | Specifies how to position the report page. The Orientation setting affects the Width and Height values.  * **portrait** - The page is positioned vertically. * **landscape** - The page is positioned horizontally.   Data type: Enumeration |
|  | PageType | Specifies the report page dimensions. Data type: Enumeration |
|  | RightMargin | Specifies the distance in inches or centimeters between the right page edge and the data area. Data type: Float |
|  | TopMargin | Specifies the distance in inches or centimeters between the top page edge and the data area. Data type: Float |
|  | Width | Specifies the width of the page in inches or centimeters. The Width and Height values change when Orientation changes. The Page Type setting determines the Width and Height values but you can change the latter as desired. Data type: Float |
| Group | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | Cascade | Specifies whether to allow the security identifiers specified by the following three properties to view the group's detail or child groups.  * **true** - The detail panel, the group header panel, and the group footer panel will be displayed. * **false** - Only the group header and footer panels will be displayed.   Data type: String |
|  | currentBlockIndex | The two properties, currentBlockIndex and itemsPerBlock, work together to control the data of the object to be displayed in continuous page mode. currentBlockIndex specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
|  | Grant | Enables to set cached report bursting. The property accepts user names delimited by "|" as the value. You can specify which group of data can be viewed by which user. Data type: String |
|  | Groups | Enables to set cached report bursting. The property accepts group names delimited by "|" as the value. You can specify which group of data can be viewed by which group of users. Data type: String |
|  | isExpandData | Specifies whether to enable Page Report Studio users to expand/collapse dimensions in the crosstab. This property works only in continuous page mode. Data type: Boolean |
|  | itemsPerBlock | The two properties, currentBlockIndex and itemsPerBlock, work together to control the data of the object to be displayed in continuous page mode. itemsPerBlock specifies the number of records in each data block.  Data type: Integer |
|  | KeepGroupTogether | Specifies whether to keep the whole group together. Data type: Boolean |
|  | RepeatWhileGF | If the group header is set to be repeated, you can specify whether to repeat the group header when a page break occurs on the group footer. Data type: Boolean |
|  | Roles | Enables to set cached report bursting. The property accepts role names delimited by "|" as the value. You can specify which group of data can be viewed by which role. Data type: String |
|  | ShrinkFooter | Specifies whether to hide the group footer panel when collapsing a group in Page Report Studio. Only works in continuous page mode. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
| Report Header | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | Specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is only applied if the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Report Footer | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | Specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is only applied if the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | ToBottom | Specifies whether to move the banded object footer panel to the bottom of the page. The default is false, which means that the banded object footer appears at the end of the banded object. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Page Header | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Displays the width of the object, in inches or centimeters. This property is read only. |
| Page Footer | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressInLastPage | If true, the footer panel on the last page will not be displayed. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Displays the width of the object, in inches or centimeters. This property is read only. |
| Group Header | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | MergeToNextPanel | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is only applied if the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RemoveBlankRow | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
|  | Repeat | Specifies whether to make the group header appear in every page. Data type: Boolean |
|  | RepeatInDetailPanel | Specifies whether to make the objects in the panel repeated in the detail panel in the exported Excel file. Data type: Boolean |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Group Footer | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | MergeToNextPanel | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is applied only when the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
|  | RightLine | Specifies the line style of the right border of the object. Data type: String |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Detail Panel | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CacheSection | Specifies whether to cache the objects in the detail panel. Data type: Boolean |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | currentBlockIndex | The two properties, currentBlockIndex and itemsPerBlock, work together to control the data of the object to be displayed in continuous page mode. currentBlockIndex specifies the index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on.  Data type: Integer |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | itemsPerBlock | The two properties, currentBlockIndex and itemsPerBlock, work together to control the data of the object to be displayed in continuous page mode. itemsPerBlock specifies the number of records in each data block.  Data type: Integer |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is applied only when the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RemoveBlankRow | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TileDetailSection | Specifies whether to tile records in the detail panel. For a vertical/horizontal banded object, you can make each set of records in the detail panel to be tiled when viewing the report if you set this property to true and set the detail panel's width/height equal to or less than 1/2 that of the banded object. The detail panel width/height defines the width/height of each record tile.  Data type: Boolean |
|  | TileHorizontal | If the TileDetailSection property of the detail panel is set to true, you can further specify the direction for tiling records in the detail panel.  * **true** - Records will be tiled in the row direction and then in column. * **false** - Records will be tiled in the column direction and then in row.   Data type: String |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Label | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AutoFit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BindColumn | When the label's [Sortable](#Sort1) or [Filterable](#Filter1) property is set to true, you need to specify a field as the value so that the records of the field can be sorted or filtered via the proper button beside the label when viewing the report in Page Report Studio. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | DetailReport | Specifies the detail report that the object is linked to. The link is available when the report runs in Page Report Studio. Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail1) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToPDF | Specifies whether to include the object when exporting the report to PDF. This property is available only when the label is displayed as a web control. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Filterable | Specifies whether the records can be filtered. If true, a filter button appears beside the label when viewing the report in Page Report Studio. You can use the button to filter the records based on a specific field's value. The field is specified via the [BindColumn](#BindCol1) property. Data type: Boolean |
|  | FilterOptions | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. If it is set to Default, the filter options displayed will be determined by the setting in the Profile dialog in Logi JReport Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).  Data type: Integer |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the background color of the object. Data type: String |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property can be a style sheet selector. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio, Web Report Studio or JDashboard. Data type: String |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. This property often works with the AutoFit property. If AutoFit = true and MaxWidth is not equal to 0, the text will extend until the width is this value.  Data type: Float |
|  | padding-bottom | Specifies the space in inches or centimeters between the text and the bottom border of the object. Data type: Float |
|  | padding-left | Specifies the space in inches or centimeters between the text and the left border of the object. Data type: Float |
|  | padding-right | Specifies the space in inches or centimeters between the text and the right border of the object. Data type: Float |
|  | padding-top | Specifies the space in inches or centimeters between the text and the top border of the object. Data type: Float |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50**% - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | Sortable | Specifies whether the records can be sorted. If true, a sort button appears beside the label when viewing the report in Page Report Studio. You can use the button to arrange the records of a specific field in ascending or descending order. The field is specified via the [BindColumn](#BindCol1) property. Data type: Boolean |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | Text | Specifies the text in the label. Data type: String |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position1) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position1) property is set to static. Data type: Float |
| DBField | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AutoFit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
|  | Background | Specifies the background color of the object. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CacheValue | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ColumnName | Substitutes the current field with another field. To make the property editable, uncheck Forbid changing column in the Options dialog (**File** > **Options** > **Panel** > **Forbid changing column**).  Data type: String |
|  | DataMappingFile | Specifies the data mapping file to the object for NLS use. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
|  | DetailReport | Specifies the detail report that the object is linked to. The link is available when the report runs in Page Report Studio. Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail2) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | DisplayNull | Specifies the string to be displayed if the field value is null. Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
|  | ExportToPDF | Specifies whether to include the object when exporting the report to PDF. This property is available only when the object is displayed as a web control. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | FilterOptions | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. If it is set to Default, the filter options displayed are decided by the setting in the Profile dialog in Logi JReport Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).  Data type: Integer |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the foreground color of the object. Data type: String |
|  | Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should specify a prefix JRD when setting the format property value. |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property can be a style sheet selector. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio, Web Report Studio or JDashboard. Data type: String |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. This property often works with the AutoFit property. If AutoFit = true and MaxWidth is not equal to 0, the text will extend until the width is this value.  Data type: Float |
|  | padding-bottom | Specifies the space in inches or centimeters between the text and the bottom border of the object. Data type: Float |
|  | padding-left | Specifies the space in inches or centimeters between the text and the left border of the object. Data type: Float |
|  | padding-right | Specifies the space in inches or centimeters between the text and the right border of the object. Data type: Float |
|  | padding-top | Specifies the space in inches or centimeters between the text and the top border of the object. Data type: Float |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report tab level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressedIfNull | If true and its value is null, the field will not be displayed. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | ValueDelimiter | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position2) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position2) property is set to static. Data type: Float |
| Parameter | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AutoFit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
|  | Background | Specifies the background color of the object. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | DataMappingFile | Specifies the data mapping file to the object for NLS use. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
|  | DetailReport | Specifies the detail report that the object is linked to. The link is available when the report runs in Page Report Studio. Data type: Boolean |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail3) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | DisplayNull | Specifies the string to be displayed if the field value is null. Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToPDF | Specifies whether to include the object when exporting the report to PDF. This property is available only when the object is displayed as a web control. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the foreground color of the object. Data type: String |
|  | Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should specify a prefix JRD when setting the format property value. |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property can be a style sheet selector. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio or Web Report Studio. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. This property often works with the AutoFit property. If AutoFit = true and MaxWidth is not equal to 0, the text will extend until the width is this value.  Data type: Float |
|  | padding-bottom | Specifies the space in inches or centimeters between the text and the bottom border of the object. Data type: Float |
|  | padding-left | Specifies the space in inches or centimeters between the text and the left border of the object. Data type: Float |
|  | padding-right | Specifies the space in inches or centimeters between the text and the right border of the object. Data type: Float |
|  | padding-top | Specifies the space in inches or centimeters between the text and the top border of the object. Data type: Float |
|  | Parameter | Substitutes the current parameter with another one. To make the property editable, uncheck Forbid changing parameter in the Options dialog (**File** > **Options** > **Panel** > **Forbid changing parameter**).  Data type: String |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressedIfNull | If true and its value is null, the field will not be displayed. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | ValueDelimiter | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position3) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position3) property is set to static. Data type: Float |
| Image | Alt | Specifies the text that will be displayed instead if the image cannot be displayed. Data type: String |
|  | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ColumnNumber | Specifies the number of columns which will be the object's width in the exported Excel file. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | DetailReport | Specifies the detail report that the object is linked to. The link is available when the report runs in Page Report Studio. Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail4) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | Disabled | Specifies whether to disable the actions on the image. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | HorizontalAlignment | Specifies the horizontal alignment of the image in the container. Data type: Enumeration |
|  | ID | Specifies the identifier of the object, which must be unique in the report. The ID property can be a style sheet selector. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio or Web Report Studio. Data type: String |
|  | LogicColumn | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxScalingRatio | Specifies the maximum ratio up to which the image can be scaled. Data type: Float |
|  | Name | Specifies the name of the image. Data type: String |
|  | onblur | Specifies the action when the object loses input focus. Data type: String |
|  | onclick | Specifies the action when the user selects the left mouse button on the object. Data type: String |
|  | ondblclick | Specifies the action when the user double-clicks the object. Data type: String |
|  | onfocus | Specifies the action when the object receives focus. Data type: String |
|  | onkeydown | Specifies the action when the user presses a key. Data type: String |
|  | onkeypress | Specifies the action when the user presses an alphanumeric key. Data type: String |
|  | onkeyup | Specifies the action when the user releases a key. Data type: String |
|  | onmousedown | Specifies the action when the user selects the object with either mouse button. Data type: String |
|  | onmousemove | Specifies the action when the user moves the mouse over the object. Data type: String |
|  | onmouseout | Specifies the action when the user moves the mouse pointer outside the boundaries of the object. Data type: String |
|  | onmouseover | Specifies the action when the user moves the mouse pointer into the object. Data type: String |
|  | onmouseup | Specifies the action when the user releases a mouse button while the mouse is over the object. Data type: String |
|  | PictureName | Specifies the file name of the image. The image can be one on your local file system or retrieved by using a URL. Data type: String |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: Enumeration |
|  | Rotation | Specifies the angle at which to rotate the image, in degrees. The following is the meaning of different values:  * 0 - No rotation. * positive value - Rotates the image clockwise. * negative value - Rotates the image anticlockwise.   Data type: Float |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | RowNumber | Specifies the number of rows which will be the object's height in the exported Excel file. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ScalingMode | Specifies the scaling mode of the image, which controls the image behavior when you try to adjust the image field size.  * **actual size** - The image will remain its original size. If the image field size is smaller than the image size, part of the image will be cut off. * **fit image** - The image size will be automatically adjusted to fill up the image field, with its original perspective remained but under the limitation of Maximum Scaling Ratio. * **fit width** - The image will be automatically adjusted to fit the width of the image field but under the limitation of Maximum Scaling Ratio. * **fit height** - The image will be automatically adjusted to fit the height of the image field but under the limitation of Maximum Scaling Ratio. * **customize** - The image size will be automatically adjusted to fit the image field, regardless of the [MaxScalingRatio](#Ratio)'s value.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | TabIndex | Specifies the index that defines the tab order for the image. Data type: Integer |
|  | Title | Specifies the tip information about the image, which will be displayed when you hover the mouse pointer over the image in HTML result, or at server runtime. Data type: String |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | Value | Specifies the initial value of the image. Data type: String |
|  | VerticalAlignment | Specifies the vertical alignment of the image in the container. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position4) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position4) property is set to static. Data type: Float |
| Special Field | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AutoFit | Specifies whether to adjust the width and height of the object according to the contents. Data type: Boolean |
|  | Background | Specifies the background color of the object. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | DetailReport | Specifies the detail report that the object is linked to. The link is available when the report runs in Page Report Studio. Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail5) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | DisplayNull | Specifies the string to be displayed if the field value is null. Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | FieldType | Specifies another special field format to substitute the current special field. Data type: Enumeration |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the foreground color of the object. Data type: String |
|  | Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should specify a prefix JRD when setting the format property value. |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property can be a style sheet selector. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. This property often works with the AutoFit property. If AutoFit = true and MaxWidth is not equal to 0, the text will extend until the width is this value.  Data type: Float |
|  | padding-bottom | Specifies the space in inches or centimeters between the text and the bottom border of the object. Data type: Float |
|  | padding-left | Specifies the space in inches or centimeters between the text and the left border of the object. Data type: Float |
|  | padding-right | Specifies the space in inches or centimeters between the text and the right border of the object. Data type: Float |
|  | padding-top | Specifies the space in inches or centimeters between the text and the top border of the object. Data type: Float |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50**% - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **relative** - The object is positioned at an offset to the position at which it is inserted. The offset is determined by the X and Y property values. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position5) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position5) property is set to static. Data type: Float |
| Crosstab | AlternativeLineColorDirection | Specifies whether the color defined by the property Pattern List will apply to the fields in the same rows or columns in the crosstab.  * **vertical** - The value of the property Pattern List will take effect on the fields in the same columns, except for the total columns. * **horizontal** - The value of the property Pattern List will take effect on the fields in the same rows, except for the total rows.   Data type: String |
|  | AlternativeLineColorPatternList | Specifies the color pattern for the fields in the same rows or columns in the crosstab. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient. Data type: String |
|  | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AvoidOrphanHeader | Specifies whether to make the column header be together with the data. Sometimes the column header happens to be at the bottom of a page. To keep the column header together with the data in the next page, set this property to true.  Data type: Boolean |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BlockGap | Specifies the space between each part if the crosstab is split into more than one part. Data type: Float |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BoundaryValue | Specifies the number of aggregate fields to be displayed in one column when displayed vertically, or in one row when displayed horizontally. The left fields will be word-wrapped. Data type: Integer |
|  | Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
|  | canExpandData | Specifies whether to enable Page Report Studio users to expand/collapse dimensions in the crosstab. This property works only in continuous page mode. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ColumnTotalOnLeft | Specifies whether to display the Total column in the first column in the crosstab. Data type: Boolean |
|  | currentColBlockIndex | Specifies the horizontal index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on. The four properties work together to control the data of the crosstab to be displayed in continuous page mode: currentRowBlockIndex, currentColBlockIndex, itemsPerRowBlock, and itemsPerColBlock.  Data type: Integer |
|  | currentRowBlockIndex | Specifies the vertical index of the data block that will be displayed. 0 means the first block index, and 1 the second, and so on. The four properties work together to control the data of the crosstab to be displayed in continuous page mode: currentRowBlockIndex, currentColBlockIndex, itemsPerRowBlock, and itemsPerColBlock.  Data type: Integer |
|  | EnableAlternativeLineColor | Specifies whether to enable setting alternating line color for the crosstab. Only when it is set to true, the settings for the properties Direction and Pattern List can take effect. Data type: Boolean  **Note:** The setting of the alternating line color function for crosstab can only take effect when all the aggregate fields in the crosstab have transparent background. |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Hasborder | Specifies whether to show the cell borders. Data type: Boolean |
|  | Height | Displays the height of the object, in inches or centimeters. This property is read only. |
|  | HorizontalGap | Specifies the space between the left/right edge of a crosstab cell and the contents in it. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | isOutSideAggTitle | Specifies to place the summary labels to the left of the row values if true, right of the row values if false. Data type: Boolean |
|  | isTableStyle | Specifies whether to add headers to the Total row and column. Data type: Boolean |
|  | itemsPerColBlock | Specifies the number of columns of records in each data block. The four properties work together to control the data of the crosstab to be displayed in continuous page mode: currentRowBlockIndex, currentColBlockIndex, itemsPerRowBlock, and itemsPerColBlock.  Data type: Integer |
|  | itemsPerRowBlock | Specifies the number of rows of records in each data block. The four properties work together to control the data of the crosstab to be displayed in continuous page mode: currentRowBlockIndex, currentColBlockIndex, itemsPerRowBlock, and itemsPerColBlock.  Data type: Integer |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | repeatAgg | Specifies whether to repeat the crosstab for different aggregate fields. Data type: Boolean |
|  | RepeatColumnHeader | Specifies whether to repeat column headings on every page. Data type: Boolean |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | RowTotalOnTop | Specifies whether to display the Total row in the first row of the crosstab. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Summary | It is mapped to the HTML attribute *[summary](http://www.w3.org/TR/html401/struct/tables.html#adef-summary)*. This attribute provides a summary of the object's purpose and structure. Data type: String |
|  | SuppressColumnHeader | Specifies whether to suppress the column header in view mode. Data type: Boolean |
|  | SuppressEmpty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressRowHeader | Specifies whether to suppress the row header in view mode. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | VerticalGap | Specifies the space between the top/bottom edge of a crosstab cell and the contents in it. Data type: Float |
|  | VerticalLayout | Indicates whether the aggregate fields are displayed vertically. The property is read only. |
|  | Width | Displays the width of the object, in inches or centimeters. This property is read only. |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position6) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position6) property is set to static. Data type: Float |
| Crosstab AggField | Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
|  | AutoFit | Specifies whether to adjust the width of the object according to the contents. Data type: Boolean |
|  | Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
|  | Background | Specifies the background color of the object. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CacheValue | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnName | Substitutes the current field with another field. To make the property editable, uncheck Forbid changing column in the Options dialog (**File** > **Options** > **Panel** > **Forbid changing column**).  Data type: String |
|  | DataMappingFile | Specifies the data mapping file to the object for NLS use. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail6) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | DisplayNull | Specifies the string to be displayed if the field value is null. Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToPDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the foreground color of the object. Data type: String |
|  | Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should specify a prefix JRD when setting the format property value. |
|  | FilterOptions | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. If it is set to Default, the filter options displayed are decided by the setting in the Profile dialog in Logi JReport Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).  Data type: Integer |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property can be a style sheet selector. Data type: String |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio, Web Report Studio or JDashboard. Data type: String |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. Data type: Float |
|  | padding-bottom | Specifies the space in inches or centimeters between the text and the bottom border of the object. Data type: Float |
|  | padding-left | Specifies the space in inches or centimeters between the text and the left border of the object. Data type: Float |
|  | padding-right | Specifies the space in inches or centimeters between the text and the right border of the object. Data type: Float |
|  | padding-top | Specifies the space in inches or centimeters between the text and the top border of the object. Data type: Float |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressedIfNull | If true and its value is null, the field will not be displayed. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | ValueDelimiter | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
|  | X | Displays the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is read only. |
|  | Y | Displays the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is read only. |
| Crosstab DBField | Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
|  | AutoFit | Specifies whether to adjust the width of the object according to the contents. Data type: Boolean |
|  | Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
|  | Background | Specifies the background color of the object. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CacheValue | Specifies whether to cache the value of the field instead of obtaining it repeatedly. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnName | Substitutes the current field with another field. To make the property editable, uncheck Forbid changing column in the Options dialog (**File** > **Options** > **Panel** > **Forbid changing column**).  Data type: String |
|  | DataMappingFile | Specifies the data mapping file to the object for NLS use. For example, if the data mapping file name is Category\_de\_DE.properties, set the value as Category (without the language and locale part).  Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail7) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | DisplayNull | Specifies the string to be displayed if the field value is null. Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExpandData | Specifies whether to enable Page Report Studio users to expand/collapse the details of the field which is as dimension (group level) in the crosstab. This property works only in continuous page mode and when the [canExpandData](#ExpandData) property of the crosstab is set to true. It is not available for aggregate field. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToPDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | FilterOptions | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. If it is set to Default, the filter options displayed are decided by the setting in the Profile dialog in Logi JReport Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).  Data type: Integer |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the foreground color of the object. Data type: String |
|  | Format | Specifies the display format of the text in the report result. It varies with data type and can be manually defined. Data type: String  **Note:** For the BigDecimal type, to avoid precision loss, you should specify a prefix JRD when setting the format property value. |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property value can be a style sheet selector. Data type: String |
|  | isExpandData | Specifies whether to display the details of the field by default in Page Report Studio. This property works only in continuous page mode, and is not available for aggregate field. It is meaningful to enable the property only when the field's ExpandData property is set to true. Data type: Boolean |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio, Web Report Studio or JDashboard. Data type: String |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. Data type: Float |
|  | Orderby | Specifies the field by which to sort the data. Not available for aggregate field. Data type: String |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressedIfNull | If true and its value is null, the field will not be displayed. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | ValueDelimiter | Specifies the separator for the data whose type is DBArray. The default value space means that the elements will be displayed in a horizontal line and separated by a space.  Data type: String |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Crosstab Text Field | Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
|  | Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BindColumn | When the label's [Sortable](#Sort2) or [Filterable](#Filter2) property is set to true, you need to specify a field as the value so that the records of the field can be sorted or filtered via the proper button beside the label when viewing the report in Page Report Studio. Data type: String |
|  | Bold | Specifies whether to make the text bold. Data type: Boolean |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | DetailTargetFrame | Specifies the target window or frame in which to display the detailed information. This property is enabled only when [GotoDetail](#GotoDetail8) is set to true.  * **“”**  Loads the detailed information according to setting of the Pop Up New Window for Links option in the Profile > Customize Profile > Page Report Studio > Properties > Default tab on Logi JReport Server. * **\_blank**  Loads the detailed information into a new window. The window is not named. * **\_top**  Loads the detailed information into the full browser window. * **\_self**  Loads the detailed information into the same frame as the object. * **\_parent**  Loads the detailed information into the parent frame of the frame in which the object is. * **Other Frame**  Loads the detailed information into some other specified frame. If the frame name does not exist, the detailed information will be loaded into a new window.   Data type: String |
|  | EnableHyperlinkOnExcel | Specifies whether to enable the hyperlink when exporting the report to an Excel file. Data type: Boolean |
|  | EnableHyperlinkOnHTML | Specifies whether to enable the hyperlink when exporting the report to an HTML file. Data type: Boolean |
|  | EnableHyperlinkOnPDF | Specifies whether to enable the hyperlink when exporting the report to a PDF file. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToPDF | Specifies whether to include the object when exporting the report to PDF. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalAccessKey | It is mapped to the HTML attribute *[accesskey](http://www.w3.org/TR/html401/interact/forms.html#adef-accesskey)*. This attribute specifies an access key to the object. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalDir | It is mapped to the HTML attribute *[dir](http://www.w3.org/TR/html401/struct/dirlang.html#adef-dir)*. This attribute specifies the base direction of directionally neutral text in the object's content and attribute values. It also specifies the directionality of tables. Possible values:  * LTR - Left-to-right text or table. * RTL - Right-to-left text or table.   Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTabIndex | It is mapped to the HTML attribute *[tabindex](http://www.w3.org/TR/html401/interact/forms.html#adef-tabindex)*. This attribute specifies the position of the object in the tabbing order for the current report. Specify an integer equal to or greater than 0 and less than 65535. Data type: Integer |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Filterable | Specifies whether the records can be filtered. If true, a filter button appears beside the label when viewing the report in Page Report Studio. You can use the button to filter the records based on a specific field's value. The field is specified via the [BindColumn](#BindCol2) property. Data type: Boolean |
|  | FilterOptions | Specifies the filter-related options that will be displayed on the shortcut menu when right-clicking the object in Page Report Studio. If it is set to Default, the filter options displayed will be determined by the setting in the Profile dialog in Logi JReport Server (Profile > Customize Profile > Page Report Studio > Properties > Default > Filter Menu).  Data type: Integer |
|  | FontFace | Specifies the font of the text. Data type: Enumeration |
|  | FontSize | Specifies the font size of the text. Data type: Integer |
|  | Foreground | Specifies the foreground color of the object. Data type: String |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio>. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
|  | HorizontalAlignment | Specifies the horizontal justification of the text in the object. Data type: Enumeration |
|  | HrefLang | It is mapped to the HTML attribute *[hreflang](http://www.w3.org/TR/html401/struct/links.html#adef-hreflang)*. This attribute specifies the base language of the resource designated by a link and may only be used when a link is specified. Data type: String |
|  | id | Specifies the identifier of the object, which must be unique in the report. The id property can be a style sheet selector. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Italic | Specifies whether to make the text italic. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | Link | Specifies to link the object to another report, a website, or an e-mail address. The link is available when the report runs in HTML, PDF, or Excel format, or in Page Report Studio, Web Report Studio or JDashboard. Data type: String |
|  | LongDesc | It is mapped to the HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MaxWidth | Specifies the maximum width of the text displayed. Data type: Float |
|  | padding-bottom | Specifies the space in inches or centimeters between the text and the bottom border of the object. Data type: Float |
|  | padding-left | Specifies the space in inches or centimeters between the text and the left border of the object. Data type: Float |
|  | padding-right | Specifies the space in inches or centimeters between the text and the right border of the object. Data type: Float |
|  | padding-top | Specifies the space in inches or centimeters between the text and the top border of the object. Data type: Float |
|  | PatternColor | Specifies the color in which to draw a pattern to fill the object. Data type: String |
|  | PatternStyle | Specifies the style of the pattern.  * **none** - No pattern will be applied to the object. * **50%** - The object will be filled in the Pattern Color of 50%-transparency. * **horizontal** - The pattern will be made of horizontal lines of the Pattern Color. * **vertical** - The pattern will be made of vertical lines of the Pattern Color. * **grid** - The pattern will be an overlapping of horizontal and vertical lines of the Pattern Color. * **diagonal** - The pattern will be made of diagonal lines of the Pattern Color.   Data type: String |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |
|  | Shadow | Specifies whether to draw two shadowed borders, beneath and to the right of the object. Data type: Boolean |
|  | ShadowColor | Specifies the color of the shadow. Data type: String |
|  | Sortable | Specifies whether the records can be sorted. If true, a sort button appears beside the label when viewing the report in Page Report Studio. You can use the button to arrange the records of a specific field in ascending or descending order. The field is specified via the [BindColumn](#BindCol2) property. Data type: Boolean |
|  | StrikeOut | Specifies whether to add a strikethrough line to the text. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressAggreate | Specifies whether to hide the Total row or column. Not applicable for CTLabelField. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | Text | Specifies the text in the label. Data type: String |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | TransferStyle | Specifies whether the style of the primary report will be applied to the linked report if the object is linked to a report. Data type: Boolean |
|  | TransWhileToHtml | Specifies whether or not to ignore the HTML tags when exporting the report result to HTML format.  * **true** - The text will appear in the HTML file the same as that in Logi JReport Designer (HTML tag elements in the text, if any, will not be parsed). * **false** - HTML tag elements in the text will be parsed when exporting the report result to HTML format.   This property is useful for exporting the report result to HTML format. You may want to write the label contents in HTML tags in your report, and for the exported HTML files, the tags will be transferred as they are translated into HTML.  Data type: String |
|  | Underline | Specifies whether to underline the text. Data type: Boolean |
|  | VerticalAlignment | Specifies the vertical justification of the text in the object. Data type: Enumeration |
|  | WordWrap | Specifies whether to wrap the text to the width. Data type: Boolean |
| Subreport | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Embedded | If false, the page header and footer of the subreport will not be shown. Data type: Boolean |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | MaxPageNum | Specifies the maximum number of pages in the data buffer. Data type: Integer |
|  | OnNewSheet | Specifies whether to put the subreport in a new sheet when exporting the report to Excel. Data type: Boolean |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a tabular cell, or a text box. |
|  | Postfix | Specifies how to add postfix number to the sheets in which the subreport will be put when exporting the report to Excel.  * **Add postfix number to every page** - Specifies to add the postfix number to every sheet for the subreport (Subreport1, Subreport2, Subreport3, Subreport4, ...). * **Add postfix number only to additional pages** - Specifies to add the postfix number to the subreport sheets starting from the second one (Subreport, Subreport1, Subreport2, Subreport3, ...).   It is meaningful to specify the property value when the OnNewSheet property is set to true.  Data type: String |
|  | RecPerPage | Specifies the number of records in each page in the data buffer. Data type: Integer |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | SheetName | Specifies the name of the new sheet in which the subreport will be put. Make sure the name specified here isn't used by any other sheets. It is meaningful to specify the property value when the OnNewSheet property is set to true.  Data type: String  **Note:** The characters "|", ":", "/", "?", "\", "\*", "]", "[" cannot be displayed in the sheet name in Excel and the last character in the sheet name cannot be single quotation mark ('). If any one of them is used when you specify the property, it will be replaced by "\_" in Excel. |
|  | SRQueryName | Displays the name of the query used by the subreport. This property is read only. |
|  | SRSecurity | Displays the security name (record level security) used by the subreport. This property is read only. |
|  | SRSourceName | Displays the name of the data source used by the subreport. If nothing is displayed, the default data source will be used. This property is read only. |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressEmpty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position7) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position7) property is set to static. Data type: Float |
| Line | BottomAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachCol specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | BottomAttachPosX | Specifies the horizontal coordinate of the bottom right point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachPosY | Specifies the vertical coordinate of the bottom right point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachRow specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LineColor | Specifies the color of the line. Data type: String |
|  | LineStyle | Specifies the style of the line. Data type: Enumeration |
|  | LineWidth | Specifies the thickness of the line. Data type: Float |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopAttachCol | The four Excel properties,TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachCol specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | TopAttachPosX | Specifies the horizontal coordinate of the top left point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachPosY | Specifies the vertical coordinate of the top left point of the line in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachRow specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Box | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderStyle | Specifies the line style of the box border. Data type: Enumeration |
|  | BorderWidth | Specifies the width of the object's border, in inches or centimeters. Data type: Float |
|  | BottomAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachCol specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | BottomAttachPosX | Specifies the horizontal coordinate of the bottom right point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachPosY | Specifies the vertical coordinate of the bottom right point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachRow specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachCol specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | TopAttachPosX | Specifies the horizontal coordinate of the top left point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachPosY | Specifies the vertical coordinate of the top left point of the box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachRow specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Round box | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the object's border. Data type: String |
|  | BorderStyle | Specifies the line style of the object's border. Data type: Enumeration |
|  | BorderWidth | Specifies the width of the object's border, in inches or centimeters. Data type: Float |
|  | BottomAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachCol specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | BottomAttachPosX | Specifies the horizontal coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachPosY | Specifies the vertical coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachRow specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | CornerFactor | Specifies the relative radius of the object's corners. Data type: Float |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachCol specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | TopAttachPosX | Specifies the horizontal coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachPosY | Specifies the vertical coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachRow specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Oval | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the object's border. Data type: String |
|  | BorderStyle | Specifies the line style of the object's border. Data type: Enumeration |
|  | BorderWidth | Specifies the width of the object's border, in inches or centimeters. Data type: Float |
|  | BottomAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachCol specifies the X coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | BottomAttachPosX | Specifies the horizontal coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachPosY | Specifies the vertical coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. BottomAttachRow specifies the Y coordinate of the lower right corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopAttachCol | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachCol specifies the X coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
|  | TopAttachPosX | Specifies the horizontal coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachPosY | Specifies the vertical coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachRow | The four Excel properties, TopAttachCol, TopAttachRow, BottomAttachCol and BottomAttachRow, work together to control the position of a drawing object in the exported Excel file. TopAttachRow specifies the Y coordinate of the upper left corner of the drawing object in the exported Excel file, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect.  Data type: Float |
| Arc | ArcAngle | Specifies the angle of the arc, in degrees. The value ranges from 0 to 360. As it gets closer to 360, the arc begins to take on an elliptical shape. Data type: Float |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the object's border. Data type: String |
|  | BorderStyle | Specifies the line style of the object's border. Data type: Enumeration |
|  | BorderWidth | Specifies the width of the object's border, in inches or centimeters. Data type: Float |
|  | BottomAttachPosX | Specifies the horizontal coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | BottomAttachPosY | Specifies the vertical coordinate of the bottom right point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | StartAngle | Specifies the start angle of the arc, in degrees. The value ranges from 0 to 360. At 0, the vertex of the arc starts at 12:15 clock position. As it gets closer to 360, the arc travels in a counterclockwise motion. Data type: Float |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopAttachPosX | Specifies the horizontal coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
|  | TopAttachPosY | Specifies the vertical coordinate of the top left point of the focus box in a banded panel. A drawing object can cross panels and the coordinate indicates the relative position in the involved panel. Data type: Float |
| Table | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AutoExpands | Specifies whether the objects in cells of the table will expand to their empty neighbouring cells horizontally when the actual size of the objects is bigger than the cells due to no enough column or page width for auto fit. This property requires that the property AutoFit for the objects in the table cells is set to true. Data type: Boolean  **Note:** The property does not apply to horizontal tables. |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Horizontal | Specifies whether to show the table in horizontal style. Data type: Boolean |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Summary | It is mapped to the HTML attribute *[summary](http://www.w3.org/TR/html401/struct/tables.html#adef-summary)*. This attribute provides a summary of the object's purpose and structure. Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressEmpty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position8) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position8) property is set to static. Data type: Float |
| Table Column | AutoFit | Specifies whether to adjust the width of the object according to the contents. If the property is set to true, the width of the object will be adjusted automatically only when:   * The position property for the field/label in this object is static or relative. * If the position property for the field/label in this object is absolute, then the AutoFit property for the field/label should be set to true.   Data type: Boolean |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
| Table Cell | Abbr | It is mapped to the HTML attribute *[abbr](http://www.w3.org/TR/html401/struct/tables.html#adef-abbr)*. This attribute specifies an abbreviated form of the content of the object. The abbreviated text may be rendered by user agents when appropriate in place of the object's content. Data type: String |
|  | Axis | It is mapped to the HTML attribute *[axis](http://www.w3.org/TR/html401/struct/tables.html#adef-axis)*. This attribute is used to place a cell into conceptual categories that can be considered to form axes in an n-dimensional space. The value of this attribute is a comma-separated list of category names. Data type: String |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | Headers | It is mapped to the HTML attribute *[headers](http://www.w3.org/TR/html401/struct/tables.html#adef-headers)*. This attribute specifies the list of header cells that provide header information for the current data cell. The value of this attribute is a space-separated list of cell names; those cells must be named by setting their *id* attribute. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HorizontalAlignment | Specifies the horizontal justification of the content in the table cell. Data type: Enumeration  **Note:** When the position property of the object in the table cell is set to absolute, this property does not take effect. |
|  | JoiningMerge | Specifies whether to make all the sequential rows included in the cell vertically merged in the report result. It is meaningful to set the property only when the cell is merged with other cells in the same column. Data type: Boolean |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | Repeat | Specifies whether to repeat the content of the cell in every page of the report result when the cell is split into pages. Available only for vertically merged cell. Data type: Boolean |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | Scope | It is mapped to the HTML attribute *[scope](http://www.w3.org/TR/html401/struct/tables.html#adef-scope)*. This attribute specifies the set of data cells for which the current header cell provides header information. Available values are:  * **Row** - The current cell provides header information for the rest of the row that contains it. * **Column** - The current cell provides header information for the rest of the column that contains it. * **none** - The scope attribute will not be generated when exporting to HTML.   Data type: String |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | VerticalAlignment | Specifies the vertical justification of the content in the table cell. Data type: Enumeration  **Note:** When the position property of the object in the table cell is set to absolute, this property does not take effect. |
|  | Width | Specifies the width of the object, in inches or centimeters. |
| Reportset | ImportParamValues | Specifies the name of a class file from which to import default values for parameters used in the report, for example, TestParamList. Then when viewing the report, the displayed Enter Parameter Values dialog will only list the imported default parameters. To make the property work, you need specify the ParaListAuto property to false.  Data type: String |
|  | ParaListAuto | Specifies whether to get the default values for parameters used in the report from values defined in the catalog.  * **true** - Gets parameter default values from values defined in catalog. * **false** - Gets parameter default values from the class file specified by the Import Parameter Values property.   Data type: String |
| Dataset | dsName | Specifies the name of the data source. Data type: String |
|  | MaxPageNumber | Specifies the maximum number of pages in the data buffer. Data type: Integer |
|  | MaxRecords | Specifies the maximum number of records you want to display for all of the data components using this dataset. The default is to display all the records. Data type: Integer |
|  | queryName | Shows the name of the query in use. This property is read only. |
|  | RecordsPerPage | Specifies the number of records in each page in the data buffer. Data type: Integer |
|  | SecurityName | Specifies the name of the data source security imported from the catalog. Data type: String  **Note:** Column-level security (CLS) is not supported on library component at present, so for a library component, only the data source security policies which have not been defined with CLS will be available in the value list. |
| Report Body | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressEmpty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
| Report Sheet | AfterInitParameter | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called after you set parameters in the pop-up parameter dialog when running the report. Data type: String |
|  | AfterRun | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called immediately after Logi JReport Engine has finished running the report result. Data type: String |
|  | AppletHeight | Specifies the applet height for running an exported applet in a web browser. Data type: Float |
|  | AppletWidth | Specifies the applet width for running an exported applet in a web browser. Data type: Float |
|  | BeforeRun | This property is for exit function usage. You can specify an external application file (Java class file) which develops an action. The action will be called at the point Logi JReport Engine is about to run the report. Data type: String |
|  | Columned | If true, the engine performance will be improved when exporting the report to CSV or Excel format. Only after the Columned property is set to true, it is meaningful to specify values to the following Excel properties of objects in the report, otherwise the specified values for these Excel properties cannot take effect.   * ColumnIndex/RowIndex * ColumnNumber/RowNumber. The properties are for chart platforms, images and UDOs. * TopAttachCol/TopAttachRow/BottomAttachCol/BottomAttachRow. The properties are for drawing objects.   Data type: Boolean |
|  | ColumnWidthList | Specifies the width of columns beginning from the first column for the exported Excel sheet. The Columned property must be set to true for this property to take effect. Use semicolon (;) to separate each width, for example: 12;8;15;10;9  The example specifies the width of the first 5 columns. For the other columns, they take the default width of Microsoft Excel sheet.  8 indicates the default column width in Microsoft Excel sheet. It can be omitted. The above example can also be written as 12;;15;10;9  Data type: String |
|  | EmbeddedFonts | Specifies the True Type Fonts that have been used in the report so as to embed them if you want to export the report result to a PDF file. Data type: String |
|  | ExcelBufferSize | Specifies the number of report result sheets which will be stored in the buffer when exporting the report to Excel. Data type: Integer |
|  | FastPass | If true, the engine performance will be improved when running the report to CSV format in multiple threads on Logi JReport Server. To make fast pass work, the property Columned should be true.  Data type: Boolean |
|  | ImportJavaScript | Specifies the name of a JavaScript file you develop to apply customized functions in Page Report Studio, for example, user1.js. Your JavaScript file should be located in <server\_install\_root>\public\_html\javascript\dhtml.  Data type: String |
|  | InitReportCube | Specifies whether or not to enable the automatic cube conversion.  * **true** - If true, it is to convert the query based report to a report cube based report automatically when opening the report in Page Report Studio for analytic reporting purpose. If the converting fails due to error or incomplete conditions, no warning message will be shown on UI but the information will be recorded into the log file. * **false** - If false, the conversion of query to report cube will not be performed automatically when opening the report in Page Report Studio. Instead, when you are to perform analytic reporting actions such as drilling on the report, a dialog will be displayed prompting you to do the conversion.   Data type: String |
|  | NoTempFile | Specifies whether or not to create temporary files.  * **true** - Not to create temporary files. Gains faster engine performance. * **false** - To create temporary files. Gains better accuracy in calculating data.   Data type: String |
|  | PageBackground | Specifies the background color of the report page. Data type: String |
|  | PrecisionSensitive | Specifies whether to enable specified precision settings in the report result when exporting the report to different formats. Data type: Boolean |
|  | ResultBufferSize | Specifies the number of report result pages which will be stored in the buffer. Data type: Integer |
|  | RowsPerSheet | Specifies the maximum number of rows for every worksheet when exporting the report to Excel. For the Excel version Excel 97-2003 Workbook (\*.xls), the value ranges from 0 to 65000. Any value out of the range will be considered as 65000. For the Excel version Excel Workbook (\*.xlsx), the value ranges from 0 to 1048000. Any value out of the range will be considered as 1048000.  Data type: Integer |
|  | SheetName | Specifies the sheet name for the report when exporting it to Excel. If the report is split into several sheets when exported to Excel because of limited rows per sheet, a postfix number will be added to the sheets starting from the second one (SheetName, SheetName1, SheetName2, SheetName3, ...). Data type: String  **Note:** The characters "|", ":", "/", "?", "\", "\*", "]", "[" cannot be displayed in the sheet name in Excel and the last character in the sheet name cannot be single quotation mark ('). If any one of them is used when you specify the property, it will be replaced by "\_" in Excel. |
|  | ShowSubHeaderFooter | Specifies whether or not to show the page header and footer panels of subreports in the report.  * **true** - The page header and page footer panels of subreports in the report will be displayed when the panels are set to be visible in the subreports. * **false** - The page header and page footer panels of subreports in the report will not be displayed.   Data type: String |
|  | StyleGroup | Specifies the style group for the report. If the report is to be used as a subreport, specify any style group to turn on the style group feature for the report and it will inherit the styles of the primary report; do not set this property or specify it as None to turn off the style group feature for the report and it will not inherit styles from the primary report.  Data type: String |
|  | StyleGroupOfDHTML | Pre-sets a style group for use when exporting the report to Page Report Result. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfExcel | Pre-sets a style group for use when exporting the report to Excel. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfFax | Pre-sets a style group for use when exporting the report to Fax. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfHTML | Pre-sets a style group for use when exporting the report to HTML. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfPDF | Pre-sets a style group for use when exporting the report to PDF. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfPS | Pre-sets a style group for use when exporting the report to PostScript. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfRST | Pre-sets a style group for use when exporting the report to Logi JReport Result or Applet. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfRTF | Pre-sets a style group for use when exporting the report to RTF. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfText | Pre-sets a style group for use when exporting the report to Text. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
|  | StyleGroupOfXML | Pre-sets a style group for use when exporting the report to XML. If you do not specify a value here, the [StyleGroup](#StyleGroup) property value will be applied. Data type: String |
| Banded Object | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | Background | Specifies the background color of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderJoint | Specifies the joint style for the border lines of the object.  * **miter** - Joins path segments by extending their outside edges until they meet. * **round** - Joins path segments by rounding off the corner at a radius of half the line width.   Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute [*id*](http://www.w3.org/TR/html401/struct/global.html#adef-id). This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. This property is read only. |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute [*lang*](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang). This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | RoundJointRadius | Specifies the radius for the border line joint of the object. This property takes effect only when [BorderJoint](#BorderJoint) is set to round. Data type: Integer |
|  | Style | The property can be used in two ways:  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressEmpty | Specifies whether to display the object in the report result when no record is returned to it. Data type: Boolean |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position9) property is set to static. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position9) property is set to static. Data type: Float |
| Banded Object Page Header | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | MergeToNextPanel | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RemoveBlankRow | Specifies whether to remove blank rows in the panel in the exported Excel file. Data type: Boolean |
|  | RepeatInDetailPanel | Specifies whether to make the objects in the panel repeated in the detail panel in the exported Excel file. Data type: Boolean |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Banded Object Page Footer | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalStyle | It is mapped to the HTML attribute *[style](http://www.w3.org/TR/html401/present/styles#adef-style)*. This attribute specifies style information for the object. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SuppressInLastPage | If true, the footer panel on the last page will not be displayed. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Banded Object Header | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | MergeToNextPanel | Specifies whether to merge the panel into the next panel in the exported Excel file. Data type: Boolean |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is applied only when the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Banded Object Footer | Background | Specifies the background color and fill effect of the object. Data type: String |
|  | BorderColor | Specifies the color of the border of the object. Data type: String |
|  | BorderWidth | Specifies the width of the border in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | CanCrossPage | Specifies whether the panel can be split across a page break. This property is applied only when the report has page layout enabled. The default is false which means that the panel is split only if it exceeds the page height. Data type: Boolean |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | FillWholePage | Specifies whether to make the panel extended to the bottom of the page, so that the next panel starts on a new page. Data type: Boolean |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | Label | Specifies the popup text displayed when the mouse pointer hovers over the left edge of the panel. Data type: String |
|  | Lang | It is mapped to the HTML attribute *[lang](http://www.w3.org/TR/html401/struct/dirlang.html#adef-lang)*. This attribute specifies the base language of the object's attribute values and text content. Data type: String |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | OnNewPage | Specifies whether the panel starts on a new page. This property is applied only when the report has page layout enabled. The default is false which means the panel starts on a new page only if the previous page is filled. Data type: Boolean |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | ShowBottomLine | Specifies whether to include a horizontal line at the bottom of the panel. Applies to panels in table components only. The default is false, which means that no horizontal line appears at the bottom of the panel. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SuppressBlankSection | Specifies whether a panel with no data is included in the report result. The default is false which means an empty panel is shown. Data type: Boolean |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | ToBottom | Specifies whether to move the banded object footer panel to the bottom of the page. The default is false, which means that the banded object footer appears at the end of the banded object. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Underlay | Specifies whether the panel will be layered beneath the next panel in the banded object. A panel layered beneath a subsequent panel can be used to contain a background picture or watermark. Banded page header, page footer, or group footer panels cannot be layered. The default is false which means that the panel is not layered beneath the next panel. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
| Chart Platform | Alt | Specifies the alternate text of the image, which will be shown when the image cannot be displayed. This property applies only when the chart is exported to HTML as an image chart. Data type: String |
|  | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. By default it is the value of the specified object. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AntiAliasing | Specifies whether to make the edges in a chart smooth. Data type: Boolean |
|  | Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
|  | CategoryEndOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. CategoryEndOffset specifies the ending offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
|  | CategoryFilter | Specifies the data format for the category axis (the X axis) to display the tick mark labels in the way you choose. Data type: String |
|  | CategoryStartOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. CategoryStartOffset specifies the starting offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ColumnNumber | Specifies the number of columns which will be the object's width in the exported Excel or CSV file. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | A representation of the standard HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalTitle | A representation of the standard HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | GroupValueFormat | Specifies the encoding format for values on the category axis. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HintFilter | Specifies the number format for the hint message. Data type: String |
|  | HintPercentFilter | Specifies the format for each hint percentage to the total. Data type: String |
|  | HyperLink | Specifies whether to add a hyperlink that refers to another report or a website to the chart. Data type: String |
|  | HyperLinkTarget | Specifies the target window or frame in which to display the content the [Hyperlink](#Hyperlink1) property specifies.  * **<Server Setting>**  Loads the linked file according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the linked file into a new window. The window is not named. * **Whole Window**  Loads the linked file into the full browser window. * **Same Frame**  Loads the linked file into the same frame as the link. * **Parent Frame**  Loads the linked file into the parent frame of the frame that contains the link. * **Other Frame**  Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.   Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | LogicColumn | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
|  | LongDesc | A representation of the standard HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MotionFilter | Specifies the data format for the motion field values displayed on the motion bar. Data type: String |
|  | PatternList | Specifies patterns of the data markers. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient. Data type: String |
|  | PlatformBackgroundBorderPenColor | Specifies the color of the platform border. Data type: String |
|  | PlatformBackgroundBorderPenEndCaps | Specifies the ending style of the platform border line. Data type: Enumeration |
|  | PlatformBackgroundBorderPenLineJoint | Specifies the joint style of the platform border line. Data type: Enumeration |
|  | PlatformBackgroundBorderPenLineJointRadius | Specifies the radius for the joint of the platform border line. The property takes effect only when [PlatformBackgroundBorderPenLineJoint](#BdrJoint1) is set to joint round. Data type: Float |
|  | PlatformBackgroundBorderPenOutlined | Specifies whether to show the platform border line in Outline Path. If the property is set to true, the platform border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
|  | PlatformBackgroundBorderPenStyle | Specifies the line style of the platform border. Data type: Enumeration |
|  | PlatformBackgroundBorderPenThickness | Specifies the width of the platform border, in inches or centimeters. Data type: Float |
|  | PlatformBackgroundBorderPenTransparency | Specifies the transparency of the platform border, in percent. Data type: Integer |
|  | PlatformBackgroundBorderPenVariabledDash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the Format Platform dialog will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the Format Platform dialog will take effect.   Data type: Boolean |
|  | PlatformBackgroundBorderStyle | Specifies the border type of the platform. Data type: Enumeration |
|  | PlatformBackgroundBottom | Specifies the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
|  | PlatformBackgroundFillPatternColor | Specifies the color of the platform background, applied when the property PlatformBackgroundFillPatternType is set to color. Data type: String |
|  | PlatformBackgroundFillPatternGradientEndColor | Specifies the color of the point where the gradient ends, applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: String |
|  | PlatformBackgroundFillPatternGradientEndX | Specifies the horizontal position where the gradient ends, measured in a percentage of the platform width. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientEndY | Specifies the vertical position where the gradient ends, measured in a percentage of the platform height. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientStartColor | Specifies the color of the point where the gradient begins, applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: String |
|  | PlatformBackgroundFillPatternGradientStartX | Specifies the horizontal position where the gradient begins, measured in a percentage of the platform width. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientStartY | Specifies the vertical position where the gradient begins, measured in a percentage of the platform height. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientStyle | Specifies the gradient style for the platform background, applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Enumeration |
|  | PlatformBackgroundFillPatternImageFile | Specifies the file name of the image, a portion of which will be displayed as the platform background. Applied when PlatformBackgroundFillPatternType is set to image. Enter the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
|  | PlatformBackgroundFillPatternImageHeight | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
|  | PlatformBackgroundFillPatternImageLayout | Specifies the layout style for the image that will be displayed as the platform background, applied when the property PlatformBackgroundFillPatternType is set to image. Data type: Enumeration |
|  | PlatformBackgroundFillPatternImageWidth | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
|  | PlatformBackgroundFillPatternImageX | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
|  | PlatformBackgroundFillPatternImageY | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
|  | PlatformBackgroundFillPatternTextureBackColor | Specifies the background color of the texture, applied when the property PlatformBackgroundFillPatternType is set to texture. Data type: String |
|  | PlatformBackgroundFillPatternTextureForeColor | Specifies the foreground color of the texture, applied when the property PlatformBackgroundFillPatternType is set to texture. Data type: String |
|  | PlatformBackgroundFillPatternTextureStyle | Specifies the texture style of the platform background, applied when the property PlatformBackgroundFillPatternType is set to texture. Data type: Enumeration |
|  | PlatformBackgroundFillPatternTransparency | Specifies the transparency of the platform background, in percent. Data type: Integer |
|  | PlatformBackgroundFillPatternType | Specifies the fill pattern for the platform background. Data type: Enumeration |
|  | PlatformBackgroundLeft | Specifies the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
|  | PlatformBackgroundRight | Specifies the right position of the background area, measured in a percentage of the chart width, from the right edge of the chart. Data type: Float |
|  | PlatformBackgroundTop | Specifies the top position of the background area, measured in a percentage of the chart height, from the top edge of the chart. Data type: Float |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | PrimaryDataFilter | Specifies the data format for the primary value axis (the Y1 axis) to display the tick mark labels in the way you choose. Data type: String |
|  | ReverseCategory | Specifies whether to reverse the sequence of the category field value. Data type: Boolean |
|  | ReverseSeries | Specifies whether to reverse the sequence of the series field value. Data type: Boolean |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | RowNumber | Specifies the number of rows which will be the object's height in the exported Excel or CSV file. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: String |
|  | SecondaryDataFilter | Specifies the data format for the secondary value axis (the Y2 axis) to display the tick mark labels in the way you choose. Data type: String |
|  | SeriesEndOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. SeriesEndOffset specifies the ending offset of the series.  Data type: Integer |
|  | SeriesFilter | Specifies the data format for the series axis (the Z axis) to display the tick mark labels in the way you choose. Data type: String |
|  | SeriesStartOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. SeriesStartOffset specifies the starting offset of the series.  Data type: Integer |
|  | SeriesValueEncoding | Specifies the encoding format for values on the series axis. Data type: String |
|  | ShowLegend | Specifies whether to make the legend visible in a chart. Data type: Boolean |
|  | SortCategory | Specifies the sorting order for the category field values. Data type: Enumeration |
|  | SortSeries | Specifies the sorting order for the series field values. Data type: Enumeration |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SwapGroup | Specifies to display values from different data fields by switching data between the category and series axes, the category and value axes of a chart. By default, this property is set to false, which means no switch will take place in the chart.  * **Switching between the category and series axes**  If you create a chart by adding fields to all of its axes, and set SwapGroup to true, data on the category and series axes will be switched. * **Switching between the category and value axes**  If you create a chart by adding one field to the category axis and several to the value axis, and set SwapGroup to true, data on the category and value axes will be switched.   Data type: Boolean  **Note:** If the chart has only one field on the category axis and one on the value axis, even though the property value is set to true, there will be no switch take place on the two axes. |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position10) property is set to static. Data type: Float |
|  | XHyperLink | Specifies whether to add a hyperlink that refers to another report or a website to the X axis labels. Data type: String |
|  | XHyperLinkTarget | Specifies the target window or frame in which to display the content the [XHyperlink](#XHyperlink1) property specifies.  * **<Server Setting>**  Loads the linked file according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the linked file into a new window. The window is not named. * **Whole Window**  Loads the linked file into the full browser window. * **Same Frame**  Loads the linked file into the same frame as the link. * **Parent Frame**  Loads the linked file into the parent frame of the frame that contains the link. * **Other Frame**  Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.   Data type: String |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property is ignored if the [position](#Position10) property is set to static. Data type: Float |
|  | ZHyperLink | Specifies whether to add a hyperlink that refers to another report or a website to the Z axis labels. Data type: String |
|  | ZHyperLinkTarget | Specifies the target window or frame in which to display the content the [ZHyperlink](#ZHyperlink1) property specifies.  * **<Server Setting>**  Loads the linked file according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the linked file into a new window. The window is not named. * **Whole Window**  Loads the linked file into the full browser window. * **Same Frame**  Loads the linked file into the same frame as the link. * **Parent Frame**  Loads the linked file into the parent frame of the frame that contains the link. * **Other Frame**  Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.   Data type: String |
| Chart Paper | Background | Specifies the properties of the chart paper background. |
|  | BorderColor | Specifies the color of the paper border. Data type: String |
|  | BorderWidth | Specifies the width of the paper border, in inches or centimeters. Data type: Float |
|  | BottomLine | Specifies the line style of the bottom border of the object. Data type: Enumeration |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | LeftLine | Specifies the line style of the left border of the object. Data type: Enumeration |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. The X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: String  **Note:** This property only affects objects with a parent container that is the report body, a tabular cell, or a text box. |
|  | RecordLocation | Specifies the calculation point for the properties which use formulas.  * **Default** - The values of the properties are calculated in the default location where they are located. * **Page Header** - The values of the properties are calculated in the page header. * **Page Footer** - The values of the properties are calculated in the page footer.   Data type: String |
|  | RightLine | Specifies the line style of the right border of the object. Data type: Enumeration |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | TopLine | Specifies the line style of the top border of the object. Data type: Enumeration |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property takes effect only when the [Placement](#Placement) property for the chart legend is set to auto. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property takes effect only when the [Placement](#Placement) property for the chart legend is set to auto. Data type: Float |
| Chart legend | AutoSize | Specifies whether to resize the legend automatically. Data type: Boolean |
|  | BottomMargin | Specifies the distance in inches or centimeters between the legend labels and the bottom border of the legend. Data type: Float |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | IconAlignment | Specifies the relative position of the icon to the legend. Data type: Enumeration |
|  | IconBorderPenColor | Specifies the color of the icon borders. Data type: String |
|  | IconBorderPenEndCaps | Specifies the ending style of the icon border line. Data type: Enumeration |
|  | IconBorderPenLineJoint | Specifies the joint style of the icon border line. Data type: Enumeration |
|  | IconBorderPenOutlined | Specifies whether to show the icon border line in Outline Path. If the property is set to true, the icon border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
|  | IconBorderPenStyle | Specifies the line style of the icon borders. Data type: Enumeration |
|  | IconBorderPenThickness | Specifies the width of the icon borders in inches or centimeters. Data type: Float |
|  | IconBorderPenTransparency | Specifies the transparency of the icon borders, in percent. Data type: Integer |
|  | IconBorderPenVariabledDash | Specifies whether to resize the dash automatically. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
|  | IconHeight | Specifies the height of the icon, in inches or centimeters. Data type: Float |
|  | IconTextGap | Specifies the distance between each legend label and icon. Data type: Float |
|  | IconWidth | Specifies the width of the icon, in inches or centimeters. Data type: Float |
|  | LabelFilterSource | Specifies the data format option for the chart legend labels.  * **Axis Data Format** - The data format of the legend labels will follow that of the axis data: if the chart has series axis, the legend label format will be the same as the series axis data format; if not, the category axis data format will be used to the legend labels. * **Legend Data Format** - The data format of the legend labels will be controlled by the property [LegendFilter](#LegendDataFormat).   Data type: Enumeration |
|  | LabelHSpacing | Specifies the horizontal distance between two adjacent legend labels. Data type: Float |
|  | LabelTextFontName | Specifies the font face for the legend labels. Data type: Enumeration |
|  | LabelTextFontSize | Specifies the font size for the legend labels. Data type: Integer |
|  | LabelTextFontStyle | Specifies the font style for the legend labels. Data type: Enumeration |
|  | LabelTextPenStyle | Specifies the style for the label text outline. Data type: Enumeration |
|  | LabelTextPatternColor | Specifies the color of the label, applied when the property LabelTextPatternType is set to color. Data type: String |
|  | LabelTextPatternGradientEndColor | Specifies the color of the point where the gradient ends, applied when the property LabelTextPatternType is set to gradient. Data type: String |
|  | LabelTextPatternGradientEndX | Specifies the horizontal position where the gradient ends, measured in a percentage of the label text width. Applied when the property LabelTextPatternType is set to gradient. Data type: Integer |
|  | LabelTextPatternGradientEndY | Specifies the vertical position where the gradient ends, measured in a percentage of the label text height. Applied when the property LabelTextPatternType is set to gradient. Data type: Integer |
|  | LabelTextPatternGradientStartColor | Specifies the color of the point where the gradient begins, applied when the property LabelTextPatternType is set to gradient. Data type: String |
|  | LabelTextPatternGradientStartX | Specifies the horizontal position where the gradient begins, measured in a percentage of the label text width. Applied when the property LabelTextPatternType is set to gradient. Data type: Integer |
|  | LabelTextPatternGradientStartY | Specifies the vertical position where the gradient begins, measured in a percentage of the label text height. Applied when the property LabelTextPatternType is set to gradient. Data type: Integer |
|  | LabelTextPatternGradientStyle | Specifies the gradient style for the label, applied when the property LabelTextPatternType is set to gradient. The image fill type does not apply to the legend label. Data type: Enumeration |
|  | LabelTextPatternTextureBackColor | Specifies the background color of the texture, applied when the property LabelTextPatternType is set to texture. Data type: String |
|  | LabelTextPatternTextureForeColor | Specifies the foreground color of the texture, applied when the property LabelTextPatternType is set to texture. Data type: String |
|  | LabelTextPatternTextureStyle | Specifies the texture style for the label, applied when the property LabelTextPatternType is set to texture. Data type: Enumeration |
|  | LabelTextPatternTransparency | Specifies the transparency of the background, in percent. Data type: Integer |
|  | LabelTextPatternType | Specifies the fill pattern for the label. Data type: Enumeration |
|  | LabelTextPenColor | Specifies the color for the label text outline. Data type: String |
|  | LabelTextPenEndCaps | Specifies the ending style for the label text outline. Data type: Enumeration |
|  | LabelTextPenLineJoint | Specifies the joint style for the label text outline. Data type: Enumeration |
|  | LabelTextPenOutlined | Specifies whether to show the label text outline in outline form. If the property is set to true, the outline will be shown in outline form; otherwise, in whole form. Data type: Boolean |
|  | LabelTextPenThickness | Specifies the thickness for the label text outline. Data type: Float |
|  | LabelTextPenTransparency | Specifies the transparency for the label text outline, in percent. Data type: Integer |
|  | LabelTextPenVariabledDash | Specifies whether to resize the dash automatically. If the property is set to true, the dash size will be adjusted automatically; otherwise, the dash size will be of fixed size. Data type: Boolean |
|  | LabelTextRotation | Specifies the rotation angle of each legend label around its center, in degrees. The default value is 0. Data type: Float |
|  | LabelTextShearing | Specifies the shearing transformation of each legend label around its center. The default value is 0. Data type: Float |
|  | LabelTextSpecialEffect1 | Specifies the special effect for the label text. Data type: Enumeration |
|  | LabelTextSpecialEffect2 | Specifies whether the label text will in superscript or subscript form, or neither of them. Data type: Enumeration |
|  | LabelTextStrikethrough | Specifies the style of the line by which the label texts are struck through. Data type: Enumeration |
|  | LabelTextUnderline | Specifies the underline style for the legend labels. Data type: Enumeration |
|  | LabelTextWordWrap | Specifies whether to enable the word wrap function for the label text, not applying to radar charts, bubble charts, scatter charts and gauge charts. If the text contains special characters (such as ",", "." and space), it will be broken at the position of one of the special characters. Data type: Boolean |
|  | LabelVSpacing | Specifies the vertical distance between two adjacent legend labels. Data type: Float |
|  | LeftMargin | Specifies the distance in inches or centimeters between the legend labels and the left border of the legend. Data type: Float |
|  | LegendBackgroundBorderPenColor | Specifies the color of the legend border. Data type: String |
|  | LegendBackgroundBorderPenEndCaps | Specifies the ending style of the legend border line. Data type: Enumeration |
|  | LegendBackgroundBorderPenLineJoint | Specifies the joint style of the legend border line. Data type: Enumeration |
|  | LegendBackgroundBorderPenOutlined | Specifies whether to show the legend border line in Outline Path. If the property is set to true, the legend border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
|  | LegendBackgroundBorderPenStyle | Specifies the line style of the legend border. Data type: Enumeration |
|  | LegendBackgroundBorderPenThickness | Specifies the width of the legend border, in inches or centimeters. Data type: Float |
|  | LegendBackgroundBorderPenTransparency | Specifies the transparency of the legend border, in percent. Data type: Integer |
|  | LegendBackgroundBorderPenVariabledDash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the Format Legend dialog will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the Format Legend dialog will take effect.   Data type: Boolean |
|  | LegendBackgroundBorderStyle | Specifies the border type of the legend. Data type: Enumeration |
|  | LegendBackgroundBottom | Specifies the bottom position of the background area, measured in a percentage of the legend height, from the bottom edge of the legend. Data type: Float |
|  | LegendBackgroundFillPatternColor | Specifies the color of the legend background, applied when the property LegendBackgroundFillPatternType is set to color. Data type: String |
|  | LegendBackgroundFillPatternGradientEndColor | Specifies the color of the point where the gradient ends, applied when the property LegendBackgroundFillPatternType is set to gradient. Data type: String |
|  | LegendBackgroundFillPatternGradientEndX | Specifies the horizontal position where the gradient ends, measured in a percentage of the legend width. Applied when the property LegendBackgroundFillPatternTypee is set to gradient. Data type: Integer |
|  | LegendBackgroundFillPatternGradientEndY | Specifies the vertical position where the gradient ends, measured in a percentage of the legend height. Applied when the property LegendBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | LegendBackgroundFillPatternGradientStartColor | Specifies the color of the point where the gradient begins, applied when the property LegendBackgroundFillPatternType is set to gradient. Data type: String |
|  | LegendBackgroundFillPatternGradientStartX | Specifies the horizontal position where the gradient begins, measured in a percentage of the legend width. Applied when the property LegendBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | LegendBackgroundFillPatternGradientStartY | Specifies the vertical position where the gradient begins, measured in a percentage of the legend height. Applied when the property LegendBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | LegendBackgroundFillPatternGradientStyle | Specifies the gradient style for the legend background, applied when the property LegendBackgroundFillPatternType is set to gradient. Data type: Enumeration |
|  | LegendBackgroundFillPatternImageFile | Specifies the file name of the image, a portion of which will be displayed as the legend background. Applied when the property LegendBackgroundFillPatternType is set to image. Enter the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
|  | LegendBackgroundFillPatternImageHeight | The four properties, LegendBackgroundFillPatternImageX, LegendBackgroundFillPatternImageY, LegendBackgroundFillPatternImageWidth, and LegendBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property LegendBackgroundFillPatternType is set to image. LegendBackgroundFillPatternImageHeight specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
|  | LegendBackgroundFillPatternImageLayout | Specifies the layout style for the image that will be displayed as the legend background, applied when the property LegendBackgroundFillPatternType is set to image. Data type: Enumeration |
|  | LegendBackgroundFillPatternImageWidth | The four properties, LegendBackgroundFillPatternImageX, LegendBackgroundFillPatternImageY, LegendBackgroundFillPatternImageWidth, and LegendBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property LegendBackgroundFillPatternType is set to image. LegendBackgroundFillPatternImageWidth specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
|  | LegendBackgroundFillPatternImageX | The four properties, LegendBackgroundFillPatternImageX, LegendBackgroundFillPatternImageY, LegendBackgroundFillPatternImageWidth, and LegendBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property LegendBackgroundFillPatternType is set to image. LegendBackgroundFillPatternImageX specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
|  | LegendBackgroundFillPatternImageY | The four properties, LegendBackgroundFillPatternImageX, LegendBackgroundFillPatternImageY, LegendBackgroundFillPatternImageWidth, and LegendBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the legend background. They take effect when the property Fill Type is set to image. LegendBackgroundFillPatternImageY specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
|  | LegendBackgroundFillPatternTextureBackColor | Specifies the background color of the texture, applied when the property LegendBackgroundFillPatternType is set to texture. Data type: String |
|  | LegendBackgroundFillPatternTextureForeColor | Specifies the foreground color of the texture, applied when the property LegendBackgroundFillPatternType is set to texture. Data type: String |
|  | LegendBackgroundFillPatternTextureStyle | Specifies the texture style of the legend background, applied when the property LegendBackgroundFillPatternType is set to texture. Data type: Enumeration |
|  | LegendBackgroundFillPatternTransparency | Specifies the transparency of the legend background, in percent. Data type: Integer |
|  | LegendBackgroundFillPatternType | Specifies the fill pattern for the legend background. Data type: Enumeration |
|  | LegendBackgroundLeft | Specifies the left position of the background area, measured in a percentage of the legend width, from the left edge of the legend. Data type: Float |
|  | LegendBackgroundRight | Specifies the right position of the background area, measured in a percentage of the legend width, from the right edge of the legend. Data type: Float |
|  | LegendBackgroundTop | Specifies the top position of the background area, measured in a percentage of the legend height, from the top edge of the legend. Data type: Float |
|  | LegendFilter | Specifies the data format of the legend labels, applied when [LabelFilterSource](#LabelFormatSource) is set to Legend Data Format. Data type: String |
|  | PercentFormat | Specifies the format of the percentage values on the legend. Applied when ShowPercent is set to true. Data type: String |
|  | Placement | Specifies the position of the legend in the platform. Data type: Enumeration |
|  | ReverseLabels | Specifies whether to reverse the order of the labels in the legend object. Data type: Boolean |
|  | RightMargin | Specifies the distance in inches or centimeters between the legend labels and the right border of the legend. Data type: Float |
|  | ShowPercent | Specifies whether to show the percentage of each entry value to the total on the legend. Applies to pie, bar and bench charts that have only one value axis. Data type: Boolean |
|  | ShowScrollbar | Specifies whether to show a scrollbar on the legend to fully view the legend content when the content does not fit into the legend. Data type: Boolean |
|  | ShowTips | Specifies whether to show the corresponding data information when the mouse pointer points at a target in the chart legend in Designer view mode, in HTML result, in Page Report Studio, or in Web Report Studio or JDashboard. Data type: Boolean |
|  | ShowValues | Specifies whether to show the values for the legend entries. Applies to pie, bar and bench charts that have only one value axis. Data type: Boolean |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object, or type in the style name. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | SubPlacement | Specifies the position of the legend further based on the setting of the property Placement. Data type: Enumeration |
|  | TopMargin | Specifies the distance in inches or centimeters between the legend labels and the top border of the legend. Data type: Float |
|  | TotalValueText | Specifies the text of the total value label on the legend. Applies to pie, bar and bench charts that have only one value axis. Data type: String |
|  | Truncate | Specifies whether to truncate the legend entry label text when the text overflow the labels. Data type: Boolean |
|  | ValueFormat | Specifies the number format of the legend entry values. Applied when ShowValues is set to true. Data type: String |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. This property takes effect only when the [Placement](#Placement) property is set to auto. Data type: Float |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. This property takes effect only when the [Placement](#Placement) property is set to auto. Data type: Float |
| Chart Label | Alt | Specifies the alternate text of the image, which will be shown when the image cannot be displayed. This property applies only when the chart is exported to HTML as an image chart. Data type: String |
|  | AnchorDispValue | Specifies a string or formula to display for the TOC entry for this object in the TOC Browser. The TOCAnchor property must be set to true for this property to take effect. Data type: String |
|  | AntiAliasing | Specifies whether to make the edges in a chart smooth. Data type: Boolean |
|  | Cache | Specifies whether to cache the dataset for this object in the data buffer so other objects which use the same dataset can share the data rather than perform their own SQL query. Data type: Boolean |
|  | CategoryEndOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. CategoryEndOffset specifies the ending offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
|  | CategoryFilter | Specifies the data format for the category axis (the X axis) to display the tick mark labels in the way you choose. Data type: String |
|  | CategoryStartOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. CategoryStartOffset specifies the starting offset of the categories. It does not apply to the charts which involve only one group.  Data type: Integer |
|  | class | Specifies a CSS class to be applied to the object which is a valid class in the CSS file. Data type: String |
|  | ColumnIndex | Specifies the X coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | ColumnNumber | Specifies the number of columns which will be the object's width in the exported Excel or CSV file. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: String |
|  | ExportToCSV | Specifies whether to include the object when exporting the report to CSV. Data type: Boolean |
|  | ExportToDHTML | Specifies whether to include the object when exporting the report to Page Report Result. Data type: Boolean |
|  | ExportToXLS | Specifies whether to include the object when exporting the report to Excel. Data type: Boolean |
|  | ExternalCSSClassValue | Specifies a class selector to be applied to the object when exported as HTML. Data type: String |
|  | ExternalID | It is mapped to the HTML attribute *[id](http://www.w3.org/TR/html401/struct/global.html#adef-id)*. This attribute specifies a name to the object, which must be unique in the report. Data type: String |
|  | ExternalTitle | It is mapped to the HTML attribute *[title](http://www.w3.org/TR/html401/struct/global.html#adef-title)*. This attribute offers advisory information about the object. Data type: String |
|  | GotoDetail | Specifies whether to show the detailed information when you select the object in Page Report Studio. This property is available only when the object is in the group header/footer panel of a banded object. Data type: Boolean |
|  | GroupValueFormat | Specifies the encoding format for values on the category axis. Data type: String |
|  | Height | Specifies the height of the object, in inches or centimeters. Data type: Float |
|  | HintFilter | Specifies the number format for the hint message. Data type: String |
|  | HintPercentFilter | Specifies the format for each hint percentage to the total. Data type: String |
|  | HyperLink | Specifies whether to add a hyperlink that refers to another report or a website to the chart. Data type: String |
|  | HyperLinkTarget | Specifies the target window or frame in which to display the content the [Hyperlink](#Hyperlink2) property specifies.  * **<Server Setting>**  Loads the linked file according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the linked file into a new window. The window is not named. * **Whole Window**  Loads the linked file into the full browser window. * **Same Frame**  Loads the linked file into the same frame as the link. * **Parent Frame**  Loads the linked file into the parent frame of the frame that contains the link. * **Other Frame**  Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.   Data type: String |
|  | Invisible | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will still be performed if the property is set to true. Data type: Boolean |
|  | LogicColumn | Specifies whether to show the object in the next visible table cell in the same row when the column which holds the object is hidden. Data type: Enumeration  **Notes:**   * The next visible table cell should be completely empty, that is, the cell should not hold any content including blank space. * When the property for several objects in the same row is set to next visible column, and the columns holding these objects are all hidden, then only the object in the rightmost column will be shown in the next visible cell. |
|  | LongDesc | A representation of the standard HTML attribute *[longdesc](http://www.w3.org/TR/html401/struct/objects.html#adef-longdesc-IMG)*. This attribute specifies a link to a long description of the object. Data type: String |
|  | MotionFilter | Specifies the data format for the motion field values displayed on the motion bar. Data type: String |
|  | PatternList | Specifies patterns of the data markers. The patterns can be one or more of the following: Automatic, Color, Texture, and Gradient. Data type: String |
|  | PlatformBackgroundBorderPenColor | Specifies the color of the platform border. Data type: String |
|  | PlatformBackgroundBorderPenEndCaps | Specifies the ending style of the platform border line. Data type: Enumeration |
|  | PlatformBackgroundBorderPenLineJoint | Specifies the joint style of the platform border line. Data type: Enumeration |
|  | PlatformBackgroundBorderPenLineJointRadius | Specifies the radius for the joint of the platform border line. The property takes effect only when [PlatformBackgroundBorderPenLineJoint](#BdrJoint2) is set to joint round. Data type: Float |
|  | PlatformBackgroundBorderPenOutlined | Specifies whether to show the platform border line in Outline Path. If the property is set to true, the platform border line will be shown in Outline Path; otherwise, in Fill Path. Data type: Boolean |
|  | PlatformBackgroundBorderPenStyle | Specifies the line style of the platform border. Data type: Enumeration |
|  | PlatformBackgroundBorderPenThickness | Specifies the width of the platform border, in inches or centimeters. Data type: Float |
|  | PlatformBackgroundBorderPenTransparency | Specifies the transparency of the platform border, in percent. Data type: Integer |
|  | PlatformBackgroundBorderPenVariabledDash | Specifies whether to resize the dash automatically.  * **true** - If selected, the dash size will be adjusted automatically, and the option Auto Adjust Dash in the Format Platform dialog will take effect. * **false** - If selected, the dash size will be of fixed size, and the option Fixed Dash Size in the Format Platform dialog will take effect.   Data type: Boolean |
|  | PlatformBackgroundBorderStyle | Specifies the border type of the platform. Data type: Enumeration |
|  | PlatformBackgroundBottom | Specifies the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
|  | PlatformBackgroundFillPatternColor | Specifies the color of the platform background, applied when the property PlatformBackgroundFillPatternType is set to color. Data type: String |
|  | PlatformBackgroundFillPatternGradientEndColor | Specifies the color of the point where the gradient ends, applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: String |
|  | PlatformBackgroundFillPatternGradientEndX | Specifies the horizontal position where the gradient ends, measured in a percentage of the platform width. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientEndY | Specifies the vertical position where the gradient ends, measured in a percentage of the platform height. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientStartColor | Specifies the color of the point where the gradient begins, applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: String |
|  | PlatformBackgroundFillPatternGradientStartX | Specifies the horizontal position where the gradient begins, measured in a percentage of the platform width. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientStartY | Specifies the vertical position where the gradient begins, measured in a percentage of the platform height. Applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Integer |
|  | PlatformBackgroundFillPatternGradientStyle | Specifies the gradient style for the platform background, applied when the property PlatformBackgroundFillPatternType is set to gradient. Data type: Enumeration |
|  | PlatformBackgroundFillPatternImageFile | Specifies the file name of the image, a portion of which will be displayed as the platform background. Applied when PlatformBackgroundFillPatternType is set to image. Enter the file name with suffix in the value cell. If the image is outside of the current catalog, you should include the full path of the image correctly. Data type: String |
|  | PlatformBackgroundFillPatternImageHeight | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image Height specifies the height of the image portion, measured in a percentage of the image height.  Data type: Integer |
|  | PlatformBackgroundFillPatternImageLayout | Specifies the layout style for the image that will be displayed as the platform background, applied when the property PlatformBackgroundFillPatternType is set to image. Data type: Enumeration |
|  | PlatformBackgroundFillPatternImageWidth | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image Width specifies the width of the image portion, measured in a percentage of the image width.  Data type: Integer |
|  | PlatformBackgroundFillPatternImageX | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image X specifies the distance between the left border of image and the portion that will contain the pattern, measured in a percentage of the image width.  Data type: Integer |
|  | PlatformBackgroundFillPatternImageY | The four properties, PlatformBackgroundFillPatternImageX, PlatformBackgroundFillPatternImageY, PlatformBackgroundFillPatternImageWidth, and PlatformBackgroundFillPatternImageHeight, together are used to define a portion of the image (the portion is a rectangle), which will be displayed as the platform background. They take effect when the property PlatformBackgroundFillPatternType is set to image. Image Y specifies the distance between the top border of image and the portion that will contain the pattern, measured in a percentage of the image height.  Data type: Integer |
|  | PlatformBackgroundFillPatternTextureBackColor | Specifies the background color of the texture, applied when the property PlatformBackgroundFillPatternType is set to texture. Data type: String |
|  | PlatformBackgroundFillPatternTextureForeColor | Specifies the foreground color of the texture, applied when the property PlatformBackgroundFillPatternType is set to texture. Data type: String |
|  | PlatformBackgroundFillPatternTextureStyle | Specifies the texture style of the platform background, applied when the property PlatformBackgroundFillPatternType is set to texture. Data type: Enumeration |
|  | PlatformBackgroundFillPatternTransparency | Specifies the transparency of the platform background, in percent. Data type: Integer |
|  | PlatformBackgroundFillPatternType | Specifies the fill pattern for the platform background. Data type: Enumeration |
|  | PlatformBackgroundLeft | Specifies the left position of the background area, measured in a percentage of the chart width, from the left edge of the chart. Data type: Float |
|  | PlatformBackgroundRight | Specifies the right position of the background area, measured in a percentage of the chart width, from the right edge of the chart. Data type: Float |
|  | PlatformBackgroundTop | Specifies the top position of the background area, measured in a percentage of the chart height, from the top edge of the chart. Data type: Float |
|  | position | Specifies the position of the object.  * **static** - The object is positioned at the location in which it is inserted. If selected, the X, Y and other position-related properties will be hidden or disabled. The position of the object is affected by preceding objects in the same container. * **absolute** - The object will be located at the position specified by dragging and dropping or by setting its X and Y property values. The position of the object is not affected by preceding objects in the same container.   Data type: Enumeration  **Note:** This property only affects objects with a parent container that is the report body, a table cell, a tabular cell, or a text box. |
|  | PrimaryDataFilter | Specifies the data format for the primary value axis (the Y1 axis) to display the tick mark labels in the way you choose. Data type: String |
|  | ReverseCategory | Specifies whether to reverse the sequence of the category field value. Data type: Boolean |
|  | ReverseSeries | Specifies whether to reverse the sequence of the series field value. Data type: Boolean |
|  | RowIndex | Specifies the Y coordinate of the object relative to its parent container when exported to Excel or CSV, measured in cells. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: Integer |
|  | RowNumber | Specifies the number of rows which will be the object's height in the exported Excel or CSV file. The [Columned](#Column) property at the report tab level must be set to true for this property to take effect. Data type: String |
|  | SecondaryDataFilter | Specifies the data format for the secondary value axis (the Y2 axis) to display the tick mark labels in the way you choose. Data type: String |
|  | SeriesEndOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. SeriesEndOffset specifies the ending offset of the series.  Data type: Integer |
|  | SeriesFilter | Specifies the data format for the series axis (the Z axis) to display the tick mark labels in the way you choose. Data type: String |
|  | SeriesStartOffset | The four properties work together to control the range of the data being displayed on a chart: CategoryStartOffset, CategoryEndOffset, SeriesStartOffset, and SeriesEndOffset. SeriesStartOffset specifies the starting offset of the series.  Data type: Integer |
|  | SeriesValueEncoding | Specifies the encoding format for values on the series axis. Data type: String |
|  | ShowLegend | Specifies whether to make the legend visible in a chart. Data type: Boolean |
|  | SortCategory | Specifies the sorting order for the category field values. Data type: Enumeration |
|  | SortSeries | Specifies the sorting order for the series field values. Data type: Enumeration |
|  | Style | The property can be used in two ways.  * Specifies a style to be applied to the object. This works when a StyleGroup has been specified at the report sheet level and when there are styles in the StyleGroup that can be applied to the object. * Specifies a CSS selector to be applied to the object.   Data type: String |
|  | Suppressed | Specifies whether to show the object in the design area and in the report result. All formulas and calculations will be skipped if the property is set to true. Data type: Boolean  **Note:** When both the Invisible and Suppressed properties of an object are set to true, Suppressed has the higher priority. |
|  | SuppressedIfNoRecords | Specifies whether to display the object in the report result when no record is returned to its parent data component. Data type: Boolean |
|  | SwapGroup | Specifies to display values from different data fields by switching data between the category and series axes, the category and value axes of a chart. By default, this property is set to false, which means no switch will take place in the chart.  * **Switching between the category and series axes**  If you create a chart by adding fields to all of its axes, and set SwapGroup to true, data on the category and series axes will be switched. * **Switching between the category and value axes**  If you create a chart by adding one field to the category axis and several to the value axis, and set SwapGroup to true, data on the category and value axes will be switched.   Data type: Boolean  **Note:** If the chart has only one field on the category axis and one on the value axis, even though the property value is set to true, there will be no switch take place on the two axes. |
|  | TOCAnchor | Specifies whether to include the object in the TOC Browser for the report. Data type: Boolean |
|  | Width | Specifies the width of the object, in inches or centimeters. Data type: Float |
|  | X | Specifies the horizontal coordinate of the top left corner of the object, relative to its parent container. Data type: Float |
|  | XHyperLink | Specifies whether to add a hyperlink that refers to another report or a website to the X axis labels. Data type: String |
|  | XHyperLinkTarget | Specifies the target window or frame in which to display the content the [XHyperlink](#XHyperlink2) property specifies.  * **<Server Setting>**  Loads the linked file according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the linked file into a new window. The window is not named. * **Whole Window**  Loads the linked file into the full browser window. * **Same Frame**  Loads the linked file into the same frame as the link. * **Parent Frame**  Loads the linked file into the parent frame of the frame that contains the link. * **Other Frame**  Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.   Data type: String |
|  | Y | Specifies the vertical coordinate of the top left corner of the object, relative to its parent container. Data type: Float |
|  | ZHyperLink | Specifies whether to add a hyperlink that refers to another report or a website to the Z axis labels. Data type: String |
|  | ZHyperLinkTarget | Specifies the target window or frame in which to display the content the [ZHyperlink](#ZHyperlink2) property specifies. If the specified frame name does not exist, the linked document will be loaded into a new window.  * **<Server Setting>**  Loads the linked file according to setting of the Pop Up New Window for Links option in the Customize Profile panel of the Profile dialog in Logi JReport Server. * **New Window**  Loads the linked file into a new window. The window is not named. * **Whole Window**  Loads the linked file into the full browser window. * **Same Frame**  Loads the linked file into the same frame as the link. * **Parent Frame**  Loads the linked file into the parent frame of the frame that contains the link. * **Other Frame**  Loads the linked file into some other specified frame. If the frame name does not exist, the linked file will be loaded into a new window.   Data type: String |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562442-Inserting-Moving-and-Deleting-an-Object)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582841-Getting-Report-Metadata-Information)
