---
title: "Advanced Run Dialog Box Properties"
id: 1500009773921
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009773921-Advanced-Run-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:49Z
---

# Advanced Run Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773861-Add-to-Global-NLS-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774381-Analysis-Template-Properties)

# Advanced Run Dialog Box Properties

Use the Advanced Run dialog box to run a report in [Advanced mode](https://devnet.logianalytics.com/hc/en-us/articles/1500009778381-Running-Reports#Advanced). This topic describes how to specify advanced settings for running a report.

This topic contains the following sections:

* [General Tab Properties](#General)
* [Parameter Tab Properties](#Parameter)
* [Format Tab Properties](#Format)
* [Archive Tab Properties](#Archive)
* [Duration Tab Properties](#Duration)

You see these elements on all the tabs:

**Back**

Select **Back** to go back to the left tab.

**Next**

Select **Next** to go to the right tab.

**Finish**

Select **Finish** to run the report with the settings you specified here.

**Cancel**

Select **Cancel** to close the dialog box without running the report.

**Help**

Select **Help** to view information about the Advanced Run dialog box.

## General Tab Properties

Use the General tab to specify report and catalog information and task priority.

![Advanced Run dialog - General tab](https://devnet.logianalytics.com/hc/article_attachments/4404880234903/advcdrn_gen.gif)

**Select Report Tabs**

Server displays this section for page reports only. Select the report tabs which you want to run. The selected report tabs will run in the list order. If the page report has only one report tab, Server selects it by default.

* ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404885326231/btn_mvup.gif)**Move Up button**  
   Select to move the specified report tab higher in the list.
* ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404880154263/btn_mvdown.gif)**Move Down button**  
   Select to move the specified report tab lower in the list.

**Select Dynamic Connection**

Server displays this section when there are multiple dynamic connections for the current log-in user. You can specify a dynamic connection.

* **Data Source**  
   Data source name in the catalog.
* **Connection Name**  
   Dynamic connection name.
* **Connection**  
   Select a dynamic connection from the drop-down list.
* **Connection Properties**  
  [Information](https://devnet.logianalytics.com/hc/en-us/articles/1500009745922-Edit-Dynamic-Connection-Dialog-Box-Properties) of the selected dynamic connection, which is read only.

**Report Information**

Report and catalog information.

* **Report**  
   Report name and path in the server resource tree.
* **Catalog**  
   Catalog name and path in the server resource tree. Unavailable to [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports).
  + **Select Another Catalog**  
     Select **Select Another Catalog** to choose another catalog for the report in the [Select Another Catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009746402-Select-Another-Catalog-Dialog-Box-Properties) dialog box.
* **Report Version**  
   Select the report version. Unavailable to shared reports.
* **Catalog Version**  
   Select the catalog version. Unavailable to shared reports.
* **Priority**  
   Select a priority level of the report running task. The priority levels are from 1 to 10 in ascending order of lowest priority to highest priority. This property is available to administrators. By default, Server ignores this property unless you modified server.properties to set queue.policy not equal to 0.

## Parameter Tab Properties

Use the Parameter tab to specify the parameter values if any to run the report.

![Advanced Run dialog - Parameter tab](https://devnet.logianalytics.com/hc/article_attachments/4404885514775/advcdrn_prm.gif)

**Enter Parameters**

Server displays the parameters that the report uses. [Edit the values](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values) according to your requirement.

If the report does not use any parameters, Server displays "No Parameter Needed" here.

**![Use Saved Values button](https://devnet.logianalytics.com/hc/article_attachments/4404880238871/btn_srv_ussvvlu.gif) Use Saved Values**

If you see this icon, you can select the previously saved parameter values to apply to the report and [save parameter values for reuse later](https://devnet.logianalytics.com/hc/en-us/articles/1500009778361-Specifying-Parameter-Values#Reuse).

**Save as default**

Select **Save as default** to save current parameter values as the default parameter values for the report. Server displays this option when you did not clear [Enable Setting Default Parameter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#DefaultParam) the corresponding report type in the server profile.

This option is a user-report level setting. It is an action and takes effect after you Select **OK** in the dialog box. Its initial status is always cleared.

## Format Tab Properties

Use the Format tab to specify the format in which you would like to run the report and set the format properties.

![Advanced Run dialog - Format tab](https://devnet.logianalytics.com/hc/article_attachments/4404885373719/advcdrn_fmt.gif)

**Select Format**

Select the format of the report result.

* **Select Format**  
   Select the format in which the report result will be and the properties of the format. The format can be one of the following:
  + [Web Report](#Web)
  + [Page Report](#DHTML)
  + [HTML](#HTML)
  + [PDF](#PDF)
  + [Excel](#Excel)
  + [Text](#Text)
  + [RTF](#RTF)
  + [XML](#XML)
  + [PostScript](#PS)

**Advanced**

Advanced format settings.

* **Enable Style Group**  
   If you have specified a style group via the [Override Style Group](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#Style) option in the server profile, Server selects this option and displays the specified default style group in the Style Group box by default. You can also choose another style group from the Style Group drop-down list to run the selected page report tabs or web report.

  When the <No Style> item is selected in the Override Style Group drop-down list, Server clears this option by default and uses the style group property of the page report tab or web report for this format that is predefined in Logi Report Designer to run the selected page report tabs or web report.
* **Enable Converting Encoding**  
   Select **Enable Converting Encoding** to enable the conversion of encoding. Then Server activates the Before Converting and After Converting options. Select the encoding from the drop-down lists.
* **Enable NLS**  
   Select this option to enable NLS for the report. Then Server displays the Using Language drop-down list for you to choose a language. If there is no NLS resource defined for the report, you can only run the report using the default language.
* **Encoding**  
   Select the encoding for the report.
* **Connect to [Data Source Name] [Connection Name]**  
   Specify the DB user and password with which you want to connect to the data source that the report uses. For the default connection, Server does not display [Connection Name].
  + **Use the DB user and password defined in catalog**  
     If the option is selected, the DB user and password defined in the catalog will be used.
  + **Use the DB User**  
     Select this option and you can then specify another DB user and password instead of the one defined in the catalog.
* **Use User Defined Default On-screen Filter Values**  
   Select this option to apply the default on-screen filter values that you have specified to the report. Server displays the option when you did not clear [Enable Setting Default On-screen Filter Values For](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#OnScreenFilter) the corresponding report type in the server profile.
* **Add TaskListener to be Invoked**  
   Select this option to call a Java application before/after the report runs so as to obtain information about the report task. Server enables the option only when the format is not Page Report or Web Report.

## Archive Tab Properties

You see the options below only when the view format is NOT Page Report or Web Report in the Format tab.

![Advanced Run dialog - Archive tab](https://devnet.logianalytics.com/hc/article_attachments/4404880235415/advcdrn_archv.gif)

**Auto Archive Properties**

Select this option to archive the result version automatically after the report has finished running.

**Archive Location**

Location in which to archive the report result version.

* **Built-in Version Folder**  
   Select this option to save the report result version to the built-in version folder. Server does not display the option to [organization users](https://devnet.logianalytics.com/hc/en-us/articles/1500009749922-Multitenancy-Supported-via-Organizations) when the report is in the Public Reports folder, and to [shared reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009777281-Sharing-Web-Reports) either.
* **My Reports Folder**   
   Select this option to save the report result version to the My Reports folder.
* **Public Reports Folder**   
   Select this option to save the report result version to the Public Reports folder. Server does not display the option to organization users.
* **Organization Reports Folder**  
   Select this option to save the report result version to the Organization Reports folder. Server displays the option to organization users only.

**Input archive destination and result name**

Type the name and location with which to archive the result.

**Apply Archive Policy**

Select this option to apply an archive policy to the report result version.

* **Archive as New Version**  
   Select this option to enable multiple versions for the report result.
  + **Maximum Number of Versions**  
     Type the maximum number of versions that Server displays in the version table of the report result. The default value is 0 means unlimited version number.
* **Replace Old Version**   
   Select this option to replace the old version when Server generates a new version.

**Result Auto-delete**

Select this option if you want Server to delete the result. Then specify when to delete it. If the time you specified to delete the result exceeds one hundred years, Server keeps the result forever.

* **Result Expires in N Days**  
   Type the number of days to keep the report result before Server deletes it.
* **Result Expires After**  
   Select this option and then select a date to delete the report result after the date.

**Set Permissions**

Available only when the Archive Location is a public folder and when you have the Grant permission on the report. Select **Set Permissions** to set user permissions to the specified report in the [Set Permissions](https://devnet.logianalytics.com/hc/en-us/articles/1500009774321-Set-Permissions-Dialog-Box-Properties) dialog box.

## Duration Tab Properties

Server displays the Duration tab only when you have [enabled the task-level timeout mechanism](https://devnet.logianalytics.com/hc/en-us/articles/1500009777301-Managing-Report-Running-Tasks#Timeout). In this tab, you can specify a time duration for a task, and ask Server to cancel the task or to notify you or someone else of the task status via e-mail if the task has not yet finished running when the task duration is up.

![Advanced Run dialog - Duration tab](https://devnet.logianalytics.com/hc/article_attachments/4404880287511/advcdrn_drtn.gif)

**Timeout**

Type the time duration for the task.

**Notify by e-mail after the specified time**

Select this option to send an e-mail about the task information when the specified time is up.

* **Mail To**  
   Type the e-mail address of the recipient.

**Cancel the task after the specified time**

Select this option to cancel the running task when the specified time is up.

---

### Web Report

Select **Web Report** to run a web report in Web Report Studio.

**Resolution**

Resolution of the result to zoom in/out, in DPI. Server obtains the default value from the operation system, which is the resolution of your monitor, for example, 72 DPI on Unix or 96 on Windows. You can set higher/lower value to zoom in/out.

**View Mode**

Select the Web Report Studio mode to run the report.

* **View Mode**  
   Select **View Mode** if you want Web Report Studio to run in View Mode by default. You can switch to Edit Mode if it is available.
* **View Mode Only**  
   Select **View Mode Only** if you want Web Report Studio to run in View Mode only. You are not able to switch to Edit Mode.
* **Edit Mode**  
   Select **Edit Mode** if you want Web Report Studio to run in Edit Mode by default. You can switch to View Mode if it is available. The option is available only when you have the [Edit permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) on the report.

### Page Report

Select **Page Report** to run a page report in Page Report Studio.

**Resolution**

Resolution of the result to zoom in/out, in DPI. Server obtains the default value from the operation system, which is the resolution of your monitor, for example, 72 DPI on Unix or 96 on Windows. You can set higher/lower value to zoom in/out.

**View Mode**

Select the Page Report Studio mode to run the report.

* **Basic View**  
   Select **Basic View** if you want Page Report Studio to run in Basic View by default. You can switch to Interactive View if it is available.
* **Basic View Only**  
   Select **Basic View Only** if you want Page Report Studio to run in Basic View only. You are not able to switch to Interactive View.
* **Interactive View**  
   Select **Interactive View** if you want Page Report Studio to run in Interactive View by default. You can switch to Basic View if it is available. The option is available only when you have the [Edit permission](https://devnet.logianalytics.com/hc/en-us/articles/1500009778641-Managing-Permissions) on the report.

**Profile**

Select the Page Report Studio profile to apply to run the report, which contains [a set of Page Report Studio settings](https://devnet.logianalytics.com/hc/en-us/articles/1500009774341-Page-Report-Studio-Profile-Properties).

**Background Mode Timeout**

Select this option to specify the time after which the report will continue to run in background mode. When a page report runs and Server has not generated the result yet after the specified time, the report will automatically run in background mode. Once the report is complete you can find the result in the My Tasks > [Background Tasks table](https://devnet.logianalytics.com/hc/en-us/articles/1500009777301-Managing-Report-Running-Tasks#Background).

The option takes effect when you have selected [Enable Background Task for Reports](https://devnet.logianalytics.com/hc/en-us/articles/1500009743782-Configuring-Server-Profile#BackgroundTask) in the server profile.

### HTML

**No Margin**

Select **No Margin** if you want to remove the margins you originally set while designing the report.

**Multiple Files**

Select if you want to generate the report result to multiple HTML files. Server designates a serial number for each HTML page. For example, if you name a 3-page report as "sales", Server will create three files called sales\_1.html, sales\_2.html, and sales\_3.html.

* **Embedded CSS**  
   Select if you want to embed the cascading style sheet (CSS) in the HTML files; otherwise, Server generates the .css file individually.

**Single File**

Server generates the report result to a single HTML file.

* **No Hyperlink**  
   Select if you do not want to see hyperlinks for navigating previous and next pages on the navigation bar of the generated HTML file.
* **No Page Number**  
   Select if you do not want to see page number information showing the current page number and total page number on the navigation bar of the generated HTML file.

**Drilldown**

Select to enable the Drilldown feature in the HTML report result so that you can inspect certain items for further detailed data.

**Section 508 Compliant Output**

Select if you want to add the accessibility attributes defined for the report elements via the Report Inspector to the HTML result which is Section 508 compliant. For more information, select [Making HTML and PDF Report Results and Server Console Accessible](https://devnet.logianalytics.com/hc/en-us/articles/1500009743362-Making-HTML-and-PDF-Report-Results-and-Server-Console-Accessible).

When you select Section 508 Compliant Output, Server selects and disables the Use HTML Data Table and Relative Font Size options. The output will be Section 508 compliant including HTML data table, accessible attributes, and relative font feature.

**Use HTML Data Table**

Select if you want to output the table and crosstab components to table objects in the HTML result.

**Absolute Font Size**

Select if you want to generate the report result using fixed font size that you cannot adjust according to the font size settings in the web browser.

**Relative Font Size**

Select if you want to generate the report result using a relative font size that you can adjust according to the font size settings in the web browser.

**Image Chart**  
 Select the image type with which to display charts:

* **Auto-select**  
   Select if you want Server to automatically detect the image format: GIF if the image colors are less than 256 colors or else JPEG.
* **GIF**  
   Select **GIF**, a lossless compression technique that supports only 256 colors, for images with only a few distinct colors, such as line drawings, black and white images, and small text that is only a few pixels high.
* **JPEG**  
   Select **JPEG**, a lossy compression technique that is designed to compress color and grayscale continuous-tone images. JPG images support 16 million colors, are best suited for photographs and complex graphics, and are supported on the Web.
* **PNG**  
   Select **PNG**, which provides a portable, legally unencumbered, well-compressed (effectively 100 percent lossless compression), well-specified standard for lossless bitmapped image file. PNG supports indexed-color images of up to 256 colors and shows a more interchangeable, flexible, and robust function than GIF.

**Resolution**

Resolution of the result to zoom in/out, in DPI. Server obtains the default value from the operation system, which is the resolution of your monitor, for example, 72 DPI on Unix or 96 on Windows. You can set higher/lower value to zoom in/out.

**Web Browser**

Select IE or Firefox as the web browser for which the HTML result adapts.

**Text Overflow**

Choose whether to make the text overflow is visible or hidden.

**Run Linked Report**

Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

### PDF

**No Margin**

Select to remove the margins you originally set while designing the report.

**Compress Image**

Select to compress the images in the report by the percentage you type in the box.

**Generate charts and barcodes using images (recommended)**

Select if you want to take the result of the whole report as a graphic to transform the report by the method of simulated printer.

**Generate charts and barcodes using vector graphics**

Select if you want to take the result of the whole report as a dataset to transform the report by sequence.

**TOC**

Select to generate a Table of Contents in the PDF report result. Not supported for web report.

**Drilldown**

Select to enable the Drilldown feature in the HTML report result so that you can inspect certain items for further detailed data.

**Encrypt**

Select if you want to encrypt the PDF file. You can then select **Settings** to configure the encrypt settings in the [Encrypt](https://devnet.logianalytics.com/hc/en-us/articles/1500009746002-Encrypt-Dialog-Box-Properties) dialog box.

**Sign**

Select if you want to add the digital sign to the PDF file. You can then select **Settings** to configure the sign settings in the [Sign](https://devnet.logianalytics.com/hc/en-us/articles/1500009774641-Sign-Dialog-Box-Properties) dialog box.

**Run Linked Report**

Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

**Accessible PDF**

Select to generate the report result as an accessible PDF file. For more information, select [Making HTML and PDF Report Results and Server Console Accessible](https://devnet.logianalytics.com/hc/en-us/articles/1500009743362-Making-HTML-and-PDF-Report-Results-and-Server-Console-Accessible).

**Zoom**

Select the zooming of the report content in the PDF file. You can select an item from the drop-down list or type a percentage in the text box. A valid percentage is greater than 0 and no larger than 6400% (you can type the value with or without the percent sign). Server treats any invalid input as **Default**.

* **Default** - It means no zoom setting. After you open the PDF file in the Adobe Acrobat, the zoom setting follows that in the Adobe.
* **Actual Size** - The report content remains its original size. It is same as 100%.
* **Fit Page** - The report content in a page fills the entire page within the window both horizontally and vertically. If the required horizontal and vertical scale ratios are different, the smaller of the two is used.
* **Fit Width** - The report content in a page fills the page width within the window.
* **Fit Height** - The report content in a page fills the page height within the window.
* **Fit Visible** - The report content in a page fills the width of its bounding box within the window.

### Excel

**Excel Version**

Select the Excel version.

* **Excel 97-2003 Workbook (\*.xls)**  
   Select to run the file as .xls format.
* **Excel Workbook (\*.xlsx)**  
   Select to run the file as .xlsx format.

**Format**

Select the format of the Excel result.

* **Auto Format**  
   Select to let Server determine the format according to the objects in the report. Server uses Column Format when the report contains crosstabs or tables, or else Report Format. Server selects this option by default.
* **Report Format**  
  Select if you want to make the formatting of the report in Excel match the format as designed in the template. Use this format if you just want to view the report in Excel.
* **Column Format**  
   Select to calculate all components' row/column values in the report using the Columned property value of the report when exporting. Choose this format if you want to actively use the result in Excel such as filtering and sorting.
* **Data Format**   
   Select to only generate the report data without format. This option is only available for the Excel version Excel 97-2003 Workbook (\*.xls).

**More/Less Options**

Select to show/hide the additional settings for running the report to Excel. When you have selected Data Format as Format, only Word Wrap and Run Linked Report are available here.

* **Include Shapes in Export**  
   Select to include the drawing objects in the Excel result, such as line, oval, and box.
* **Print Page Header**  
   Type the page header text for the printed file.
* **Print Page Footer**  
   Type the page footer text for the printed file.
* **Word Wrap**  
   Word-wrap settings.
  + **All Keep Existing**  
    Select to keep all the settings of each object's Word Wrap property originally specified in the report.
  + **All Disabled**  
     Select to disable the Word Wrap property for all objects. That is, the Word Wrap property is made false for all objects.
  + **All Enabled**  
     Select to enable the Word Wrap property for all objects. That is, the Word Wrap property is made true for all objects.
* **Print Gridlines**  
   Select to include gridlines when printing the Excel result.
* **Run Linked Report**Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

### Text

**Delimited Format**

Select to generate the report result to a standard Text file, using a delimiter you specify to separate the fields.

* **Use Quote Mark**  
   Select to use quote marks in the Text file.
* **Repeat Last Column Value If Null**  
   Select if you want a cell that has no value in the generated CSV Text file to use the value of the previous cell in the same column.
* **Custom Delimiter**  
   Select if you want to separate the fields in the generated Text file by a user defined delimiter. You can type your own delimiter in the Delimiter box.
* **Tab Delimited**  
   Select to use a Tab delimiter to separate the fields.
* **CSV Format**   
   Select to use a comma to separate the fields.

**Horizontal Density**

Type an integer value for each unit of the horizontal density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the width between columns. By default, Logi Report decides the density.

**Vertical Density**

Type an integer value for each unit of the vertical density between columns. The resulting density is a direct ratio of the value you specify. That is, the greater the value, the smaller the height between columns. By default, Logi Report decides the density.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)

* When using user defined densities, if you do not set the densities appropriately, the fields in the report may overlap each other, so you should not use this way to run the report result to Text.
* When setting the value of Horizontal/Vertical Density, you need to pay attention to the following:
  + The value of Horizontal/Vertical Density must be greater than the character's width/height of the smallest field in the report (smallest field is the field with the smallest font size), otherwise, Logi Report does not apply the value you set.
  + If one of the values of Horizontal/Vertical Density is greater than 0 and the other one is less than 0, Logi Report applies the value greater than 0 and decides the other value.
  + If the values of Vertical Density and Horizontal Density are both greater than 0 and the value of Horizontal Density is less than 1, Logi Report applies the specified value of the two densities. Otherwise, Logi Report decides the two values.
  + If the values of Vertical Density and Horizontal Density are both less than 1, Logi Report decides the two values.

**Compress**

Select to generate the report result to Text format in a compressed size. There will be no clearance between the columns.

**Header and Footer**

Select if you want the Text file to contain all headers and footers in the report, including Report Header/Footer, Page Header/Footer, and Group Header/Footer. Otherwise, the Text file will only contain the data in the Detail panel.

**Windows End-of-line (CR-LF)**

Select to use Windows end-of-line characters to indicate the start of a new line. Two characters <cr> and <lf> will be used at the end of the line.

**Unix End-of-line (LF)**

Select to use Unix End-of-line characters to indicate the start of a new line. Only the Unix End-of-line character <lf> will be used.

**Run Linked Report**

Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

### RTF

**Best Editing**

Select to apply flow layout for the RTF result.

**No Margin**

Select to remove the margins you originally set while designing the report.

**Run Linked Report**

Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

**Tip:** Microsoft Word Document limits the maximum page size in Word Print Layout to 22 inches. Therefore, when you export a report with many columns in the RTF format and then view it in Microsoft Word Document, the columns on the right might get lost. If this happens you can switch to Web Layout. If still not working, try a latest version of Microsoft Word Document.

### XML

**Only Data**

Select this option if you want to only contain the database column information in the generated XML file and to only contain the structure information of the report in the generated XML schema file.

Clear this option if you want to also contain elements controlled by formulas in the generated XML file will and to contain all the detailed information from the report, including all the property values of each report object, in the generated XML schema file.

**Schema File Name**

Type the directory and the name of an existing XML schema file (.xsd). Server generates the XML file based on it. Otherwise, Server generates a new XML schema file to the directory where the XML file is. The new XML schema file and the XML file will have the same name but with different extensions.

![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")To prevent SSRF vulnerability, you can add a white list of URLs so that Server proceeds the schema file URL that you entered here only when it matches one of the URL patterns in the white list.

![Marks content and feature updates for Logi Report v17.1. New feature new content.](https://devnet.logianalytics.com/hc/article_attachments/4404885305367/___newv17.1.jpg "New for Logi Report v17.1.")To add a while list of URLs, add a Java system property **-Dlogireport.ssrf.whitelist** in the startup file of Server, and set the property value to a string that contains a list of URL patterns separated by semi-colon. The URL pattern obeys the Java regular expression rule.

**Run Linked Report**

Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

### PostScript

**No Margin**

Select to remove the margins you originally set while designing the report.

**Run Linked Report**

Select **Run Linked Report** if you want to generate the linked reports (not including the detail reports) in the result when the report is linked with other reports. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time will cause performance issue, especially when the linked reports contain a large amount of data.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773861-Add-to-Global-NLS-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009774381-Analysis-Template-Properties)
