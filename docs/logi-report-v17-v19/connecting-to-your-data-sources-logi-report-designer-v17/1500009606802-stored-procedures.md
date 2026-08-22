---
title: "Stored Procedures"
id: 1500009606802
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009606802-Stored-Procedures
updated_at: 2021-07-24T16:05:08Z
---

# Stored Procedures

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements)

# Stored Procedures

A stored procedure is a compiled program, consisting of one or more statements and is saved into a database. The statement in a stored procedure can be an SQL statement or a control flow statement, such as an If-else statement or a Loop statement. A stored procedure is stored in the DBMS, so that it can be called locally or remotely. In addition, a stored procedure can return a value, single result set or multiple result sets. Currently, Logi Report supports stored procedures that return a single result set. If a stored procedure returns more than one result set, the first one will be used by Logi Report.

As a program, a stored procedure can take parameters. There are three types of parameters: IN, OUT and INOUT. The IN parameter lets you pass values to the procedure. The OUT parameter returns values to the caller. The INOUT parameter enables you to pass initial values to the procedure, and then returns the updated value to the caller.

A stored procedure itself can be used to create page reports directly, and in this sense it functions the same as a [query](https://devnet.logianalytics.com/hc/en-us/articles/1500009613142-Queries). Therefore, you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009613182-Data-Manager) to control the data retrieval of stored procedures and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/1500009635961-Cached-Query-Results) for stored procedures the same as you do for queries. Stored procedures can also be used to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/1500009635921-Business-Views).

This topic includes the following sections:

* [Adding Stored Procedures to a Catalog](#Add)
* [Editing Parameter Values](#Parameter)
* [Updating Stored Procedures](#Update)
* [Converting the Data in Stored Procedures](#Convert)

## Adding Stored Procedures to a Catalog

To add procedures stored in the database to a catalog via a JDBC connection, take the following steps:

1. In the Catalog Manager resource tree, right-click the JDBC connection node and select **Add Stored Procedure** on the shortcut menu. The [Add Stored Procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009607142-Add-Stored-Procedures-Dialog) dialog appears.

   ![Add Stored Procedures dialog](https://devnet.logianalytics.com/hc/article_attachments/4404904399511/addprcdr.gif)
2. The dialog lists all the stored procedures in the Stored Procedures box in a three-level tree. The top level is SQL-catalog, the second is SQL-schema and the last level is stored procedures. Select the required stored procedures and select **Add** to add them to the catalog. You can also make use of the Sort button ![Sort button](https://devnet.logianalytics.com/hc/article_attachments/4404911593495/btn_sort2.gif) to display the stored procedures in the ascending or descending order for easy look-up, or the Search button ![Search button](https://devnet.logianalytics.com/hc/article_attachments/4404911593751/btn_srch.gif) to search for the required stored procedures.

   Note that not all DBMSs support database stored procedures. In this case, you may see nothing in the Stored Procedures box.
3. If any of the selected procedures contain parameters, the Stored Procedure Parameters dialog appears for you to specify the required values. These values will be saved inside the stored procedure object, and will be used as the default value when executing this procedure. You can edit the stored procedure parameters at any time. For details, see [Editing parameter values](#Parameter).
4. When finished, select the **Done** button to close the dialog.

When a stored procedure has been added into a catalog, Logi Report will in turn do the following:

* Retrieve the stored procedure's information from DBMS via JDBC.
* Prompt you to provide the values of IN and INOUT parameters if the stored procedure has them.
* Execute the stored procedure once in order to get the result set.
* Create the field objects of the procedure object according to the result set returned.

You will then be able to use the field objects to design your reports.

**Notes:**

* Not all stored procedures will return data usable by Logi Report. The stored procedure needs to return a result set.
* When adding a stored procedure, you may get the following error:

  [DBS-B]Could not find stored procedure 'test1;1'.

  This is because test;1 becomes quoted when Logi Report Designer finds the semicolon in it. To remove the quotation marks, you will have to modify your connection information. To do this:

  1. Right-click your JDBC connection and select **Edit Connection**  from the shortcut menu to bring out the Get JDBC Connection Information dialog.
  2. Select the **Qualified** tab, then in the Quote Qualifier box, select the **User Defined** radio button and remove all the characters from the Extra Characters and Quote Character text boxes.
  3. Select **OK** to confirm the settings.
* Due to the unique nature of Oracle stored procedures and EnterpriseDB stored procedures, you are unable to add them directly into a Logi Report Designer connection. As an alternative, Logi Report has developed the user data source API which can use a stored procedure in Oracle or EnterpriseDB. For details, see [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS) and [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/1500009629661-EnterpriseDB-Stored-Procedure-UDS). These user data source classes are included with Logi Report so you do not need to write any Java code yourself to use them.

## Editing Parameter Values

When you add a stored procedure that contains parameters, you will be asked to specify values for its parameters. These values will then be saved inside the stored procedure object in the catalog, and will be used as the default values when executing the stored procedure. You can edit stored procedure parameters at any time. Also, the IN type parameter is available for use with a stored procedure in a report the same as any other Logi Report parameter.

**To edit the parameter values of a stored procedure:**

1. Right-click the stored procedure and select **Parameters** on the shortcut menu. The [Stored Procedure Parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009633801-Stored-Procedure-Parameters-Dialog) dialog appears.

   ![Stored Procedure Parameters dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911681303/strdprcdrprm.gif)
2. This dialog lists all the IN and INOUT parameters in the stored procedures. double-click the **Value** cell to edit the value of each parameter.
3. Double-click the **Bind Parameter Name** cell to bind the IN and INOUT parameters in the stored procedure to an existing [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) or [constant level formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) of the same type predefined in the catalog data source in which the JDBC connection is created, or to the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName). You can type in the parameter/formula name as *@fieldname*; for the special field User Name as *username*. By default, the bound parameter will be the one with the same name of the IN and INOUT parameter which is automatically created when adding the stored procedure.
4. Select **OK** to apply the changes to the parameters.

## Updating Stored Procedures

If you make any changes to stored procedures in the database, you will need to update them in the connection so that the reports built on them can work properly.

1. Select any stored procedure, right-click it, and select **Update** on the shortcut menu. The [Update Procedures](https://devnet.logianalytics.com/hc/en-us/articles/1500009610782-Update-Procedures-Dialog) dialog appears.

   ![Update Procedures dialog](https://devnet.logianalytics.com/hc/article_attachments/4404911674647/updtprcdr.gif)
2. Select the stored procedures you want to update, and then select the **Update** button.
3. When finished, select the **Done** button to close the dialog.

## Converting the Data in Stored Procedures

Logi Report supports converting the data in stored procedures from one type to another before the data is passed to Logi Report. This assures that the row data in the database won't be affected. To do this, you will need to implement Logi Report interfaces and then Logi Report triggers your implementation to convert the data.

1. Write a class to extend jet.universe.plugin.ResultSetConvertor in JREngine.jar in `<install_root>\lib` and implement the abstract method:

   `public abstract ResultSet convert(final String catalogName, final String schemaName, final String procName,  
   final ResultSet rs);`

   There is a sample ResultSetConvertorImpl.java in `<install_root>\help\samples\APIConvertData` for your reference which is an example of converting String to Date and Time.
2. Compile the class into a .jar file.
3. Put the jar file in the jet.universe.customcolumn\_2.0.0 folder located in the `<install_root>\help\samples\APIConvertData` directory.
4. Modify the file plugin.xml located in the jet.universe.customcolumn\_2.0.0 folder as follows:
   * Change the following class to the real name of the class:  
     `<description class="ResultSetConvertorImpl"/>`
   * Change the following library name to the real name of the jar file:  
     `<library name="convertor.jar">`
5. Move the two folders jet.universe.addcolumn\_1.0.0 and jet.universe.customcolumn\_2.0.0 from the `<install_root>\help\samples\APIConvertData` directory to the `<install_root>\plugins` directory.
6. Start Logi Report Designer.

The conversion can also be done on Logi Report Server in the same way.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009629561-Tables-Views-Synonyms) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009606822-Creating-and-Importing-SQL-Statements)
