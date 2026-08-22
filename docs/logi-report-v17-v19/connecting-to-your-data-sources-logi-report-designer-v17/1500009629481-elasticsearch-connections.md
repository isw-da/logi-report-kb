---
title: "Elasticsearch Connections "
id: 1500009629481
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009629481-Elasticsearch-Connections
updated_at: 2021-07-24T16:05:09Z
---

# Elasticsearch Connections 

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606762-Hive-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources)

# Elasticsearch Connections

You can set up Elasticsearch connections in Logi Report catalogs to get data from Elasticsearch data sources. An Elasticsearch connection contains relational data which is transformed from an Elasticsearch data source.

Logi Report Designer gets data from Elasticsearch data sources in the same way as it gets data from [JSON data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500009606902-JSON-Connections#How).

This topic includes the following sections:

* [Setting Up Elasticsearch Connections in a Catalog](#Set)
* [Adding More Tables to an Elasticsearch Connection](#Add)
* [Managing the Tables in an Elasticsearch Connection](#Manage)

## Setting Up Elasticsearch Connections in a Catalog

To set up an Elasticsearch connection to connect a Logi Report catalog to an Elasticsearch data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New Elasticsearch Connection** from the shortcut menu.  

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **Elasticsearch** connection type and select **OK**.

   The [Elasticsearch Data Source Options](https://devnet.logianalytics.com/hc/en-us/articles/1500009608042-Elasticsearch-Data-Source-Options-Dialog) dialog appears.

   ![Elasticsearch Data Source Options dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904343191/elstcschdtscoptn.gif)
3. Specify the URL, user name and password with which to connect to the Elasticsearch data source.
4. To get data from the Elasticsearch data source by the request body, select **Use Request Body Search** and specify the request body.

   Parameters and constant level formulas predefined in the catalog data source in which the Elasticsearch connection is created, as well as the special field User Name can be used in the URL and the request body in the same way as in [aggregation pipeline expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500009606942-Imported-APEs#Expression).
5. To get data from the Elasticsearch data source by the scroll API, select **Scroll** and specify how long the scroll API will keep the search context alive. For details about the scroll API, refer to <https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html>.
6. When parameters and formulas are referenced in the URL or request body, you can select the **Edit Format** button to edit the format of their values.
7. Select **OK**. The [Elasticsearch Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009630961-Elasticsearch-Connection-Wizard-Dialog) appears.

   ![Elasticsearch Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404904343447/elstcschcnctnwzd_mdfy.gif)
8. In the Modify Schema Properties screen, the elements in the Elasticsearch schema are listed in the Schema box. You can select an element and modify its properties in the Properties box. Select **Next**.
9. In the Transformed Relational Schema screen, the relational tables built based on the transformed relational schema structure are listed. Check the transformed result listed in the Transformed Tables box, and then select **Next**.

   ![Elasticsearch Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404904343703/elstcschcnctnwzd_trnsfrmd.gif)
10. In the Add Table screen, add the required tables to the connection.

    ![Elasticsearch Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404904343959/elstcschcnctnwzd_adtbl.gif)

    [Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views) are created on tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
11. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Tables to an Elasticsearch Connection

When an Elasticsearch connection is set up, you can add more tables transformed from the Elasticsearch data source into the Logi Report catalog via the Elasticsearch connection.

1. Do one of the following:
   * Right-click the Elasticsearch connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the Elasticsearch connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the Elasticsearch connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the Elasticsearch connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the Elasticsearch connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   The [Add Tables](https://devnet.logianalytics.com/hc/en-us/articles/1500009607162-Add-Tables-Dialog) dialog appears.

   ![Add Tables dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916819991/addtbl_xml.gif)
2. Select the **Refresh** button. The tables contained in the schema that is transformed from the Elasticsearch data source will then be displayed in the Tables box.
3. Choose the required tables in the Tables box and select **Add**.

   To choose consecutive tables, select the first table, press and hold down the **SHIFT** key, and then select the last table. To choose tables that are not consecutive, press and hold down **CTRL**, and then select each table.
4. After adding the required tables, select **Done** to close the dialog.

## Managing the Tables in an Elasticsearch Connection

For the tables that have been transformed from an Elasticsearch data source and added into a Logi Report catalog via the specified Elasticsearch connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms#Remove) the same as you do on tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009606762-Hive-Connections) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606982-User-Defined-Data-Sources)
