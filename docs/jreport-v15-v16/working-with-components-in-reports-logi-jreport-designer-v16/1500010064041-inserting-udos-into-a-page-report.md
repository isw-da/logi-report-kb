---
title: "Inserting UDOs into a Page Report"
id: 1500010064041
section: "Working with Components in Reports - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010064041-Inserting-UDOs-into-a-Page-Report
updated_at: 2021-07-24T10:39:18Z
---

# Inserting UDOs into a Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064021-Creating-UDOs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064001-Built-in-UDOs-JHyperLink-and-JRotator)

# Inserting UDOs into a Page Report

UDOs can be inserted in the page report areas listed in [Component Placement](https://devnet.logianalytics.com/hc/en-us/articles/1500010063261-Working-with-Components-in-Reports-#Relationship).

**To insert a UDO to a page report:**

1. Make sure the setenv.bat batch file in `<install_root>\bin` has been modified to include the required classes.
2. Start Logi JReport Designer, then create a new report, or open an existing report.
3. Do one of the following:
   * Drag the **UDO** button ![UDO button](https://devnet.logianalytics.com/hc/article_attachments/4404909176727/btn_instudo.gif) from the Components panel to the destination where you want to insert the UDO.
   * Select **Insert** > **UDO** or **Home** > **Insert** > **UDO**.
4. In the Insert UDO dialog, select a UDO as required from the UDO drop-down list. The list contains all UDOs that have been registered in the file setenv.bat.

   ![Insert UDO dialog](https://devnet.logianalytics.com/hc/article_attachments/4404901201815/instudo.gif)
5. Select **OK** in the dialog.
   * If you use menu command to insert the UDO, select the mouse button in the desired location to insert the UDO there.
   * If you take the dragging and dropping method to insert the UDO, the UDO will be inserted there upon selecting the OK button.

After a UDO has been inserted into a report, when you publish the report to Logi JReport Server, be sure to include the class path in the setenv batch file in Logi JReport Server (`<server_root>\bin\setenv.bat`).

## Example: Using UDO to Insert a Quadrant Chart into a Banded Object

Logi JReport provides you with a demo UDO, with which you can insert a quadrant chart into a banded object. To use this demo UDO, four jar files are required: myudo.jar, jfreechart-1.0.13.jar, jfreechart-1.0.13-swt.jar, and jcommon-1.0.16.jar. The file myudo.jar is saved in `<install_root>\help\samples\UDODemo\JQuadrantChart`, and you can further edit it if you want. The last three jars can be downloaded from the website: <http://www.jfree.org/jfreechart>.

**To insert a quadrant chart into a banded object using the demo UDO:**

1. Append the four jars to the ADDCLASSPATH variable of the batch file setenv.bat.
2. Add the following to the file udo.ini in `<install_root>\lib`:

   ```
   Begin   
    
   name=JQuadrantChart  
    
   template=jet.udodemo.JQuadrantTmpl  
    
   resultobject=jet.udodemo.JQuadrantRslt  
    
   resultcreator=jet.udodemo.JQuadrantCrtr  
    
   resultviewer=jet.udodemo.JQuadrantRndr  
    
   objecteditor=jet.udodemo.JQuadrantDsgn  
    
   End
   ```
3. Start Logi JReport Designer and select **File** > **Open Catalog** to open the catalog file SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
4. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010034782-Creating-Reports#Page)  which is based on the query WorldWideSales in Data Source 1 of the catalog and is grouped by the Product ID field.
5. Select **<New Summary...>** in the Summaries node of the Data panel.
6. In the New Summary dialog, specify the Aggregate Function as **Sum**, add the field **Price**  from the Products table to the Summary On text box, check the **Static Summary** radio button, specify the Group By field as **Product ID** from the Products table, and then select **OK**.

   ![New Summary](https://devnet.logianalytics.com/hc/article_attachments/4404909268887/cmpnt_udo_inst_cht1.gif)
7. Enter **Sum Price**  in the Summary Name dialog and select **OK** to create the summary.
8. Repeat steps 5 to 7 to create another summary Sum Cost, which uses Sum as the aggregate function, summarizes on the Cost field and is grouped by the Product ID field.
9. Resize the group header panel of the banded object and add the two summaries to the panel as follows:

   ![Banded Object](https://devnet.logianalytics.com/hc/article_attachments/4404901312535/cmpnt_udo_inst_cht2.gif)
10. Select the banded page header panel (BPH) and select **Insert** > **UDO**.
11. In the Insert UDO dialog, select **JQuadrantChart** from the UDO drop-down list, and then select **OK**.
12. Select the mouse button in the banded page header panel to insert the UDO there.
13. Keep the JQuadrantChart focused and go to the Report Inspector to define its properties as follows:

    * **Column Name**: Product ID
    * **Quadrant Origin X**: 750
    * **Quadrant Origin Y**: 200
    * **X Values**: Sum Price
    * **Y Values**: Sum Cost
14. Resize the banded page header panel, save the report and preview it. The report displays as follows:

    ![UDO in Banded Page Header Panel](https://devnet.logianalytics.com/hc/article_attachments/4404909269143/cmpnt_udo_inst_cht3.gif)

Below are the special properties of this demo UDO. You can edit the property values to suit your requirements.

| Property Name | Description |
| --- | --- |
| Chart Title | Specifies the title of the quadrant chart. Data type: String |
| Column Name | Specifies the field whose values will be used as the values of the X axis, which can only be the outermost group-by field of the banded object. Data type: String |
| Quadrant Font Bold | Specifies whether to make the text in the quadrant chart bold. This property takes effect only when the property Show Quadrant Text is set to true and certain text is specified for the property Quadrant1 Text, Quadrant2 Text, Quadrant3 Text or Quadrant4 Text. Data type: Boolean |
| Quadrant Font Color | Specifies the color of the text in the quadrant chart. Choose a color from the drop-down list, enter a hexadecimal RGB value (for example, 0xff0000), or select Custom from the drop-down list to specify the color. This property takes effect only when the property Show Quadrant Text is set to true and certain text is specified for the property Quadrant1 Text, Quadrant2 Text, Quadrant3 Text or Quadrant4 Text. Data type: String |
| Quadrant Font Face | Specifies the font of the text in the quadrant chart. Choose an option from the drop-down list. This property takes effect only when the property Show Quadrant Text is set to true and certain text is specified for the property Quadrant1 Text, Quadrant2 Text, Quadrant3 Text or Quadrant4 Text. Data type: Enumeration |
| Quadrant Font Size | Specifies the font size of the text in the quadrant chart. Enter an integer value to change the size. This property takes effect only when the property Show Quadrant Text is set to true and certain text is specified for the property Quadrant1 Text, Quadrant2 Text, Quadrant3 Text or Quadrant4 Text. Data type: Integer |
| Quadrant Origin X | Specifies the value of the X axis for the origin point. Data type: Float |
| Quadrant Origin Y | Specifies the value of the Y axis for the origin point. Data type: Float |
| Quadrant Separator Color | Specifies the color of the lines used to separate the quadrants of the chart. Choose a color from the drop-down list, enter a hexadecimal RGB value (for example, 0xff0000), or select Custom from the drop-down list to specify the color. This property takes effect only when the property Show Quadrant Separator is set to true. Data type: String |
| Quadrant Separator Width | Specifies the width of the lines used to separate the quadrants of the chart. Enter a numeric value to change the width. This property takes effect only when the property Show Quadrant Separator is set to true. Data type: Float |
| Quadrant1 Color | Specifies the color for the first quadrant of the chart. Choose a color from the drop-down list, enter a hexadecimal RGB value (for example, 0xff0000), or select Custom from the drop-down list to specify the color. Data type: String |
| Quadrant1 Text | Specifies the text to be displayed in the first quadrant of the chart. This property takes effect only when the property Show Quadrant Text is set to true. Data type: String |
| Quadrant1 Transparency | Specifies the transparency for the first quadrant of the chart, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Quadrant2 Color | Specifies the color for the second quadrant of the chart. Choose a color from the drop-down list, enter a hexadecimal RGB value (for example, 0xff0000), or select Custom from the drop-down list to specify the color. Data type: String |
| Quadrant2 Text | Specifies the text to be displayed in the second quadrant of the chart. This property takes effect only when the property Show Quadrant Text is set to true. Data type: String |
| Quadrant2 Transparency | Specifies the transparency for the second quadrant of the chart, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Quadrant3 Color | Specifies the color for the third quadrant of the chart. Choose a color from the drop-down list, enter a hexadecimal RGB value (for example, 0xff0000), or select Custom from the drop-down list to specify the color. Data type: String |
| Quadrant3 Text | Specifies the text to be displayed in the third quadrant of the chart. This property takes effect only when the property Show Quadrant Text is set to true. Data type: String |
| Quadrant3 Transparency | Specifies the transparency for the third quadrant of the chart, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Quadrant4 Color | Specifies the color for the fourth quadrant of the chart. Choose a color from the drop-down list, enter a hexadecimal RGB value (for example, 0xff0000), or select Custom from the drop-down list to specify the color. Data type: String |
| Quadrant4 Text | Specifies the text to be displayed in the fourth quadrant of the chart. This property takes effect only when the property Show Quadrant Text is set to true. Data type: String |
| Quadrant4 Transparency | Specifies the transparency for the fourth quadrant of the chart, in percent. Enter a numeric value to change the transparency. Data type: Integer |
| Show Quadrant Separator | Specifies whether to show the lines used to separate the quadrants of the chart. Data type: Boolean |
| Show Quadrant Text | Specifies whether to show the text in the quadrants of the chart. Data type: Boolean |
| X Values | Specifies the field whose values will be displayed as the values of the X coordinate. Only the fields with numeric values in the group header panel of the banded object can be used. Data type: String |
| Y Values | Specifies the field whose values will be displayed as the values of the Y coordinate. Only the fields with numb eric values in the group header panel of the banded object can be used. Data type: String |

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010064021-Creating-UDOs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010064001-Built-in-UDOs-JHyperLink-and-JRotator)
