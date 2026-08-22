---
title: "Example of Creating an NLS Report"
id: 1500009589961
section: "Applying National Language Support - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589961-Example-of-Creating-an-NLS-Report
updated_at: 2021-07-24T05:54:32Z
---

# Example of Creating an NLS Report

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568542-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571242-Cresting-and-Applying-Styles)

# Example of Creating an NLS Report

This topic illustrates how to make the report Coffee Sales.wls in the SampleReports.cat catalog file display in Chinese.

It contains the following tasks:

> * [Task 1: Create an NLS Property File](#Task1)
> * [Task 2: Create a Data Mapping File](#Task2)
> * [Task 3: Publish the Report to Logi JReport Server](#Task3)
> * [Task 4: Apply NLS to the Report at runtime](#Task4)

## Task 1: Create an NLS Property File

1. [Open the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592981-Web-Reports#Open) Coffee Sales.wls in the catalog file SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. Select the **FilterControl** node representing the filter control Product Type in the Report Inspector and set its Map Name property to **true**. Select the nodes FilterControl1 and FilterControl2 representing the filter controls Category and Product Name respectively in the Report Inspector, you can find that their Map Name property is false.

   If the Map Name property of a filter control is set to true, its title, namely, the name shown in the text box of the Text property is the name shown in the Catalog Manager and cannot be changed, whose type in the NLS Editor will be Metadata. Otherwise, its title shown in the text box of the Text property is editable, and its type in the NLS Editor will be Title.
3. Select **View** > **Language** > **NLS Editor** to open the NLS Editor, then select the **Add**  button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) above the Language box.
4. In the Add Language dialog, select **Chinese (China)** from the Available Languages list and select **OK** to add it and return to the NLS Editor.
5. In the Display tab, the scope and types of the objects in the report and items need to be translated are listed in the Scope, Type and Key columns. You can find that only the type of the filter controls Category and Product Name is Title.

   ![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404889305495/nls_rpt_exmpl1.gif)
6. Give all the corresponding target language text in the Translate in <language> column and select **OK**.

   ![Translate in NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404893832855/nls_rpt_exmpl2.gif)

## Task 2: Create a Data Mapping File

1. On the Catalog Manager toolbar, select the **Data Mapping Editor** to display the Data Mapping Editor.
2. Select the **New** button, then in the Create Data Mapping File dialog, type **DataMapping** in the File Name text box, select **Chinese (China)** from the Language drop-down list and select **OK** to return to the Data Mapping Editor.

   ![Create Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404889305751/nls_rpt_exmpl4.gif)
3. Select the **Import Key** button. In the Import Key dialog, select the following fields used in the report one by one by pressing the Ctrl button on the keyboard: Country and Region in the Customers table; Category, Product Name and Product Type Name (the Product Type field used in the report) in the Products table. Select **OK**.

   ![Import Key dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893833111/nls_rpt_exmpl5.gif)
4. Double-click cells in the Map to Value column to specify the mapping values for the imported fields to Chinese. Select **OK**.

   ![Translate in Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404889306007/nls_rpt_exmpl6.gif)
5. Select **File** > **Options**. In the Options dialog, select **Catalog** from the Category box, uncheck the option **Forbid editing data object properties**, and then select **OK**.
6. In the Catalog Manager, select the **Category** field in the Products table, expand the Properties sheet on the left, then select **DataMapping** as the value of its Data Mapping File property.
7. Repeat the step above to set the Data Mapping File property of the fields Product Name and Product Type Name to DataMapping respectively. Select **Save Catalog** on the Catalog Manager toolbar to save the changes.
8. In the design area, select the chart legend and the Region field in the crosstab and set their Data Mapping File property to **DataMapping** in the Report Inspector respectively.

   You may notice that the Data Mapping File property can be specified in both the Catalog Manager and the Report Inspector. In Logi JReport, you can specify the data mapping file of a field used in a report both at the catalog level and report level. When the property is specified at both levels, the data mapping file set in the Report Inspector has the higher priority.
9. Save the report.

## Task 3: Publish the Report to Logi JReport Server

Now the NLS property file and corresponding data mapping file are created and applied to the report Coffee Sales.wls. Publish the report and the catalog it uses to Logi JReport Server. For details, refer to [Publishing Resources Remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500009592641-Publishing-Resources#Remotely).

## Task 4: Apply NLS to the Report at Runtime

1. Log onto the Logi JReport Server Console page.
2. On the Start Page, select **Profile** under the Manage category. The Profile page is displayed.
3. Switch to the **Advanced** tab, check the **Yes** checkbox of the Enable NLS option, and select **Chinese (China)** from the Default Language drop-down list. Select **OK** in this dialog and then Select **OK** in the prompt message dialog.

   ![Profile page - Advanced](https://devnet.logianalytics.com/hc/article_attachments/4404889306263/nls_rpt_exmpl7.gif)
4. On the Logi JReport Server Resources page, locate the report published just now and select to run it in Web Report Studio. The report is displayed in Chinese.

   ![Run Report](https://devnet.logianalytics.com/hc/article_attachments/4404889306519/nls_rpt_exmpl8.gif)
5. Select **Edit Mode** from the mode drop-down menu on the Web Report Studio toolbar.
6. Select the chart or the crosstab, the business view it uses is then displayed in the Resources panel. You can see all resources in the resource tree are now displayed as you translated for the metadata objects in the NLS Editor in Logi JReport Designer.

   ![Resources Panel](https://devnet.logianalytics.com/hc/article_attachments/4404893833367/nls_rpt_exmpl9.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009568542-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009571242-Cresting-and-Applying-Styles)
