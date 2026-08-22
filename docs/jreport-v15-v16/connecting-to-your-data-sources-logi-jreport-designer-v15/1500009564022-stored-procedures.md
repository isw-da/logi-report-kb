---
title: "Stored Procedures"
id: 1500009564022
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564022-Stored-Procedures
updated_at: 2021-07-24T05:55:50Z
---

# Stored Procedures

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584821-Tables-Views-Synonyms)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files)

# Stored Procedures

A stored procedure is a compiled program, consisting of one or more statements and is saved into a database. The statement in a stored procedure can be an SQL statement or a control flow statement, such as an If-else statement or a Loop statement. A stored procedure is stored in the DBMS, so that it can be called locally or remotely. In addition, a stored procedure can return a value, single result set or multiple result sets. Currently, Logi JReport supports stored procedures that return a single result set. If a stored procedure returns more than one result set, the first one will be used by Logi JReport.

As a program, a stored procedure can take parameters. There are three types of parameters: IN, OUT and INOUT. The IN parameter lets you pass values to the procedure. The OUT parameter returns values to the caller. The INOUT parameter enables you to pass initial values to the procedure, and then returns the updated value to the caller.

[Queries](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries) and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009562582-Business-Views) can be built on stored procedures and a report is developed from a query (or something else which is functionally similar) or from a business view.

A stored procedure itself can be used to create page reports directly, and in this sense it functions the same as a [query](https://devnet.logianalytics.com/hc/en-us/articles/1500009592441-Queries). Therefore, you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009592481-Data-Manager) to control the data retrieval of stored procedures, including the number of rows to be displayed and the duration allowed for the retrieval, and use the manager to keep access information from previous runs of a stored procedure. You can also create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results) for stored procedures and save the result files somewhere in your machine, then when you view reports based on the stored procedures, you can choose to use the data from the cached query result files as opposed to the database.

Below is a list of the sections covered in this topic:

> * [Adding Stored Procedures to a Catalog](#Add)
> * [Editing Parameter Values](#Parameter)
> * [Updating Stored Procedures](#Update)

## Adding Stored Procedures to a Catalog

To add procedures stored in the database to a catalog via a JDBC conn ection, take the following steps:

1. In the Catalog Manager resource tree, right-click the JDBC connection node and select **Add Stored Procedure** on the shortcut menu. The [Add Stored Procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009585581-Add-Stored-Procedures-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893959191/addprcdr.gif)
2. The dialog lists all the stored procedures in the Stored Procedures box in a three-level tree. The top level is SQL-catalog, the second is SQL-schema and the last level is stored procedures. Select the required stored procedures, and then select **Add**. However, not all DBMSs support database stored procedures. In this case, you may see nothing in the box.
3. If any of the selected procedures contain parameters, the Stored Procedure Parameters dialog appears for you to input the required values. These values will be saved inside the stored procedure object, and will be used as the default value when executing this procedure. You can edit the stored procedure parameters at any time. For details, see [Editing parameter values](#Parameter).
4. When finished, select the **Done** button to close the dialog.

When a stored procedure has been added into a catalog, Logi JReport will in turn do the following:

* Retrieve the stored procedure's information from DBMS via JDBC.
* Prompt you to provide the values of IN and INOUT parameters if the stored procedure has them.
* Execute the stored procedure once in order to get the result set.
* Create the field objects of the procedure object according to the result set returned.

You will then be able to use the field objects to design your reports.

**Notes:**

* Not all stored procedures will return data usable by Logi JReport. The stored procedure needs to return a result set.
* When adding a stored procedure, you may get the following error:

  [DBS-B]Could not find stored procedure 'test1;1'.

  This is because test;1 becomes quoted when Logi JReport Designer finds the semicolon in it. To remove the quotation marks, you will have to modify your connection information. To do this:

  1. Right-click your JDBC connection and select **Edit Connection**  from the shortcut menu to bring out the Get JDBC Connection Information dialog.
  2. Select the **Qualified** tab, then in the Quote Qualifier box, check the **User Defined** radio button and remove all the characters from the Extra Characters and Quote Character text boxes.
  3. Select **OK** to confirm the settings.
* Due to the unique nature of Oracle stored procedures and EnterpriseDB stored procedures, you are unable to add them directly into a Logi JReport Designer connection. As an alternative, Logi JReport has developed the user data source API which can use a stored procedure in Oracle or EnterpriseDB. For details, see [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009585301-Oracle-Stored-Procedure-UDS) and [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009564282-EnterpriseDB-Stored-Procedure-UDS). These user data source classes are included with Logi JReport so you do not need to write any Java code yourself to use them.

## Editing Parameter Values

When you add a stored procedure that contains parameters, you will be asked to input values for its parameters. These values will then be saved inside the stored procedure object in the catalog, and will be used as the default values when executing the stored procedure. You can edit stored procedure parameters at any time. Also, the IN type parameter is available for use with a stored procedure in a report the same as any other Logi JReport parameter.

**To edit the parameter values of a stored procedure:**

1. Right-click the stored procedure and select **Parameters** on the shortcut menu. The [Stored Procedure Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009567682-Stored-Procedure-Parameters-Dialog) dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404893852183/strdprcdrprm.gif)
2. This dialog lists all the IN and INOUT parameters in the stored procedures. Double-click the **Value** cell to edit the value of each parameter.
3. Double-click the **Bind Parameter Name** cell to bind the IN and INOUT parameters in the stored procedure to an existing [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590021-Parameters) or [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF) of the same type predefined in the catalog data source in which the JDBC connection is created, or to the special field User Name. You can input the parameter/formula name as @parametername/@formulaname, or the special field User Name as username. By default, the bound parameter will be the one with the same name of the IN and INOUT parameter which is automatically created when adding the stored procedure. If the special field User Name is bound, to specify the user name, go to **File** > **Options**, on the menu bar in the General category of the Options dialog, set the User Name option. This username only applies to running the report in Logi JReport Designer, when running the report on the server the real user's login ID will be used.
4. Select **OK** to apply the changes to the parameters.

## Updating Stored Procedures

If you make any changes to stored procedures in the database, you will need to update them in the connection so that the reports built on them will work properly. To do this:

1. Select any stored procedure, right-click it, and select **Update** on the shortcut menu. The [Update Procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009567842-Update-Procedures-Dialog) dialog appears.

   ![Update Procedures dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889313943/updtprcdr.gif)
2. Select the stored procedures you want to update, and then select the **Update** button.
3. When finished, select the **Done** button to close the dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584821-Tables-Views-Synonyms)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564042-Predefined-SQL-Files)
