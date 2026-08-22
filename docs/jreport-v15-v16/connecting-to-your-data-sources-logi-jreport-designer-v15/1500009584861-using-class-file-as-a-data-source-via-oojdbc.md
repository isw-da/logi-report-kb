---
title: "Using Class File as a Data Source via OOJDBC"
id: 1500009584861
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584861-Using-Class-File-as-a-Data-Source-via-OOJDBC
updated_at: 2021-07-24T05:55:49Z
---

# Using Class File as a Data Source via OOJDBC

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564082-Example-3-XML-File-with-Dynamic-Parameters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584881-Using-CSV-File-as-a-Data-Source-via-OOJDBC)

# Using Class File as a Data Source via OOJDBC

This topic demonstrates how to generate the ODF file in a different way using the file demo.zip in `<install_root>\help\samples\OOJDBC`, which contains all the necessary classes and methods needed for making the OOJDBC data source work with Java objects.

Below is a list of the sections covered in this topic:

> * [Preparations](#Preparation)
> * [Importing the Class File using the Model Wizard](#Wizard)
> * [Importing the ODF File into a Catalog](#Catalog)
> * [Improvement of OOJDBC in this Example](#Improvement)

## Preparations

Before the OOJDBC data source works with Java objects, you should do the preparations, which are detailed in the following two steps:

1. You should define a class that specifies the column name and the method of getting data from this column. In this example, the class Products.java in demo.zip takes this role. This class file contains the method public int getProductID(), which implies that the column name is ProductID and you can get the product ID via this method.
2. You should publish a method to access a group of products. That means OOJDBC needs a result set with multiple rows, and each row is one of the products, so that you should define a class that can retrieve the rows. In this example, the file SQLReader.java in demo.zip takes this role. In this file, there is a static\* method JCollection execSQL(String jdbcDriver, String url, String sql), and this method returns a collection that contains the rows of the products. This collection class is com.jinfonet.jdbc.obj.JCollection.

Also, the batch files used to start the Model Wizard, Logi JReport Designer and Logi JReport Server should be modified before you can import the product table and use it to generate reports. To do this:

1. Save demo.zip in `<install_root>\help`.
2. Add it to the class path of the batch file setenv.bat in `<install_root>\bin` of both Designer and Server. setenv.bat updates the class path for both ModelWizard and Designer.

## Importing the Class File using the Model Wizard

To import the class file using the Model Wizard, take the following steps:

1. Run ModelWizard.bat in `<install_root>\bin` to open the Object Source Wizard.
2. Select **Add Table** and the Add Table dialog will be displayed.
3. In the ClassName field, type **com.jinfonet.jdbc.demo.Products**, input **demo** in the Table Name field, and then select the **Parse** button.
4. Select **Direct Access Path**. In the Access Method dialog, input **com.jinfonet.jdbc.demo.SQLReader** in the Root Class Name field. Then select the **Parse** button. In the Methods box, select the method **execSQL**, and in the Parameters box, fill in the default values as follows:

   Param0 (the driver of the database): org.hsqldb.jdbcDriver  
    Param1 (the connection URL of the database): `jdbc:hsqldb:c:\Logi JReport\Designer\Demo\db\JRDemo`  
    Param2 (the user name): sa  
    Param3 (the password): (no value)  
    Param4 (the SQL statement): select \* from products
5. Press the **OK** button and the table demo will now have been added.
6. In the Object Source Wizard, select **File** > **Save**. You will then be prompted to save the ODF file. You should save it to `<install_root>\lib` or the directory where the catalog will be. Here we save it as demo.odf.

**Note:** The same ODF file cannot exist in both `<install_root>\lib` and the directory where the catalog is located.

## Importing the ODF File into a Catalog

To import the ODF file to a Logi JReport catalog, take the following steps:

1. Start Logi JReport Designer.
2. Select **File** > **New Catalog**.
3. In the Catalog Name dialog, specify the catalog name, the data source name and the path. The catalog should be located in the directory where you saved the ODF file. For example, if you saved the ODF file in `C:\odf`, the new catalog should be created also in `C:\odf`.
4. In the Catalog Manager, right-click the node of a data source and select **New JDBC Connection** from the shortcut menu. Select **JDBC** in the Select Connection Type dialog.
5. In the Get JDBC Connection Information dialog, enter **com.jinfonet.jdbc.obj.ObjectDriver** in the Driver text field, type **jdbc:jinfonet:object:@Filename** in the URL text field. @Filename should be the .odf name you have saved but do not include the extension. So in the example, it should be jdbc:jinfonet:object:@demo.
6. Select **OK** to set up the connection.
7. In the Add Tables dialog, select the table **demo** and select **Add**.
8. Select **Done** to close the Add Tables dialog.

Now, the table demo has been added into the catalog. You can use it to develop reports as required.

**Note:** When you publish the catalog and its reports to Logi JReport Server, whether the ODF file is located in `<install_root>\lib` or in the directory where the catalog is located, it will be published to the path where the catalog is located on the server side.

## Improvement of OOJDBC in this Example

Logi JReport provides an interface com.jinfonet.interfaces.query.TableFilter and a simple implementation com.jinfonet.jdbc.obj.TableFilterImpl, which can be used in this example to improve the performance of the select and WHERE clauses in a query. You can extend TableFilterImpl to create your own Reader class. In addition, a demo FilterSQLReader.java in the file demo.zip has been made for your reference.

**Note:** If you are using FilterSQLReader.java instead of SQLReader.java, you should input com.jinfonet.jdbc.demo.FilterSQLReader in the Root Class Name field of the Access Method dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564082-Example-3-XML-File-with-Dynamic-Parameters)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584881-Using-CSV-File-as-a-Data-Source-via-OOJDBC)
