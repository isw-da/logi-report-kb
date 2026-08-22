---
title: "Export to XML Dialog Box"
id: 1500010096761
section: "References - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010096761-Export-to-XML-Dialog-Box
updated_at: 2021-07-23T19:15:24Z
---

# Export to XML Dialog Box

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096741-Export-to-Text-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096621-Expression-Dialog-Box)

# Export to XML Dialog Box

You can use the Export to XML dialog box to [export a report to XML](https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML). This topic describes the options in the dialog box.

Designer displays the Export to XML dialog box when you select File > Export > To XML.

![Export to XML dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856872343/expt2xml.gif)

You see the following options in the dialog box:

**Export to**

Specify the file name and directory where to save the XML file. Select the Browse button to specify the file name and directory.

**Schema File Name**

- Specify an XSD file to export the report to an XML file based on the XSD file. Select the Browse button to specify the schema file.
- **Select Report Tabs**

  Designer displays the option when you use the dialog box for exporting a page report. Select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. If the report has only one report tab, Designer selects the report tab by default.

  ![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif)**Move Up button**

  Select to move the specified report tab higher in the list.

  ![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif)**Move Down button**

  Select to move the specified report tab lower in the list.

**Only Data**

* If you select the option, the XML output contains only the database column information, and the exported XML schema file contains only the structure information of the report.
* If you clear the option, the XML output also contains elements controlled by formulas, and the exported XML schema file contains all the detailed information from the report, including all the property values of each report object.

**Run Linked Report**

Select to generate the reports that you link with the report (not including the detail reports)

**OK**

Select to apply all changes and close the dialog box.

**Cancel**

Select to close the dialog box without saving any changes.

**Help**

Select to view information about the dialog box.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010096741-Export-to-Text-Dialog-Box)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010096621-Expression-Dialog-Box)
