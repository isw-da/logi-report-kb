---
title: "Example 1: Adding a Flat File UDS"
id: 1500009585241
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585241-Example-1-Adding-a-Flat-File-UDS
updated_at: 2021-07-24T05:55:44Z
---

# Example 1: Adding a Flat File UDS

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585221-Adding-a-UDS-to-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS)

# Example 1: Adding a Flat File UDS

This topic demonstrates how to add a flat file UDS.

This example is a plain text file AddressesList.txt (available in `<install_root>\help\samples\APIUDS\txtUDS`), which contains data information in a table:

Laurena    Croft    34826 Atwood St.     New York City    NY    10004     USA...  
Jonathan    Hopkins    5062 Brandon Green Ave.     Minneapolis    MN    55402     USA...  
Jeremy    Miner    9283 Cherry Leaf Lane     Palo Alto    CA    94303     USA...  
....

You will notice that each line sequentially records the name, address, state, region, zip code, country, e-mail address and other information. In this example, you will be shown how to add a UDS using the data stored in a formatted text file. You can modify this example to meet your requirements.

Below is a list of the sections covered in this topic:

> * [Compiling and Running the Address UDS](#Compile)
> * [Adding the Address UDS to a Catalog](#Add)

## Compiling and Running the Address UDS

There are three classes used in this example and their source code are AddressListUDS.java, AddressListResultSet.java and AddressListResultSetMetaData.java. The data file is AddressesList.txt. All these files are available in `<install_root>\help\samples\APIUDS\txtUDS`.

If you use your own UDS classes, you must be sure that the class files can be found when running by making sure that the directory is classpath/package name. For this demo's UDS classes, the classes belong to a package named help. Copy the above necessary files to `<install_root>\help`, and add the additional entry to the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`.

For example, on Windows, if you installed Logi JReport Designer into the default directory `C:\Logi JReport\Designer`,

1. Copy the above necessary files to `C:\Logi JReport\Designer\help`.
2. Compile the Java files.

   `javac -classpath "C:\Logi JReport\Designer\lib\JREngine.jar" Address*.java`
3. Add the additional entry into the ADDCLASSPATH variable of setenv.bat in `C:\Logi JReport\Designer\bin`.

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\Logi JReport\Designer\help;`

## Adding the Address UDS to a Catalog

After compilation, you can now add the UDS to a Logi JReport catalog.

1. Start Logi JReport Designer with the batch file you just modified.
2. Open an existing catalog.
3. In the Catalog Manager resource tree, right-click the data source to which the UDS is to be added, then select **New****User Defined Data Source** from the shortcut menu.
4. In the New User Defined Data Source dialog, enter the required information:
   * **Name**: The name you want to use for identifying the UDS in Logi JReport. Here we use Address.
   * **Class Name**: The class name of the UDS. You can type one in or select Browse to select a class file. Here we use help.AddressListUDS.
   * **Parameter**: AddressesList.txt
5. Select **OK** to add the UDS.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585221-Adding-a-UDS-to-a-Catalog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS)
