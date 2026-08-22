---
title: "Export Dialog Box Properties"
id: 4405683627671
section: "Dialog Boxes in Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683627671-Export-Dialog-Box-Properties
updated_at: 2022-01-27T07:58:39Z
---

# Export Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683626647-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690507927-Fetch-Data-Dialog-Box-Properties)

# Export Dialog Box Properties

You can use the Export dialog box to set settings for [exporting reports](https://devnet.logianalytics.com/hc/en-us/articles/4405683955223-Exporting-Printing-Page-Report-Result) to different formats. This topic describes the properties in the dialog box.

![Export dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420461565975/expt.gif)

**File Name**

Specify the name of the output file.

**View Report Result**

Select if you want to directly open the report in the web browser that supports the format.

**Save to File System**

Select if you want the web browser to prompt you to save the output file to a specified folder.

**Save to Version System**

Select if you want to save the report as a version in Logi Report Server's [versioning system](https://devnet.logianalytics.com/hc/en-us/articles/4405683938455-Managing-Resource-Versions).

**Select Report Tabs**

Select the report tabs you want to export, in the order as listed. If the report has only one report tab, Server select it by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4420461479831/btn_mvup.gif)**Move Up button**

Select to move the selected item higher in the list.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4420453416727/btn_mvdown.gif)**Move Down button**

Select to move the selected item lower in the list.

**Select Format**

Select the format in which you want to export the report.

**More/Less Options**

Select to show/hide the additional properties for exporting the report to the specified format.

* **Style Group**  
   If you have specified a style group via the [Override Style Group](https://devnet.logianalytics.com/hc/en-us/articles/4405683590167-Configuring-Server-Profile#Style) property in the server profile, Server selects the style group by default. You can choose another style group from the list to apply to the exported output. If the page report was created in Logi Report Designer, when you select **<No Style>**, the style group property predefined for the specific export format in Logi Report Designer will apply.
* **Other properties**  
   Specify the properties for the selected format:
  + [PDF](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#PDF)
  + [HTML](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#HTML)
  + [Excel](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#Excel)
  + [Text](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#Text)
  + [RTF](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#RTF)
  + [XML](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#XML)
  + [PostScript](https://devnet.logianalytics.com/hc/en-us/articles/4405683737751-Advanced-Run-Dialog-Box-Properties#PS)
  + **Page Report Result**
    - **Zip Result**  
       Select to compress the result and make its size smaller.

**OK**

Select to export the report with the settings you specified here. If you have selected multiple report tabs to export at one time, and you have not specified parameter values for some of them, the [Enter Parameter Values dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405683747607-Enter-Parameter-Values-Dialog-Box-Properties) will pop up for you to specify their parameter values.

**Cancel**

Select to close the dialog box without exporting the report.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683626647-Enter-Values-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690507927-Fetch-Data-Dialog-Box-Properties)
