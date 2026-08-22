---
title: "XML Option Dialog Box"
id: 4405661751191
section: "References - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661751191-XML-Option-Dialog-Box
updated_at: 2022-01-27T20:35:38Z
---

# XML Option Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661750167-XML-Connection-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664614935-Object-Property-Reference)

# XML Option Dialog Box

You can use the XML Option dialog box to predefine the options for directly running a report in XML on Server. This topic describes the options in the dialog box.

Designer displays the XML Option dialog box when you set the Default Format for Viewing Report property of a report tab or a web report to "XML" and then select the ellipsis ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4420550841879/btn_ellipsis1.gif) in the value cell in the Report Inspector.

![XML Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550854679/xmloptn.gif)

You see the following options in the dialog box:

**Only Data**

Select to only generate data of the report in the XML output.

When you select Only Data, the XML output contains only the database column information, and the corresponding XML schema file contains only the structure information of the report; if you do no select Only Data, the XML output also contains elements controlled by formulas, and the XML schema file contains all the detail information from the report, including all the property values of each report object.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports) in the XML output. If you are only interested in the primary report, leave this option cleared. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.

**OK**

Select to apply your settings and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661750167-XML-Connection-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405664614935-Object-Property-Reference)
