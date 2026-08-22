---
title: "Example of Creating an NLS Report"
id: 1500010068861
section: "Applying National Language Support - Logi JReport Designer v16"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010068861-Example-of-Creating-an-NLS-Report
updated_at: 2022-02-02T22:43:10Z
---

# Example of Creating an NLS Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068901-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034902-Creating-and-Applying-Styles)

# Example of Creating an NLS Report

This topic introduces how to make an English report display in Chinese with example. The example is based on the report Sales Detail Report.wls in the SampleReports.cat catalog file.

This example contains the following tasks:

* [Task 1: Create an NLS property file](#Task1)
* [Task 2: Create a data mapping file](#Task2)
* [Task 3: Publish the report to Logi JReport Server](#Task3)
* [Task 4: Apply NLS to the report at runtime](#Task4)

**Task 1: Create an NLS property file**

1. Select **File** > **Open** to open the web report Sales Detail Report.wls in the catalog file SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Select the node **FilterControl** representing the filter control PRODUCT TYPE in the Report Inspector and set the Map Name property to **true**. Select the nodes FilterControl1 and FilterControl2 representing the filter controls CATEGORY and PRODUCT NAME respectively in the Report Inspector, you can find that their Map Name property is false.

   If the Map Name property of a filter control is set to true, its title, namely, the name shown in the text box of the Text property is the name shown in the Catalog Manager and cannot be changed, whose type in the NLS Editor will be Metadata. Otherwise, its title shown in the text box of the Text property is editable, and its type in the NLS Editor will be Title.
3. Select **View** > **Language** > **NLS Editor** to open the NLS Editor, then select the **Add**  button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404901125271/btn_add.gif) above the Language box.
4. In the Add Language dialog, select **Chinese (China)** from the Available Languages list and select **OK** to add it and return to the NLS Editor.
5. In the Display tab, the scope and types of the objects in the report and items need to be translated are listed in the Scope, Type and Key columns. You can find that only the type of the filter controls CATEGORY and PRODUCT NAME is Title.

   ![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901157399/nls_rpt_exmpl1.gif)
6. Give all the corresponding target language text in the Translate in <language> column and select **OK**.

   ![Translate in NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404901157655/nls_rpt_exmpl2.gif)

**Task 2: Create a data mapping file**

1. On the Catalog Manager toolbar, select the **Data Mapping Editor** to display the Data Mapping Editor.
2. Select the **New** button, then in the Create Data Mapping File dialog, type **DataMapping** in the File Name text box, select **Chinese (China)** from the Language drop-down list and select **OK** to return to the Data Mapping Editor.

   ![Create Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404909143703/nls_rpt_exmpl4.gif)
3. Select the **Import Key** button. In the Import Key dialog, select the following fields used in the report one by one by pressing the Ctrl button on the keyboard: Country and Region in the Customers table; Category, Product Name and Product Type Name (the Product Type field used in the report) in the Products table. Select **OK**.

   ![Import Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404909143959/nls_rpt_exmpl5.gif)
4. Double-click cells in the Map to Value column to specify the mapping values for the imported fields to Chinese. Select **OK**.

   ![Translate in Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404901157911/nls_rpt_exmpl6.gif)
5. In the Catalog Manager, select the **Category** field in the Products table, select **Show Properties**  on the toolbar to show the Properties sheet, then select **DataMapping** as the value of its Data Mapping File property.
6. Repeat the step above to set the Data Mapping File property of the fields Product Name and Product Type Name to DataMapping respectively. Select **Save Catalog** on the Catalog Manager toolbar to save the changes.
7. In the design area, select the chart legend and the Region field in the crosstab and set their Data Mapping File property to **DataMapping** in the Report Inspector respectively.

   You may notice that the Data Mapping File property can be specified in both the Catalog Manager and the Report Inspector. In Logi JReport, you can specify the data mapping file of a field used in a report both at the catalog level and report level. When the property is specified at both levels, the data mapping file set in the Report Inspector has the higher priority.
8. Save the report.

**Task 3: Publish the report to Logi JReport Server**

Now the NLS property file and corresponding data mapping file are created and applied to the report Sales Detail Report.wls. Publish the report and the catalog it uses to Logi JReport Server. For details, refer to [Publishing Resources Remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500010070761-Publishing-and-Downloading-Resources#Remotely).

**Task 4: Apply NLS to the report at runtime**

1. Log onto the Logi JReport Server Console.
2. On the Start Page, select **My Profile** under the Manage category. The My Profile > Customize Server Preferences page is displayed.
3. Switch to the **Advanced** tab, check the **Yes** checkbox of the Enable NLS option and select **Chinese (China)** from the Default Language drop-down list. Select **OK** in this dialog and then select **OK** in the prompt message dialog.

   ![Advanced tab](https://devnet.logianalytics.com/hc/article_attachments/4404901158167/nls_rpt_exmpl7.gif)
4. On the Logi JReport Server console > Resources page, locate the report published just now and select to run it in Web Report Studio. The report is displayed in Chinese.

   ![Run Report](https://devnet.logianalytics.com/hc/article_attachments/4404901158423/nls_rpt_exmpl8.gif)
5. Select **Edit Mode** from the mode drop-down menu on the Web Report Studio toolbar.
6. Select the chart or the crosstab, the business view it uses is then displayed in the Resources panel. You can see all resources in the resource tree are now displayed as you translated for the metadata objects in the NLS Editor in Logi JReport Designer.

   ![Resources Panel](https://devnet.logianalytics.com/hc/article_attachments/4404901158679/nls_rpt_exmpl9.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404901108631/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010068901-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404901037591/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010034902-Creating-and-Applying-Styles)
