---
title: "Exporting to XML"
id: 1500009589441
section: "Delivering Your Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589441-Exporting-to-XML
updated_at: 2021-07-24T05:54:39Z
---

# Exporting to XML

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589421-Exporting-to-RTF)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589401-Exporting-to-PostScript)

# Exporting to XML

To export the results of a report to an XML format file, follow the steps below:

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To****XML**. The [Export to XML](https://devnet.logianalytics.com/hc/en-us/articles/1500009565622-Export-to-XML-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839255/expt2xml.gif)
3. Specify the destination of the exported file in the Export to field box.
4. In the Schema File Name field, specify an XSD file to export the web report or report tab to an XML file based on the specified XSD file.
5. If you are exporting a page report, in the Select Report Tabs box, select the report tabs in the page report you want to export. The selected report tabs will be exported in the list order. You can select ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839511/btn_mvup3.gif) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404893839767/btn_mvdwn3.gif) to change the order or the report tabs.
6. Check the **Only Data** checkbox to only export data of the web report or report tab.
7. Check **Run Linked Report** if you want to include the reports that is linked with the report (not including the detail reports) in the exported XML result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.
8. When done, select the **OK** button, and a file with the extension .xml will be generated.

The following are some notes you should be aware of when exporting report results to XML:

* The existing schema file that you specify must also be generated from the web report or report tab. If you use other schema files, a NullPointerException exception will be thrown out.
* If the existing schema file that you specify contains only data, and you have cleared the Only Data checkbox in the Export to XML dialog, the exported XML file will then only contain database column information. The content of the exported XML file will be consistent with the schema file it is based on.
* If you delete an element node or an attribute node from the existing schema file, the exported XML file which is based on it, will not contain the corresponding column. In a not only data schema file, only the removal of an element used in a formula control property will affect an exported XML file which is based on it.

  **Example: Deleting an element node from a schema file affects the exported XML file which is based on it**

  Let's take EmployeeInformation.cls as an example.

  1. Select **File** > **Open**.
  2. In the Open Report dialog, select the **Browse** button to open the catalog file **SampleReports.cat** in `<install_root>\Demo\Reports\SampleReports`, then open the sample report **EmployeeInformation.cls**.
  3. Export EmployeeInformation.cls to an XML file. You will then get two files: EmployeeInformation\_report1.xml and EmployeeInformation\_report1.xsd.
  4. Open the **EmployeeInformation\_report1.xsd** file, and delete EmoloyeeInformation\_report1\_ReportBody\_PagePanel\_PageHeaderPanel\_ label3 from EmoloyeeInformation\_report1\_ReportBody\_PagePanel\_PageHeaderPanel.
  5. Export EmployeeInformation.cls to an XML file again. This time, specify the modified EmployeeInformation\_report1.xsd as the file to base it on.

     The newly exported EmployeeInformation\_report1.xml file will not contain information about EmoloyeeInformation\_report1\_ReportBody\_PagePanel\_PageHeaderPanel\_ label3.
* If you do not want to see all the property values in a generated XML file, you can comment out any unwanted properties in this way:
  1. Open the file **JRXMLTag.properties** located in resource\_en\_US.jar in `<install_root>\lib`.
  2. Add a question mark in front of any unwanted properties to comment them out. See below:

     Change: Suppressed=Suppressed

     To: ?Suppressed=Suppressed
  3. When you export the web report or report tab to XML, the exported XML file will not contain the property Suppressed for each report object.
  4. Save the property file and refresh the one in resource\_en\_US.jar.

     In addition, when you uncheck Only Data, and add an @ sign in front of the value in JRXMLTag.properties, the property listed in the Element node will then move to the Attribute node.

     For example, in JRXMLTag.properties,

     Change: StartYPos=StartYPos

     To: StartYPos=@StartYPos

     You will now find that the StartYPos property is now listed in the Attribute node.

     Before adding the @ sign in front of the value, the StartYPos property will have been listed in the Element node.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589421-Exporting-to-RTF)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009589401-Exporting-to-PostScript)
