---
title: "Accessing Data via Elasticsearch Connections"
id: 5735564552471
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735564552471-Accessing-Data-via-Elasticsearch-Connections
updated_at: 2022-11-02T04:28:54Z
---

# Accessing Data via Elasticsearch Connections

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735499410327-Accessing-Data-via-Hive-Connections)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521621399-Using-User-Defined-Data-Sources)

# Accessing Data via Elasticsearch Connections

An Elasticsearch connection contains relational data that is transformed from an Elasticsearch data source. This topic describes how you can set up Elasticsearch connections in a catalog, and add and manage tables transformed from the Elasticsearch data sources in the catalog via the connections.

This topic contains the following sections:

* [How Designer Gets Data from Elasticsearch Data Sources](#How)
* [Setting Up Elasticsearch Connections in a Catalog](#Set)
* [Adding More Tables to an Elasticsearch Connection](#Add)
* [Managing Tables in an Elasticsearch Connection](#Manage)

## How Designer Gets Data from Elasticsearch Data Sources

Designer gets data from Elasticsearch data sources in the same way as it gets data from [JSON data sources](https://devnet.logianalytics.com/hc/en-us/articles/5735512868119-How-Designer-Gets-Data-from-JSON-Data-Sources).

## Setting Up Elasticsearch Connections in a Catalog

To set up an Elasticsearch connection to connect a catalog to an Elasticsearch data source, take the following steps:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/5735563628951-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, do either of the following:
   * To set up the connection in an existing data source in the catalog, right-click the data source node and select **New Elasticsearch Connection** from the shortcut menu.
   * To set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **Elasticsearch** connection type and select **OK**.

   Designer displays the [Elasticsearch Data Source Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735508850583-Elasticsearch-Data-Source-Options-Dialog-Box).

   ![Elasticsearch Data Source Options dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898464443031/elstcschdtscoptn.gif)
3. Specify the URL, user name, and password with which to connect to the Elasticsearch data source.
4. To get data from the Elasticsearch data source by the request body, select **Use Request Body Search** and specify the request body. You can reference parameters and constant level formulas predefined in the catalog data source in which you create the Elasticsearch connection, and the special field "User Name" in the URL and the request body in the same way as in [aggregation pipeline expressions](https://devnet.logianalytics.com/hc/en-us/articles/5735512889367-Using-Imported-APEs#Expression).
5. To get data from the Elasticsearch data source by the Scroll API, select **Scroll** and specify how long the Scroll API will keep the search context alive. For more information about the Scroll API, see <https://www.elastic.co/guide/en/elasticsearch/reference/current/search-request-scroll.html>.
6. When you reference parameters and formulas in the URL or request body, you can select **Edit Format** to edit the format of their values.
7. Select **OK**. Designer displays the [Elasticsearch Connection Wizard dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735565764759-Elasticsearch-Connection-Wizard-Dialog-Box).

   ![Elasticsearch Connection Wizard - Modify Schema Properties](https://devnet.logianalytics.com/hc/article_attachments/9898517574039/elstcschcnctnwzd_mdfy.gif)
8. In the **Modify Schema Properties** screen, Designer displays the elements in the Elasticsearch schema in the **Schema** box. You can select an element and modify its [properties](https://devnet.logianalytics.com/hc/en-us/articles/5735532649367-JSON-Elasticsearch-Schema-Properties) in the **Properties** box.
9. Select **Next**. Designer displays the **Transformed Relational Schema** screen, showing the relational tables it builds based on the transformed relational schema structure.

   ![Elasticsearch Connection Wizard - Transformed Relational Schema](https://devnet.logianalytics.com/hc/article_attachments/9898533984535/elstcschcnctnwzd_trnsfrmd.gif)
10. Select **Next**. Designer displays the **Add Table** screen.

    ![Elasticsearch Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/9898533989271/elstcschcnctnwzd_adtbl.gif)
11. In the **Tables** box, select the tables you want to use in the connection and select **Add**![Add button](https://devnet.logianalytics.com/hc/article_attachments/9898405598999/btn_addarrow.gif) to add them to the **Added Tables** box. You can create [queries](https://devnet.logianalytics.com/hc/en-us/articles/5735547120407-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/5735547021975-Working-with-Business-Views) using these tables and then develop reports based on the queries and business views.
12. Select **Finish** to complete the transformation process.

## Adding More Tables to an Elasticsearch Connection

After you have created an Elasticsearch connection in a catalog, you can add more tables transformed from the Elasticsearch data source into the catalog via the connection.

**To add more tables to an existing Elasticsearch connection**

1. Do one of the following:
   * Right-click the Elasticsearch connection and select **Add Tables** from the shortcut menu.
   * Right-click the **Tables** node of the Elasticsearch connection and select **Add Tables** from the shortcut menu.
   * Right-click an existing table in the Elasticsearch connection if there is and select **Add Tables** from the shortcut menu.
   * Right-click any folder in the Tables node of the Elasticsearch connection if you have already created some and select **Add Tables** from the shortcut menu.
   * Select the **Tables** node of the Elasticsearch connection, or any existing table or folder in the connection and select **Add Tables** on the Catalog Manager toolbar.

   Designer displays the [Add Tables dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5735521826967-Add-Tables-Dialog-Box).

   ![Add Tables dialog box](https://devnet.logianalytics.com/hc/article_attachments/9898533418263/addtbl_xml.gif)
2. Select **Refresh**.
3. Designer displays the tables in the schema that it transforms from the Elasticsearch data source in the **Tables** box. Choose the required tables and select **Add**.
4. After adding the required tables, select **Done** to close the dialog box.

## Managing Tables in an Elasticsearch Connection

For the tables you have transformed from an Elasticsearch data source and added into a catalog via an Elasticsearch connection, you can [refresh them](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms#Refresh), [organize them into folders](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms#Folder), and [remove and add the table columns](https://devnet.logianalytics.com/hc/en-us/articles/5735521508887-Using-Tables-Views-Synonyms#Remove) the same as you do with tables from a JDBC database.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735499410327-Accessing-Data-via-Hive-Connections)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735521621399-Using-User-Defined-Data-Sources)
