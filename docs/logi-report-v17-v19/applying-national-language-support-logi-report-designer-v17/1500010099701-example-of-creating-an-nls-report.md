---
title: "Example of Creating an NLS Report"
id: 1500010099701
section: "Applying National Language Support - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099701-Example-of-Creating-an-NLS-Report
updated_at: 2021-07-23T19:16:17Z
---

# Example of Creating an NLS Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101441-Creating-and-Applying-Styles)

# Example of Creating an NLS Report

This topic presents an example to show how you can make an English report display in Chinese.

This example contains the following tasks:

* [Task 1: Create an NLS property file](#Task1)
* [Task 2: Create a data mapping file](#Task2)
* [Task 3: Publish the report to Server](#Task3)
* [Task 4: Apply NLS to the report at runtime](#Task4)

**Task 1: Create an NLS property file**

1. Select **File** > **Open** to open the web report **Sales Detail Report.wls** in the catalog file **SampleReports.cat** in `<install_root>\Demo\Reports\SampleReports`.
2. Select the node **Filter Control** representing the filter control PRODUCT TYPE in the Report Inspector and set the **Map Name** property to **true**. Select the nodes **Filter Control 1** and **Filter Control 2** representing the filter controls CATEGORY and PRODUCT NAME respectively in the Report Inspector, and you can find that their Map Name property is **false**.

   If you set the Map Name property of a filter control to "true", its title, namely, the value of its Text property is the same as the bound field's Name property in the Catalog Manager and you cannot change it, and its type in the NLS Editor dialog box is "Metadata"; otherwise, its Text property in the Report Inspector is editable, and its type in the NLS Editor dialog box is "Title".
3. Select **View** > **Language** > **NLS Editor**. Designer displays the NLS Editor dialog box.
4. Select the **Add** button ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif) above the **Language** box.
5. In the Add Language dialog box, select **Chinese (China)** from the **Available Languages** list and select **OK** to add it and return to the NLS Editor dialog box.
6. In the **Display** tab, Designer lists the scope and types of the objects in the report and items need to be translated in the Scope, Type, and Key columns. You can find that only the type of the filter controls CATEGORY and PRODUCT NAME is "Title".

   ![NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404848466199/nls_rpt_exmpl1.gif)
7. Give all the corresponding target language text in the **Translate in Chinese** column and select **OK**.

   ![Translate in NLS Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856865431/nls_rpt_exmpl2.gif)

**Task 2: Create a data mapping file**

1. On the Catalog Manager toolbar, select the **Data Mapping Editor**. Designer displays the Data Mapping Editor dialog box.
2. Select the **New** button, then in the Create Data Mapping File dialog box, type **DataMapping** in the **File Name** text box, select **Chinese (China)** from the **Language** drop-down list and select **OK** to return to the Data Mapping Editor dialog box.

   ![Create Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404856865815/nls_rpt_exmpl4.gif)
3. Select the **Import Key** button. In the Import Key dialog box, select the following fields used in the report one by one by pressing the Ctrl button on the keyboard: Country and Region in the Customers table; Category, Product Name, and Product Type Name (the Product Type field used in the report) in the Products table. Select **OK**.

   ![Import Key dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848466455/nls_rpt_exmpl5.gif)
4. Double-click cells in the **Map to Value** column to specify the mapping values for the imported fields to Chinese. Select **OK**.

   ![Translate in Data Mapping File](https://devnet.logianalytics.com/hc/article_attachments/4404856866583/nls_rpt_exmpl6.gif)
5. In the Catalog Manager, select the **Category** field in the Products table, select **Show Properties** on the toolbar to show the Properties sheet, then select **DataMapping** as the value of its **Data Mapping File** property.
6. Repeat the step above to set the Data Mapping File property of the fields **Product Name** and **Product Type Name** to DataMapping respectively.
7. Select **Save Catalog** on the Catalog Manager toolbar to save the changes.
8. In the design area, select the chart legend and the **Region** field in the crosstab and set their Data Mapping File property to DataMapping in the Report Inspector respectively.

   You may notice that you can specify the Data Mapping File property in both the Catalog Manager and the Report Inspector, meaning, you can specify the data mapping file of a field used in a report both at the catalog level and report level. When you specify the property at both levels, the data mapping file set in the Report Inspector has the higher priority.
9. Save the report.

**Task 3: Publish the report to Server**

By now, you have finished creating the NLS property file and the corresponding data mapping file and applied them to the report Sales Detail Report.wls. Publish the report and the catalog it uses to Server. For more information, see [Publishing Resources Remotely](https://devnet.logianalytics.com/hc/en-us/articles/1500010062722-Publishing-and-Downloading-Resources#Remotely).

**Task 4: Apply NLS to the report at runtime**

1. Log onto the Server Console.
2. In the Start Page, select **My Profile** under the **Manage** category. Server displays the My Profile > Customize Server Preferences page.
3. Switch to the **Advanced** tab, select the **Yes** checkbox of the **Enable NLS** option and select **Chinese (China)** from the **Default Language** drop-down list. Select the **OK** button.

   ![Advanced tab](https://devnet.logianalytics.com/hc/article_attachments/4404856866839/nls_rpt_exmpl7.gif)
4. In the Server Console > Resources page, locate the published Sales Detail Report.wls and run it in Web Report Studio. The report displays in Chinese as follows:

   ![Run Report](https://devnet.logianalytics.com/hc/article_attachments/4404848467095/nls_rpt_exmpl8.gif)
5. Select **Edit Mode** from the mode drop-down menu on the Web Report Studio toolbar.
6. Select the chart or the crosstab, Web Report Studio then displays the business view it uses in the Resources panel. You can see all resources in the resource tree display as you translated for the metadata objects in the NLS Editor in Designer.

   ![Resources Panel](https://devnet.logianalytics.com/hc/article_attachments/4404848467351/nls_rpt_exmpl9.gif)

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061202-Localizing-Page-Navigation-Links-in-HTML-Report-Outputs)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010101441-Creating-and-Applying-Styles)
