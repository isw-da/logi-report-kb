---
title: "XML Option Dialog Box"
id: 1500010060862
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010060862-XML-Option-Dialog-Box
updated_at: 2021-07-23T19:16:09Z
---

# XML Option Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099221-XML-Connection-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099781-Object-Property-Reference)

# XML Option Dialog Box

The XML Option dialog box helps you to predefine the options for directly running a report in XML on Server. It appears when you set the Default Format for Viewing Report property of a report tab or a web report to "XML" and then select the ellipsis button ![Ellipsis button](https://devnet.logianalytics.com/hc/article_attachments/4404856823191/btn_ellipsis1.gif) in the value cell in the Report Inspector.

![XML Option dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856879255/xmloptn.gif)

The following are details about options in the dialog box:

**Only Data**

* If the option is selected, the XML output will only contain the database column information. The exported XML schema file will only contain the structure information of the report.
* If unselected, the XML output will also contain elements controlled by formulas, and the exported XML schema file will contain all the detailed information from the report, including all the property values of each report object.

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the XML output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Cancels the changes and exits the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099221-XML-Connection-Wizard-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099781-Object-Property-Reference)
