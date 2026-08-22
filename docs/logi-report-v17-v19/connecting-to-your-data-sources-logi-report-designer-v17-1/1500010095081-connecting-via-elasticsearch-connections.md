---
title: "Connecting via Elasticsearch Connections"
id: 1500010095081
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095081-Connecting-via-Elasticsearch-Connections
updated_at: 2021-07-23T19:14:52Z
---

# Connecting via Elasticsearch Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057622-Connecting-via-Hive-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources)

# Connecting via Elasticsearch Connections

An Elasticsearch connection contains relational data which is transformed from an Elasticsearch data source. This topic describes how you can set up Elasticsearch connections in a catalog, and add and manage tables transformed from the Elasticsearch data sources in the catalog via the connections.

This topic contains the following sections:

* [How Designer Gets Data from Elasticsearch Data Sources](#How)
* [Setting Up Elasticsearch Connections in a Catalog](#Set)
* [Adding More Tables to an Elasticsearch Connection](#Add)
* [Managing the Tables in an Elasticsearch Connection](#Manage)

## How Designer Gets Data from Elasticsearch Data Sources

Designer gets data from Elasticsearch data sources in the same way as it gets data from [JSON data sources](https://devnet.logianalytics.com/hc/en-us/articles/1500010057742-How-Designer-Gets-Data-from-JSON-Data-Sources).

## Setting Up Elasticsearch Connections in a Catalog

To set up an Elasticsearch connection to connect a catalog to an Elasticsearch data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, right-click the node of a data source and choose **New Elasticsearch Connection** from the shortcut menu.  

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **Elasticsearch** connection type and select **OK**.

   Designer displays the [Elasticsearch Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010058902-Elasticsearch-Data-Source-Options-Dialog-Box).

   ![Elasticsearch Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848580247/elstcschdtscoptn.gif)
3. Specify the URL, user name, and password with which to connect to the Elasticsearch data source.
4. To get data from the Elasticsearch data source by the request body, select **Use Request Body Search** and specify the request body.

   You can reference parameters and constant level formulas predefined in the catalog data source in which you create the Elasticsearch connection, as well as the special field "User Name" in the URL and the request body in the same way as in [aggregation pipeline expressions](https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs#Expression).
5. To get data from the Elasticsearch data source by the Scroll API, select **Scroll** and specify how long the Scroll API will keep the search context alive. For more information about the Scroll API, see <https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html>.
6. When you reference parameters and formulas in the URL or request body, you can select the **Edit Format** button to edit the format of their values.
7. Select **OK**. Designer displays the [Elasticsearch Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010096501-Elasticsearch-Connection-Wizard-Dialog-Box).

   ![Elasticsearch Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/4404856972823/elstcschcnctnwzd_mdfy.gif)
8. In the **Modify Schema Properties** screen, Designer lists the elements in the Elasticsearch schema in the **Schema** box. You can select an element and modify its properties in the **Properties** box. Select **Next**.
9. In the **Transformed Relational Schema** screen, Designer lists the relational tables built based on the transformed relational schema structure. Check the transformed result in the **Transformed Tables** box, and then select **Next**.

   ![Elasticsearch Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/4404848580887/elstcschcnctnwzd_trnsfrmd.gif)
10. In the **Add Table** screen, add the required tables to the connection.

    ![Elasticsearch Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404856973079/elstcschcnctnwzd_adtbl.gif)

    You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views) using these tables and a report is developed from a query (or something else which is functionally similar) or from a business view.
11. Select **Finish** to confirm the transformed result and complete the transformation process.

## Adding More Tables to an Elasticsearch Connection

After you have created an Elasticsearch connection in a catalog, you can add more tables transformed from the Elasticsearch data source into the catalog via the connection.

1. Do one of the following:
   * Right-click the Elasticsearch connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the Elasticsearch connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the Elasticsearch connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the Elasticsearch connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the Elasticsearch connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   Designer displays the [Add Tables dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010095521-Add-Tables-Dialog-Box).

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857014039/addtbl_xml.gif)
2. Select the **Refresh** button.
3. Designer displays the tables in the schema that it transforms from the Elasticsearch data source in the **Tables** box. Choose the required tables and select **Add**.

   To choose consecutive tables, select the first table, press and hold down the **SHIFT** key, and then select the last table. To choose tables that are not consecutive, press and hold down **CTRL**, and then select each table.
4. After adding the required tables, select **Done** to close the dialog box.

## Managing the Tables in an Elasticsearch Connection

For the tables that have been transformed from an Elasticsearch data source and added into a catalog via an Elasticsearch connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/1500010057682-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057622-Connecting-via-Hive-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095301-Using-User-Defined-Data-Sources)
