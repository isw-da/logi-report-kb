---
title: "Advanced Exporting with JSPs"
id: 1500009691782
section: "Page Report Studio Logi JReport Server v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691782-Advanced-Exporting-with-JSPs
updated_at: 2021-11-03T06:56:47Z
---

# Advanced Exporting with JSPs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718221-Opening-Multiple-Reports-in-One-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718241-Page-Report-Studio-Tag-Library)

# Advanced Exporting With JSPs

This topic introduces the export functions that need to be customized using JSPs.

Below is a list of the sections covered in this topic:

* [Exporting the Result Using a JavaScript Function](#Function)
* [Customizing Buttons for One-Step Exporting](#OneStep)
* [Controlling User Access to Different Export Formats](#Access)
* [Customizing Warning Messages](#Warning)

## Exporting the Result Using a JavaScript Function

Logi JReport provides you with a JavaScript function which allows you to open the report result or export it in a specified format. You can find this function in the file API.js in `<install_root>\public_html\javascript\dhtml`, as shown below:

*function user\_oneStepExport(type, options)*

The following explains this function's two parameters, type and options, in detail.

**type** - Specifies the export format.

* HTML = 0
* PDF = 2
* PS = 3
* RTF = 4
* TEXT = 5
* EXCEL = 6
* XML = 7

**options** - Specifies the values of the options of each format. It is a string array whose member is of the format "key=value". The options and their usage are listed as follows:

| Key | Description | Available Value | Default Value |
| --- | --- | --- | --- |
| HTML | | | |
| to\_ver | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| browser | Specifies the web browser type. | 0 - IE or Chrome 1 - Firefox | 0 |
| imagetype | Specifies the type of the images in the result file. | 0 - Decided by Logi JReport 1 - GIF  2 - JPG | 0 |
| overflow | Specifies the overflow type. | 0 - VISIBLE 1 - HIDDEN  2 - VERFLOWCOUNT | 0 |
| resolution | Specifies the HTML resolution. | Any integer between 1 and 4294967296 | 96 |
| title | Specifies the title for the HTML file. | Any string | "" |
| css | Specifies whether or not to embed the cascading style sheet in the exported HTML files. | true, false | false |
| multi | Specifies whether or not to generate an HTML file for each page of the report result. | true, false | false |
| hyperlink | Specifies whether or not to contain hyperlinks in the HTML file. | true, false | false |
| pagenumber | Specifies whether or not to contain page numbers in the HTML file. | true, false | false |
| drilldown | Specifies whether or not to include the drilled-down file in the exported HTML file. | true, false | false |
| no\_margin | Specifies whether or not to remove the original margins. | true, false | false |
| absolute | Specifies whether or not to make the font size fixed in the web browser. | true, false | false |
| PDF | | | |
| to\_ver | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| no\_margin | Specifies whether or not to remove the margin. | true, false | false |
| simulate | Specifies whether or not the mode is to be Simulated Printing Mode. | true, false | true |
| standard | Specifies whether or not to set the mode as Standard Mode. | true, false | false |
| content | Specifies whether or not to contain the TOC in the exported PDF file. | true, false | false |
| drilldown | Specifies whether or not to include the drilled-down file in the exported PDF file. | true, false | false |
| encrypt | Specifies whether or not to encrypt the report result. | true, false | false |
| compress | Specifies whether or not to compress the images in the report. | true, false | false |
| ratio | Specifies the percentage with which to compress the images in the report. | Any integer between 1 to 100 | 20 |
| compatibility | Specifies the encryption compatibility. | 0 - Acrobat 3.0 and later 1 - Acrobat 5.0 and later | 1 |
| doc\_psw | Specifies the password for opening the PDF file when encrypt=true. | Any string | "" |
| permi\_pasw | Specifies the password for printing and editing the PDF file when encrypt=true. | Any string | "" |
| printing | Specifies the PDF printing mode. | 0 - Prevents users from printing the file 4 - Allows low resolution-printing  2052 - Allows high-resolution printing | 0 |
| changes | Defines which editing actions are allowed in the PDF file. | 0 - Prevents users from making any changes to the file 1024 - Allows inserting, deleting, and rotating pages  256 - Allows users to fill in form fields and adding digital signatures.  32 - Allows users to fill in form fields and add digital signatures and comments  40 - Allows users to do anything except extracting pages  2108 - Allows all | 0 |
| enable\_copy | Specifies whether or not to allow users to copy the file contents. | true, false | false |
| enable\_access | Specifies whether or not to let visually impaired users read the document with window readers. | true, false | true |
| PostScript | | | |
| to\_ver | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| no\_margin | Specifies whether or not to remove the margins in the PS file. | true, false | false |
| RTF | | | |
| to\_version | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| rtf\_flow | Specifies whether or not to apply a flow layout when exporting the report to RTF. | true, false | false |
| no\_margin | Specifies whether or not to remove the margins in the RTF file. | true, false | false |
| Text | | | |
| to\_ver | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| repeat | Specifies whether or not to replace a field value of a record with that of its previous record if the field value is null. | true, false | false |
| compress | Specifies whether or not to compress the clearance between columns. | true, false | false |
| win\_linebreak | Specifies whether or not to use Windows end-of-line characters. | true, false | true |
| normal | Specifies whether or not to generate the report result to a standard text file. | true, false | true |
| quote\_mark | Specifies whether or not to mark the fields in the exported file with quotation marks. | true, false | false |
| head\_foot | Specifies whether or not to contain all headers and footers in the report. | true, false | true |
| delimiter | Specifies the delimiter. | Any single character |  |
| width | Specifies the user-defined character width. | An integer |  |
| height | Specifies the user-defined character height. | An integer |  |
| Excel | | | |
| to\_ver | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| wrap | Specifies the word-wrap setting. | 0 - All Keep Existing 1 - All Disabled  2 - All Enabled | 0 |
| new\_layout | Specifies whether or not to use the new layout mode. | true, false | true |
| shapes | Specifies whether or not to include the shapes in the exported file. | true, false | false |
| excel\_2000 | Specifies whether or not to export the result in Data Format, which means only the report data will be exported without format. | true, false | false |
| advanced | Specifies whether or not to apply the advanced options. | true, false | false |
| header | Specifies the page header text. | Any string |  |
| footer | Specifies the page footer text. | Any string |  |
| gridline | Specifies whether or not to print gridlines when printing the exported Excel file. | true, false | false |
| XML | | | |
| to\_ver | Specifies whether or not to save the result to version. | true, false | false |
| to\_open | Specifies whether or not to export and open the result file. | true, false | false |
| to\_local | Specifies whether or not to save the result to a local file. | true, false | false |
| only\_data | Specifies whether or not to only contain the database column information in the exported XML file. | true, false | false |
| schema | Specifies the name of an existing schema file with its full path with which to generate the XML file. | An existing schema file with its full path. |  |

**Notes:**

* The three options to\_ver, to\_open, and to\_local are mutually exclusive, that is, only one of them should be true, and the rest false. If you set two or three of them to true, Logi JReport will only accept the first true and treat the rest as false. If you set all three to false, Logi JReport will consider to\_open as true.
* In the string array options, the members are separated by commas (","). You can arrange the members in any order, and omit those keys where you want to use the default value. For example, you can define a variable html\_options:

  `var html_options = ["imagetype=1", "resolution=120", "hyperlink=true", "no_margin=false", "title=hello world"];`

  Then, you can use `user_oneStepExport(0, html_options)` to obtain a URL for exporting the report result in HTML format.
* Logi JReport also provides the function user\_downloadReport(type, options) whose usage is similar to user\_oneStepExport.

## Customizing Buttons for One-Step Exporting

Seven buttons are provided for one-step exporting. They are Export to PDF, Export to Excel, Export to RTF, Export to HTML, Export to Text, Export to PS, and Export to XML. By default, the buttons are invisible on the Page Report Studio toolbar. You have to add them to the toolbar by modifying the index.jsp file in `<install_root>\public_html\dhtmljsp`.

Use the following two API functions to control the buttons:

* public void customizeToolbar(String SessionId, String RptSetId, String toolbarname, int[] buttonId);
* public void customizeToolbar(String SessionId, String RptSetId, String toolbarname, int[] buttonId, boolean isVisible);

Explanation of these parameters:

* **SessionId** - session ID, which can be retrieved by DHTMLUtil.getSessionID(request).
* **RptSetId** - report ID, which can be retrieved by obDHTMLUtil.getRptSetId(request).
* **toolbarname** - toolbar name, such as "Standard", "Analysis", "View", or user-defined ones.
* **buttonId[]** - toolbar button ID. It is an integer array, so you need define an integer array variant.

  For example: int[] mybuttonid ={DHTMLConstant.TOOLBAR\_EXPORTTOPDF, DHTMLConstant.TOOLBAR\_EXPORTTOXLS, TMLConstant.BTN\_EXPORT\_TO\_RTF}

  The array elements available for one-step exporting are:

  + DHTMLConstant.TOOLBAR\_EXPORTTOPDF
  + DHTMLConstant.TOOLBAR\_EXPORTTOXLS
  + DHTMLConstant.TOOLBAR\_EXPORTTORTF
  + DHTMLConstant.TOOLBAR\_EXPORTTOHTML
  + DHTMLConstant.TOOLBAR\_EXPORTTOTEXT
  + DHTMLConstant.TOOLBAR\_EXPORTTOPS
  + DHTMLConstant.TOOLBAR\_EXPORTTOXML
* **isVisible** - whether or not to show the buttons defined with buttonID[]. true -- show, false -- hide. This parameter can be absent, and then the value is true.

For example, if you want to add the Export to HTML button to the Page Report Studio toolbar, then:

1. Open the file index.jsp.
2. Add the code

   `int[] temparray = {DHTMLConstant.TOOLBAR_EXPORTTOHTML};  
    dhtmlConfig.customizeToolbar(SessionID, RptSetId, "Standard", temparray, true);`

   before

   `//<!-- Tool Bar -->  
    if(dhtmlConfig.isFeatureEnabled(SessionID, RptSetId, DHTMLConstant.FEATURE_TOOLBAR)){`
3. Start Logi JReport Server.
4. Run a report in Page Report Studio, and you will see a new button Export to HTML is displayed on the toolbar.

To add more than one button to the toolbar area, for example, adding Export to HTML and Export to PDF buttons to the toolbar:

1. Open the file index.jsp.
2. Add the code

   `int[] temparray = {DHTMLConstant.TOOLBAR_EXPORTTOHTML, DHTMLConstant.TOOLBAR_EXPORTTOPDF};  
    dhtmlConfig.customizeToolbar(SessionID, RptSetId, "Standard", temparray, true);`

   before

   `//<!-- Tool Bar -->  
    if(dhtmlConfig.isFeatureEnabled(SessionID, RptSetId, DHTMLConstant.FEATURE_TOOLBAR)){`
3. Start Logi JReport Server.
4. Run a report in Page Report Studio and you will see the buttons Export to HTML and Export to PDF are displayed on the toolbar.
5. Select the added button on the toolbar of the report page, the report will be exported to the corresponding format, using the default values of the format options.

## Controlling User Access to Different Export Formats

Logi JReport introduces an access control ability which can restrict different users to export report result to different formats. This is achieved by passing values to the global variable enableTypes in both customize\_panel.jsp and save\_result.jsp files in the `<install_root>\public_html\dhtmljsp` folder. The value of enableTypes should be Integer, and Logi JReport gives you the following integers to represent the corresponding report result types:

| Report Result Format | Int. Value |
| --- | --- |
| HTML | 0 |
| PDF | 1 |
| Excel | 2 |
| Text | 3 |
| RTF | 4 |
| XML | 5 |
| PostScript | 6 |

You can specify a value or an array to enableTypes using the integers in the above table. Or you can also use the integers which are not mentioned above, but if you do so, the Int. values will be ignored, and do not function. That is to say, if you pass the array {1,2,5,9,-2} to enableTypes, 9 and -2 will be ignored and {1,2,5} will work, so PDF, EXCEL, XML formats can be in use.

Assume that there are two users, user1 and user2. When user1 logs on, run a report in Page Report Studio, he can only export the report result as PDF and HTML formats. While user2 can export the report result as RTF and XML formats when logging on. To realize it, you can use the following codes in customize\_panel.jsp or save\_result.jsp file:

```
int[] enableTypes=null;  

String UserName=null;  

UserName=DHTMLUtil.getUserName(request);  

if(UserName.equalsIgnoreCase("user1"))  

enableTypes=new int[]{1,0};  

if(UserName.equalsIgnoreCase("user2"))  

enableTypes=new int[]{4,5};
```

## Customizing Warning Messages

You can customize the warning messages when exporting the report result to XML through Page Report Studio. With this function, you can specify what you want to show as a warning message. The custom warning messages are supported across web browsers.

To customize the warning messages, you need to customize the jsp files using either of the following two methods:

**Method 1**

1. Open the save\_result.jsp file in the `<install_root>\public_html\dhtmljsp` folder with your favorite editor.
2. Specify the value of customMsgForXML in the save\_result.jsp to whatever you want. The value cannot be "" or null.
3. Run a report in Page Report Studio, select **Menu** > **File > Export**  to display the Export dialog.
4. Select **XML** from the Select Report Result Format drop-down list, and if necessary, modify other properties as required, then select **OK**.
5. A warning message shows as you have defined.

**Method 2**

You can also export the report result via the Export panel instead of selecting Menu > File > Export. By default, the panel is hidden. So, the following is another way to create custom warning messages:

1. Open the customize\_panel.jsp file in the `<install_root>\public_html\dhtmljsp` folder with your favorite editor.
2. Set the class of panelDIV to visibleMargin to show the Export panel on web browser.
3. Specify the value of customMsgForXML in customize\_panel.jsp.
4. Run a report in Page Report Studio, and the Export panel together with the report shows.
5. Select **XML** from the Select Report Result Format drop-down list, and if necessary, modify other properties as required, then select **OK**.
6. A warning message shows as you have defined.

For example, using method2, when you need to export the report result as XML, and if you want to show "This is IE Browser" while browser is IE, you need to set panelDIV in customize\_panel.jsp file to visibleMargin as follows:

`<div id="<%=DHTMLConstant.DHTML_PREFIX%>panelDIV" class="visibleMargin">`

And then customize CustomMsgForXML in the same jsp file as follows:

`String browserName=request.getHeader("User-Agent");  
 String customMsgForXML ="This is "+browserName;`

Access Logi JReport Server via IE, run a report in Page Report Studio, select **XML** from the Select Report Result Format drop-down list in the Export panel, and select **OK**. Then a pop-up box will show you "This is IE Browser".

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009718221-Opening-Multiple-Reports-in-One-Session)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718241-Page-Report-Studio-Tag-Library)
