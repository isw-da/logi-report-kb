---
title: "Export Dialog Box Properties"
id: 1500009772181
section: "Page Report Studio Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009772181-Export-Dialog-Box-Properties
updated_at: 2021-07-24T00:49:16Z
---

# Export Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744282-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744582-Fetch-Data-Dialog-Box-Properties)

# Export Dialog Box Properties

You can use the Export dialog box to set settings for [exporting the report result](https://devnet.logianalytics.com/hc/en-us/articles/1500009777541-Exporting-Printing-Page-Report-Result) to different formats. This topic describes the options in the dialog box.

![Export dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885396631/expt.gif)

**File Name**

Specifies the name of the result file.

**View Report Result**

If selected, the result will be directly opened in the web browser if the format is supported by a plug-in of the web browser; otherwise you will be prompted to save the result file.

**Save to File System**

If selected, the web browser will prompt you to save the result file to a specified folder.

**Save to Version System**

If selected, the report result will be saved as a result version in Logi Report Server's [versioning system](https://devnet.logianalytics.com/hc/en-us/articles/1500009777341-Managing-Resource-Versions).

**Select Report Tabs**

Specifies the report tabs which you want to export. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**

Moves the specified report tab higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**

Moves the specified report tab lower in the list.

**Select Format**

Specifies the format to which the report result will be exported.

**More/Less Options**

Shows/Hides the additional settings for exporting the report to the specified format.

* **Style Group**  
   If a style group has been specified via the [Override Style Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Style) option in the server profile, the specified style group will be selected in the drop-down list by default. You can also choose another style group from the drop-down list to apply to the exported result. If the page report is created in Logi Report Designer, when the <No Style> item is specified, the style group property predefined for specific export format in Logi Report Designer will be applied to export the report result to that format.
* **Properties**  
   Specifies the properties for the selected format:
  + [PDF](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#PDF)
  + [HTML](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#HTML)
  + [Excel](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#Excel)
  + [Text](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#Text)
  + [RTF](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#RTF)
  + [XML](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#XML)
  + [PostScript](https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties#PS)
  + **Page Report Result**
    - **Zip Result**  
       Specifies to compress the result and its size would be smaller.

**OK**

Exports the report with the settings you specified. If you have selected multiple report tabs to export at one time and some of them have not been specified with parameters, the [Enter Parameter Values](https://devnet.logianalytics.com/hc/en-us/articles/1500009746022-Enter-Parameter-Values-Dialog-Box-Properties) dialog box will pop up for you to specify their parameter values.

**Cancel**

Cancels the operation and closes this dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744282-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744582-Fetch-Data-Dialog-Box-Properties)
