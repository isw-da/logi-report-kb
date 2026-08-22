---
title: "XML Option Dialog"
id: 1500010068381
section: "References - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068381-XML-Option-Dialog
updated_at: 2021-07-24T10:38:17Z
---

# XML Option Dialog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033042-XML-Connection-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033442-Object-Property-Reference)

# XML Option Dialog

The XML Option dialog helps you to specify the parameters for running a report in the XML format. It appears when you set the Default Format for Viewing Report property of a report tab or a web report to XML and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404909121559/btn_chsr1.gif) in the value cell in the Report Inspector.

![XML Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901167127/xmloptn.gif)

The following are details about options in the dialog:

**Only Data**

* If checked, the exported XML file will only contain the database column information. The exported XML schema file will only contain the structure information of the report.
* If unchecked, the exported XML file will also contain elements controlled by formulas, and the exported XML schema file will contain all the detailed information from the report, including all the property values of each report object.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the XML result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010033042-XML-Connection-Wizard-Dialog) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010033442-Object-Property-Reference)
