---
title: "Example: Developing Reports from a Web Service Data Source"
id: 1500009585381
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585381-Example-Developing-Reports-from-a-Web-Service-Data-Source
updated_at: 2021-07-24T05:55:42Z
---

# Example: Developing Reports from a Web Service Data Source

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564362-Editing-the-Operation-Used-to-Create-Tables)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564222-User-Defined-Data-Sources)

# Example: Developing Reports from a Web Service Data Source

In this example, we use a WSDL file from <http://www.webservicex.net/> to demonstrate how to use web service as the data source to create a report.

1. [Open the catalog file](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog) SampleReports.cat in `<install_root>\Demo\Reports\SampleReports`.
2. In the Catalog Manager, select any data source node, select **New Data Source** on the toolbar.
3. In the New Data source dialog, specify the name of the data source as **Medicare Providers**, select the **SOAP Web Service**  connection type and select **OK**.

   ![New Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893962391/cnctn_wbsvc_exmpl_dtsrc.gif)
4. In the SOAP Web Service Data Source dialog, check the **URI** radio button, and then type the URI string: **http://www.webservicex.net/medicareSupplier.asmx?WSDL** in the text field to get the WSDL file.

   ![SOAP Web Service Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889395095/cnctn_wbsvc_exmpl_web.gif)
5. Keep the default settings for other options in the dialog, and then select **OK**.

Next we are going to add tables via the connection into the Logi JReport catalog.

1. Locate the **Tables** node in the web service connection, right-click it and select **Add Tables** from the shortcut menu to display the Add Tables dialog.
2. Select **GetSupplierByZipCode** from the Operation Name drop-down list.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889395351/cnctn_wbsvc_exmpl_tbl.gif)
3. In the Input Message column, select **zip**, then in its value column, select ![New Formula/Parameter button](https://devnet.logianalytics.com/hc/article_attachments/4404893837335/btn_fmla.gif) and select **<New Parameter...>** from the drop-down list.
4. In the New Parameter dialog, input **pZipCode** as the parameter name in the Name text field.
5. Select **Type-in Parameter** from the Value Setting drop-down list.
6. Set the data type of the parameter value to **String** from the Value Type drop-down list.
7. In the Value List box, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a value line, select in it and then type in **85226**.
8. Repeat the above step to add three more values one by one: 80027, 20878, 20874.
9. In the Options box, enter **Type a zip code** as the prompt text.

   ![New Parameter dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893962647/cnctn_wbsvc_exmpl_1.gif)
10. Select **OK** to return to the Add Table dialog.
11. Select **OK** to add the table to the web service connection.

Now will use the tables got from the web service data source to create a [business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) and then create a web report using the business view.

1. Locate the **Business Views**  node in the data source on which the web service connection is set, right-click it and select **New Business View**  from the shortcut menu.
2. Specify the name of the business view as **MedicareProvider** in the Input Business View Name dialog, then select **OK**. The Add Tables/Views/Queries dialog appears.
3. In the All Tables/Views/Queries box, expand the connection > **Tables** node, select all the tables and select **![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893789463/btn_addarrow.gif)** to add them to the Selected Tables/Views/Queries box. Select **OK**.

   ![Add Tables/Views/Queries dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893962903/cnctn_wbsvc_exmpl_addtbvwqy.gif)
4. In the Query Editor, select all the columns in the tables by selecting the **\*** checkboxes and select **OK**. Then select **Yes** in the prompt message.

   ![Query Editor](https://devnet.logianalytics.com/hc/article_attachments/4404889395607/cnctn_wbsvc_exmpl_qryedtr.gif)
5. In the Business View Editor, drag and drop the tables from the Resource Objects panel to the MedicareProvider node in the Business View panel.

   ![Business View Editor](https://devnet.logianalytics.com/hc/article_attachments/4404893963159/cnctn_wbsvc_exmpl_bvedtr.gif)
6. Select **Save** on the editor toolbar to save the business view, then close the editor.
7. Upon closing the Business View Editor, Logi JReport will prompt you to create a report using the business view. Select New Web Report in the prompted dialog. A blank report is created.
8. [Insert a table in the web report](https://devnet.logianalytics.com/hc/en-us/articles/1500009563682-Inserting-a-Table#Web) with the type Table (Group Above) which is based on MedicareProvider in the data source Medicare Providers, shows the fields SupplierNumber, CompanyName**,** City and Description, and grouped by the field Zip.
9. Right-click the TableGroupFooter panel and select **Hide** from the shortcut menu to hide it from view. Repeat to hide the TableFooter panel in the same way.
10. Select **Home**/**File** > **Save** to save the report as **MedicareProviderInfobyZip.wls**.
11. Select the **View** tab to preview the report. The Enter Parameter Values dialog appears.

    ![Enter Parameter Values dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893963415/cnctn_wbsvc_exmpl_2.gif)
12. Type a zip code or select the one you want from the drop-down list, and then select **OK**. The report will be displayed according to your selected parameter value. For example, specify the zip code as 20878, then the report will be displayed as follows, showing information for zip code 20878 only:

    ![View Report](https://devnet.logianalytics.com/hc/article_attachments/4404893963671/cnctn_wbsvc_exmpl_3.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564362-Editing-the-Operation-Used-to-Create-Tables)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564222-User-Defined-Data-Sources)
