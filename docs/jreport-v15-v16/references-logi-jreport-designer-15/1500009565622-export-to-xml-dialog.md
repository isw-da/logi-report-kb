---
title: "Export to XML Dialog"
id: 1500009565622
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009565622-Export-to-XML-Dialog
updated_at: 2021-07-24T05:55:20Z
---

# Export to XML Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565602-Export-to-Text-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565502-Expression-Dialog)

# Export to XML Dialog

The Export to XML dialog appears when you select File > Export > To XML. It helps you to [export a report to XML format](https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML). [See the dialog](javascript:%20void(null)).

![Export to XML dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893839255/expt2xml.gif)

The following are details about options in the dialog:

**Export to**

Specifies the file name and directory where you want to store the exported XML file.

**Schema File Name**

Specifies the directory and the name of an existing XML schema (.xsd) file. If you specify an existing XML schema file, the exported XML file, the generated XML file that is to be exported will be based on it. Otherwise, a new XML schema file will be generated to the directory where the exported XML file is to be exported. The new XML schema file and the exported XML file will have the same name but with different extensions.

**Select Report Tabs**

When exporting a page report, you can specify the report tabs in the page report you want to export to the XML file. The selected report tabs will be exported in the list order. If the report has only one report tab, it is selected by default.

![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404893808791/btn_mvup.gif)

Moves the specified report tab one step up.

![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404889289751/btn_mvdwn.gif)

Moves the specified report tab one step down.

**Only Data**

* If checked, the exported XML file will only contain the database column information. The exported XML schema file will only contain the structure information of the report.
* If unchecked, the exported XML file will also contain elements controlled by formulas, and the exported XML schema file will contain all the detailed information from the report, including all the property values of each report object.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the exported XML file.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565602-Export-to-Text-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009565502-Expression-Dialog)
