---
title: "Exporting to XML"
id: 1500010099401
section: "Delivering Your Reports - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099401-Exporting-to-XML
updated_at: 2021-07-23T19:16:12Z
---

# Exporting to XML

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099361-Exporting-to-RTF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099341-Exporting-to-PostScript)

# Exporting to XML

This topic describes how you can export the result of a page or web report to an XML format file.

1. Open the report that you want to export.
2. Select **File** > **Export**  > **To XML**. Designer displays the [Export to XML dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096761-Export-to-XML-Dialog-Box).

   ![Export to XML dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856872343/expt2xml.gif)
3. Select the **Browse** button to specify the destination directory and file name of the XML file. You can also type the location and file name in the **Export to** text box manually (make sure that the folder you specify does exist; otherwise, Designer displays an error message).
4. In the **Schema File Name** text box, specify an XSD file to export the report to an XML file based on the XSD file. If you do not specify an existing XML schema file, Designer generates a new XSD file in the directory where you specify to export the XML file with the same name as the XML file.
5. If you are exporting a page report, in the **Select Report Tabs** box, select the report tabs in the page report that you want to export. Designer exports the selected report tabs in the list order. You can make use of the **Move Up**![Move Up button](https://devnet.logianalytics.com/hc/article_attachments/4404848403735/btn_mvup.gif) and **Move Down**![Move Down button](https://devnet.logianalytics.com/hc/article_attachments/4404856822935/btn_mvdwn.gif) buttons to change the order of the report tabs.
6. Select the **Only Data** checkbox to only export data of the report.
7. Select **Run Linked Report** if you want to generate the reports that you link with the report (not including the detail reports) in the XML output. If you are only interested in the primary report, leave this option unselected. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, causes performance issue.
8. Select **OK** to start exporting.

You should pay attention to the following when using the Export to XML feature:

* The existing schema file that you specify must also be generated from the report. If you use other schema files, you get a NullPointerException exception.
* If the existing schema file that you specify contains only data, and you have cleared the Only Data checkbox in the Export to XML dialog box, the exported XML file then only contains database column information. The content of the XML file is consistent with the schema file it is based on.
* If you delete an element node or an attribute node from the existing schema file, the exported XML file which is based on it, cannot contain the corresponding column. In a schema file containing not only data, only the removal of an element used in a formula control property can affect an XML file which is based on it.

  **Example: Deleting an element node from a schema file affects the exported XML file which is based on it**

  Let's take Employee Information List.cls as an example.

  1. Select **File** > **Open**.
  2. In the Open Report dialog box, select the **Browse** button to open the catalog file **SampleReports.cat** in `<install_root>\Demo\Reports\SampleReports`, then open the sample report **Employee Information List.cls**.
  3. Export the report to an XML file. You then get two files: Employee Information List\_Employee Information.xml and Employee Information List\_Employee Information.xsd.
  4. Open **Employee Information List\_Employee Information.xsd**, and delete **Employee Information List\_Employee Information\_ReportBody\_PagePanel\_PageHeaderPanel\_ label4** from Employee Information List\_Employee Information\_ReportBody\_PagePanel\_PageHeaderPanel.
  5. Export the report to an XML file again. This time, specify the modified Employee Information List\_Employee Information.xsd as the file to base it on.

     The newly exported Employee Information List\_Employee Information.xml file does not contain information about Employee Information List\_Employee Information\_ReportBody\_PagePanel\_PageHeaderPanel\_ label4.
* If you do not want to see all the property values in a generated XML file, you can comment out any unwanted properties in this way:
  1. Open the file **JRXMLTag.properties** located in **resource\_en\_US.jar** in `<install_root>\lib`.
  2. Add a question mark in front of any unwanted properties to comment them out. See below:

     Change: Suppressed=Suppressed

     To: ?Suppressed=Suppressed
  3. When you export the report to XML, the XML file does not contain the property **Suppressed** for each report object.
  4. Save the property file and refresh the one in resource\_en\_US.jar.

     In addition, when you clear **Only Data** and add an "@" symbol in front of the value in JRXMLTag.properties, the property listed in the Element node then moves to the Attribute node.

     For example, in JRXMLTag.properties,

     Change: StartYPos=StartYPos

     To: StartYPos=@StartYPos

     You can then find that the **StartYPos** property is now listed in the Attribute node.

     Before adding the "@" symbol in front of a value, the StartYPos property should have been listed in the Element node.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010099361-Exporting-to-RTF)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010099341-Exporting-to-PostScript)
