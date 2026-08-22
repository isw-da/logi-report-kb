---
title: "Report Tab Properties"
id: 1500009746221
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009746221-Report-Tab-Properties
updated_at: 2021-07-25T07:19:56Z
---

# Report Tab Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746201-Report-Body-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746441-Save-As)

# Report Tab Properties

The Report Tab Properties dialog box is used to set the properties of a report tab.

There are the following tabs in this dialog box: [General](#General) and [Others](#Others).

**OK**

Applies the settings and closes this dialog box.

**Cancel**

Discards the settings and closes this dialog box.

**Help**

Displays the help document about this feature.

## General

This tab shows some general information of the report tab.

![Report Tab Properties dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404936909975/rptprpty_gnrl.gif)

**Name**

Specifies the report tab name.

**Show NLS Value**

Select this option to show the translated name for the display name of the object in the Name text box if you have enabled the NLS feature and translated it.

If selected, this option takes effect only when the display name of the object is not modified.

**Records per Page**

Specifies the number of records in each page for the data buffer.

**Page Background**

Specifies the page background color.

**Max Page Number**

Specifies the maximum number of pages in the data buffer.

**Result Buffer Size**

Specifies the size of the result buffer for storing the report result.

**Embedded Fonts**

Specifies the True Type Fonts that have been used in the report tab. This property is only for exporting PDF files.

**Compress If No Record**

If this option is set to true and there is no record retrieved to the report tab, the report page will be compressed.

**Parameter List Auto**

If true, values defined in the catalog will be used as the default parameter values; otherwise, Logi Report will get the default values from a specified class file. For more information, refer to Importing Parameter Values in the *Logi Report Designer Guide*.

## Others

This tab shows some miscellaneous information of the report tab.

![Report Tab Properties dialog - Others tab](https://devnet.logianalytics.com/hc/article_attachments/4404942582679/rptprpty_other.gif)

**National Language Support**

Specifies a language profile file.

**Compress Result**

Specifies whether or not to compress the exported RST file.

**Excel Buffer Size**

Specifies the size of the Excel buffer to store the XLS format report result.

**Fast Pass**

If true, the performance of the engine when saving the report result to a CSV format file on Logi Report Server will be improved.

**Rows per Sheet**

Specifies the maximal number of rows for every worksheet when exporting the result to an XLS file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009746201-Report-Body-Properties)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746441-Save-As)
