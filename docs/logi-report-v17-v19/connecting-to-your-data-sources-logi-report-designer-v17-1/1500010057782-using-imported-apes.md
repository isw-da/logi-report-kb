---
title: "Using Imported APEs"
id: 1500010057782
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010057782-Using-Imported-APEs
updated_at: 2021-07-23T19:14:56Z
---

# Using Imported APEs

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057802-Working-with-MongoDB-Connections-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057622-Connecting-via-Hive-Connections)

# Using Imported APEs

For users who wish to write their own MongoDB aggregation pipeline expressions (APE), Designer enables them to put the expressions into JSON files (.json) and import the files into a catalog via the specified MongoDB connection. Designer can then load data from the MongoDB database by the aggregation pipeline expressions in the imported JSON files. This topic describes the syntax of the aggregation pipeline expressions Designer supports, how you can import JSON files that define APEs into a catalog via MongoDB connections and update the JSON files in the catalog.

Currently, Designer supports JSON files that contain only one aggregation pipeline expression. The imported JSON files can work similarly as [imported SQLs](https://devnet.logianalytics.com/hc/en-us/articles/1500010095181-Using-Imported-SQLs), for example, you can use imported APEs to build [queries](https://devnet.logianalytics.com/hc/en-us/articles/1500010062562-Working-with-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500010101021-Working-with-Business-Views), and create page reports directly.

This topic contains the following sections:

* [Creating the Aggregation Pipeline Expressions](#Expression)
* [Importing APEs from JSON Files into a Catalog](#Import)
* [Updating the JSON Files](#Update)

## Creating the Aggregation Pipeline Expressions

When you write aggregation pipeline expressions, you need to make sure they follow JSON format. You should mark the key and value pairs in an aggregation pipeline expression with double quotation marks (double quotation marks are not needed for a value whose data type is not String), and enclose them in a pair of square brackets. Moreover, when the data in the MongoDB database is of hierarchical structure, in order to get all detail data in the MongoDB databases, it is suggested that you add *$unwind* in the expression, then a tabular with all data records can be returned; otherwise, a hierarchical structure with partial data records is returned. For more information about the expression definition, see <https://docs.mongodb.com/manual/core/aggregation-pipeline/>.

The following is an example:

`[ {"$match" : { "CUSTOMERID" : { "$gt" : 10}}}, { "$project" : { "CUSTOMERNAME" : 1 , "COUNTRY" : 1 , "CUSTOMERID" : 1}}, { "$sort" : { "COUNTRY" : 1}} ]`

In an aggregation pipeline expression, you can use [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels#CLF) predefined in the current catalog data source in the format *@FieldName* or *?FieldName* to calculate your data. For example, if you need to get different result sets at runtime, you can [reference parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099741-Parameter-Application-Cases#FilterQuery) in the *$match* stage of the expression to dynamically filter the data. In the above example, if you want to use a parameter to return a result set in which the customer ID is greater than the parameter, then the *$match* stage would be like this:

`{"$match" : { "CUSTOMERID" : { "$gt" : @pID}}}`

Where, pID is a parameter and fID is a constant level formula created in the catalog.

Besides using parameters, you can also use the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" as *@username* in the *$match* stage of the aggregation pipeline expressions to filter data dynamically.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) When the [Scope of All Values](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog#AllScope) property of a parameter is set to "All Values in Database", you cannot use the parameter in aggregation pipeline expressions.

## Importing APEs from JSON Files into a Catalog

After you have set up the MongoDB connection and saved aggregation pipeline expressions in JSON files, you can import them into the catalog as follows:

1. In the Catalog Manager resource tree, right-click the MongoDB connection and select **Add APE** on the shortcut menu.
2. In the Select a JSON File dialog box, browse to the JSON file and select **Open**.
3. In the Enter Aggregation Pipeline Expression Information dialog box, type a name for the JSON file in the **Expression Name** text box, select the database and collection of the MongoDB database from which to get data in accordance with the aggregation pipeline expression in the selected JSON file. Select **OK**.

   ![Enter MongoDB Aggregation Pipeline Expression dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404857019671/cnctn_mngodb_entrape.gif)

   Designer then adds the JSON file under the **Imported APEs** node in the catalog resource tree. You can right-click it and select **Show APE** from the shortcut menu to view the aggregation pipeline expression in the JSON file if you want. Designer maintains the format of the JSON file, such as comments, when you add the file into the catalog.

   When you import a JSON file via the Data screen of the report wizard, you should also specify the MongoDB connection based on which to execute the aggregation pipeline expression in the selected JSON file from the Connection drop-down list.

## Updating the JSON Files

If you make any change to the aggregation pipeline expression in an JSON file, you need to update the JSON file in the catalog so that reports built based on the aggregation pipeline expression can work properly.

1. From the **Imported APEs** node in the catalog resource tree, select the JSON file, right-click it and select **Update** from the shortcut menu.
2. In the Select a JSON File dialog box, select the JSON file you want to update, then select **Open**.
3. In the Enter Aggregation Pipeline Expression Information dialog box, select the database and collection of the MongoDB database from which to get data in accordance with the aggregation pipeline expression in the selected JSON file.
4. Select **OK** to update the JSON file.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057802-Working-with-MongoDB-Connections-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057622-Connecting-via-Hive-Connections)
