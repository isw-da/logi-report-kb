---
title: "Using Stored Procedures"
id: 4405661423383
section: "Connecting to Your Data Sources - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405661423383-Using-Stored-Procedures
updated_at: 2022-01-27T20:34:39Z
---

# Using Stored Procedures

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs)

# Using Stored Procedures

This topic provides a brief introduction about using stored procedures in Designer, and describes how you can add stored procedures into a catalog via the JDBC connections you have set up and work with them in the catalog.

This topic contains the following sections:

* [Knowing Stored Procedures](#Know)
* [Adding Stored Procedures to a Catalog](#Add)
* [Editing Parameter Values](#Parameter)
* [Updating Stored Procedures](#Update)
* [Converting the Data in Stored Procedures](#Convert)

## Knowing Stored Procedures

A stored procedure is a compiled program, consisting of one or more statements and is saved into a database. The statement in a stored procedure can be an SQL statement or a control flow statement, such as an If-else statement or a Loop statement. A stored procedure is stored in the DBMS, so that it can be called locally or remotely. In addition, a stored procedure can return a value, single result set or multiple result sets. Currently, Logi Report supports stored procedures that return a single result set. If a stored procedure returns more than one result set, Logi Report uses the first one.

As a program, a stored procedure can take parameters. There are three types of parameters: IN, OUT, and INOUT. The IN parameter lets you pass values to the procedure. The OUT parameter returns values to the caller. The INOUT parameter enables you to pass initial values to the procedure, and then returns the updated value to the caller.

You can use a stored procedure to create page reports directly, and in this sense a stored procedure functions the same as a [query](https://devnet.logianalytics.com/hc/en-us/articles/4405661915543-Working-with-Queries). Therefore, you can use the [Data Manager](https://devnet.logianalytics.com/hc/en-us/articles/4405664684439-Managing-the-Data-Retrieval-of-Queries) to control the data retrieval of stored procedures and create [cached result files](https://devnet.logianalytics.com/hc/en-us/articles/4405664683031-Working-with-Cached-Query-Results) for stored procedures the same as you do for queries. You can also use stored procedures to build queries and [business views](https://devnet.logianalytics.com/hc/en-us/articles/4405664680215-Working-with-Business-Views).

However, due to the unique nature of Oracle stored procedures and EnterpriseDB stored procedures, you are unable to add them directly into a catalog. As an alternative, Logi Report has developed the User Data Source API which can use a stored procedure in Oracle or EnterpriseDB. For more information, see [Oracle Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/4405661438615-Oracle-Stored-Procedure-UDS) and [EnterpriseDB Stored Procedure UDS](https://devnet.logianalytics.com/hc/en-us/articles/4405661437591-EnterpriseDB-Stored-Procedure-UDS). Logi Report already includes these user data source classes so you do not need to write any Java code yourself to use them.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Not all stored procedures can return data usable by Designer. The stored procedure needs to return a result set.

## Adding Stored Procedures to a Catalog

To add procedures stored in the database to a catalog via a JDBC connection, take the following steps:

1. In the Catalog Manager resource tree, right-click the JDBC connection node and select **Add Stored Procedure** on the shortcut menu. Designer displays the [Add Stored Procedures dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661451543-Add-Stored-Procedures-Dialog-Box).

   ![Add Stored Procedures dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420550955799/addprcdr.gif)
2. From the **Database Catalog** drop-down list, select the catalog in the database which contains the stored procedures you need.
3. The **Stored Procedures** box lists all the stored procedures in the selected database catalog in a three-level tree. The top level is SQL-catalog, the second is SQL-schema, and the last level are stored procedures. Select the required stored procedures and select **Add** to add them to the catalog.

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) Not all DBMSs support database stored procedures. In this case, you may see nothing in the Stored Procedures box.
4. If any of the selected procedures contain parameters, Designer displays the Stored Procedure Parameters dialog box for you to specify the required values. Designer saves these values inside the stored procedure object, and uses them as the default values when executing this procedure. You can [edit the stored procedure parameters at any time](#Parameter).
5. Select **Done** to close the dialog box.

After you have added a stored procedure into a catalog, Designer in turn performs the following:

* Retrieving the stored procedure's information from DBMS via JDBC.
* Prompting you to provide the values of the IN and INOUT parameters if the stored procedure has them.
* Executing the stored procedure once in order to get the result set.
* Creating the field objects of the procedure object according to the result set returned.

You can then use the field objects to design reports.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420542072599/noteicon.jpg) When adding a stored procedure, you may get the following error:

[DBS-B]Could not find stored procedure 'test1;1'.

This is because test;1 becomes quoted when Designer finds the semicolon in it. To remove the quotation marks, you need to modify your connection information as follows:

1. Right-click your JDBC connection and select **Edit Connection**  from the shortcut menu. Designer displays the Get JDBC Connection Information dialog box.
2. Select the **Qualified** tab, then in the **Quote Qualifier** box, select **User Defined** and remove all the characters from the **Extra Characters** and **Quote Character** text boxes.
3. Select **OK** to confirm the settings.

## Editing Parameter Values

When you add a stored procedure that contains parameters, Designer prompts you to specify values for its parameters. Designer saves these values inside the stored procedure object in the catalog, and uses them as the default values when executing the stored procedure. You can edit stored procedure parameters at any time. Also, the IN type parameters of a stored procedure is available for use the same as any other Logi Report parameters.

**To edit the parameter values of a stored procedure**

1. Right-click the stored procedure and select **Parameters** on the shortcut menu. Designer displays the [Stored Procedure Parameters dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405664582039-Stored-Procedure-Parameters-Dialog-Box).

   ![Stored Procedure Parameters dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420542101271/strdprcdrprm.gif)
2. The dialog box lists all the IN and INOUT parameters in the stored procedure. Double-click the **Value** cell to edit the value of each parameter.
3. Double-click the **Bind Parameter Name** cell to bind the IN and INOUT parameters in the stored procedure to the existing [parameters](https://devnet.logianalytics.com/hc/en-us/articles/4405661800215-Working-with-Parameters) or [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/4405664602263-Formula-Levels#CLF) of the same type predefined in the catalog data source in which you have created the JDBC connection, or to the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/4405664402327-Working-with-Special-Fields#UserName)" (to bind to a parameter or formula, type the name of the parameter or formula in the cell; to bind to the special field "User Name", type *username* in the cell). By default, the bound parameter is the one with the same name of the IN/INOUT parameter that Designer automatically creates when you add the stored procedure.
4. Select **OK** to apply the changes to the parameters.

## Updating Stored Procedures

If you make any changes to stored procedures in the database, you need to update them in the catalog so that the reports built on them can work properly.

**To update the stored procedures added to a catalog**

1. Select any stored procedure, right-click it, and select **Update** on the shortcut menu. Designer displays the [Update Procedures dialog box](https://devnet.logianalytics.com/hc/en-us/articles/4405661743767-Update-Procedures-Dialog-Box).

   ![Update Procedures dialog box](https://devnet.logianalytics.com/hc/article_attachments/4420556229655/updtprcdr.gif)
2. Select the stored procedures you want to update, and then select **Update**.
3. Select **Done** to close the dialog box.

## Converting the Data in Stored Procedures

Logi Report supports converting the data in stored procedures from one type to another before the data is passed to Logi Report. This assures that the row data in the database is not affected. To do this, you need to implement Logi Report interfaces and then Logi Report triggers your implementation to convert the data.

1. Write a class to extend **jet.universe.plugin.ResultSetConvertor** in **JREngine.jar** in `<install_root>\lib` and implement the abstract method:

   `public abstract ResultSet convert(final String catalogName, final String schemaName, final String procName,  
   final ResultSet rs);`

   There is a sample **ResultSetConvertorImpl.java** in `<install_root>\help\samples\APIConvertData` for your reference. The sample converts String to Date and Time.
2. Compile the class into a .jar file.
3. Put the jar file in the **jet.universe.customcolumn\_2.0.0** folder located in the `<install_root>\help\samples\APIConvertData` directory.
4. Modify the file **plugin.xml** located in the jet.universe.customcolumn\_2.0.0 folder.
   * Change the class to the real name of the class: `<description class="ResultSetConvertorImpl"/>`
   * Change the library name to the real name of the jar file: `<library name="convertor.jar">`
5. Move the two folders **jet.universe.addcolumn\_1.0.0** and **jet.universe.customcolumn\_2.0.0** from the `<install_root>\help\samples\APIConvertData` directory to the `<install_root>\plugins` directory.
6. Start Designer to view the converted data.

You can also perform the conversion on Server in the same way.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420556069783/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405664414743-Using-Tables-Views-Synonyms)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420550802199/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661424407-Using-Imported-SQLs)
