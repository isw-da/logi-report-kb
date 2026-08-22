---
title: "Adding User Defined Data Sources to a Catalog"
id: 1500009607002
section: "Connecting to Your Data Sources - Logi Report Designer v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009607002-Adding-User-Defined-Data-Sources-to-a-Catalog
updated_at: 2021-12-31T02:41:23Z
---

# Adding User Defined Data Sources to a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS)

# Adding User Defined Data Sources to a Catalog

Logi Report Designer can access data from an external user defined data source, such as a Text file, or Excel file, which is not stored in a database, or when there is no JDBC driver available.

This topic includes the following sections:

* [Adding a UDS to a Catalog](#Add)
* [Example 1: Adding a Flat File UDS](#Example1)
* [Example 2: Adding an SQL Data Source UDS](#Example2)
* [Example 3: Adding a Java Object Data Source UDS](#Example3)
  + [Demo 1: Using a Simple Java Object UDS](#Demo1)
  + [Demo 2: Using a Java Object UDS with Multi-levels of Collections](#Demo2)
* [Example 4: Adding a Dynamic UDS](#Example4)

## Adding a UDS to a Catalog

The general steps to add a UDS to a Logi Report catalog are as follows:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009628301-Creating-Opening-and-Saving-Catalogs#Open), then in the Catalog Manager, right-click the node of a data source and choose **New User Defined Data Source** from the shortcut menu.

   If you want to add the UDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **User Defined** connection type and select **OK**.

   The [New User Defined Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009609402-New-User-Defined-Data-Source-Dialog) dialog appears.

   ![Add User Defined Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404916781207/nwuds.gif)
2. In the Name field, specify a name for the UDS as required.
3. Provide the class name with package name in the Class Name field. You can also select **Browse** to find the class file. The class you specify must exist and can be found by Logi Report Designer, which means the class should be in the class path of the system environment or set in ADDCLASSPATH of setenv.bat/setenv.sh. After filling in this field, the class name of the interface that the class implements will be displayed automatically behind The class implements:.
4. Specify the parameter for the UDS in the Parameter box. The PARAMETER string must match the format defined in the [UDS class](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API#ParamString).

   You can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500009611462-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009611142-Formula-Levels#CLF) predefined in the current catalog data source in the format *@FieldName* and the special field [User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500009606442-Special-Fields#UserName) as *@username* in the PARAMETER string. For example, if the PARAMETER string of a UDS is `SQL=select * from employee`, and you want to use the predefined parameter p\_sql to replace the part after "=", then the PARAMETER string will be `SQL=@p_sql`.
5. When parameters and formulas are referenced in the PARAMETER string, you can select the **Edit Format** button to edit the format of their values.
6. Select the **Specify Columns** option to enable the column definitions list and add column definitions. If you don't specify the column definitions, Logi Report will get them from the result set automatically.
   * **Name**  
     The name of a column. It should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
   * **SQLType**  
     The data type of the column.
   * **Precision**, **Length**, **Scale**, **Radix**  
     The default value for each SQL type. You can select the cell and modify the value.
   * **Nullable**  
     Indicates whether the value of the column can be null. X stands for NoNulls, √ stands for Nullable and ? stands for Nullable Unknown.
7. Select **OK** to add the UDS.

## Example 1: Adding a Flat File UDS

There are three classes used in this example and their source code are AddressListUDS.java, AddressListResultSet.java and AddressListResultSetMetaData.java. The data file is AddressesList.txt. All these files are available in `<install_root>\help\samples\APIUDS\txtUDS`.

AddressesList.txt is a plain text file which contains data information in a table:

Laurena    Croft    34826 Atwood St.     New York City    NY    10004     USA...  
Jonathan    Hopkins    5062 Brandon Green Ave.     Minneapolis    MN    55402     USA...  
Jeremy    Miner    9283 Cherry Leaf Lane     Palo Alto    CA    94303     USA...  
....

You can notice that each line sequentially records the name, address, state, region, zip code, country, e-mail address and other information.

If you use your own UDS classes, you must be sure that the class files can be found when running by making sure that the directory is classpath/package name. For this demo's UDS classes, the classes belong to a package named help. Copy the above necessary files to `<install_root>\help`, and add the additional entry to the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`.

**Task 1: Compile and run the Address UDS**

For example, on Windows, if you installed Logi Report Designer into the default directory `C:\LogiReport\Designer`,

1. Copy the above necessary files to `C:\LogiReport\Designer\help`.
2. Compile the Java files.

   `javac -classpath "C:\LogiReport\Designer\lib\JREngine.jar" Address*.java`
3. Add the additional entry into the ADDCLASSPATH variable of setenv.bat in `C:\LogiReport\Designer\bin`.

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\LogiReport\Designer\help;`

**Task 2: Add the Address UDS to a catalog**

After compilation, you can now add the UDS to a Logi Report catalog.

1. Start Logi Report Designer with the batch file you just modified.
2. Open an existing catalog.
3. In the Catalog Manager resource tree, right-click the data source to which the UDS is to be added, then select **New****User Defined Data Source** from the shortcut menu.
4. In the New User Defined Data Source dialog, specify the required information:
   * **Name**: The name you want to use for identifying the UDS in Logi Report. Here we use Address.
   * **Class Name**: The class name of the UDS. You can type one in or select Browse to select a class file. Here we use help.AddressListUDS.
   * **Parameter**: AddressesList.txt
5. Select **OK** to add the UDS.

## Example 2: Adding an SQL Data Source UDS

This is a fairly complex example, which executes an SQL statement and returns a result set through the JDBC API.

See the Java code for class definition below:

```
import jet.datasource.*;  
  
public class SQLDataSource implements JRUserDataSource {  
    // Define data.  
    public ResultSet getResultSet(String param)  
            throws JRUserDataSourceException {  
        // Method body.  
    }  
    /**  
    * Free the resources such as: Connection, Statement, ResultSet.  
    */  
    public void releaseResultSet() throws JRUserDataSourceException {  
        // Method body.  
    }  
}
```

The following explains the above code.

* The format of the String variable parameter is DRIVER=driver&URL=url&USER=user&PSWD=password&SQL=sql.

  For example, we used HSQL DB as the data source, and `C:\LogiReport\Designer\Demo\db\JRDemo` as the hsql db path; "sa" as the user's name, "" as the password, and `Select * from authors` as the SQL string. The parameter string may be similar to:

  `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\LogiReport\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=select * from employee`

  If you want to use predefined parameters in the Logi Report catalog, you can type the parameter string as:

  `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\LogiReport\\Designer\\Demo\\db\\JRDemo"&USER=@un&PSWD=&SQL=@sql`

  Where, @sql is a parameter predefined in the catalog, and its default value is "select \* from employee".

  **Note:** Every time when running, java.sql.Resultset must return the same metadata (UDS fields), including the number and order of fields, and the field properties such as column name, SQL type, precision, scale, nullable, currency, and array.
* The method *getResultSet()* parses the parameter string, builds a connection to the URL, and then executes the SQL statement.
* The method *releaseResultSet()* releases the resource such as Connection, Statement, and ResultSet.

**Task 1: Compile and run SQLDataSource**

There is one class used in this example and its source code is SQLDataSource.java, which is available in `<install_root>\help\samples\APIUDS\sqlUDS`. In this example, SQLDataSource will return the result set from demo hsql db. You should set up the HSQL DB path in the URL string and point it to the demo database at `<install_root>\Demo\db\JRDemo`.

Copy SQLDataSource.java to `<install_root>\help`, and compile it to generate SQLDataSource.class. Append the path `<install_root>\help` to the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`, so that SQLDataSource can be found at runtime.

**Task 2: Add the SQLDataSource UDS to a catalog**

After compilation, you can now add the UDS to a Logi Report catalog.

1. Start Logi Report Designer with the batch file you just modified.
2. Open an existing catalog.
3. In the Catalog Manager resource tree, right-click the data source to which the UDS is to be added, then select **New****User Defined Data Source** from the shortcut menu.
4. In the New User Defined Data Source dialog, specify the required information.

   If you select the Specify Columns option, the column definitions list will be enabled and you can add column definitions. If you don't specify column definitions, Logi Report will obtain them from the result set automatically. Here, we will not specify column definitions. Instead, we will use the default ones from the ResultSet and the ResultSetMetaData.

   Type **employees** in the Name text box and **SQLDataSource** in the Class Name text box. In the Parameter box, type:

   `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\LogiReport\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=select * from employee`

   Make sure that the five bold parts in the above line are capitalized.
5. Select **OK** to add the UDS.

## Example 3: Adding a Java Object Data Source UDS

The Logi Report Designer UDS can use any Java object as a data source for you to create reports. To implement this function, Logi Report Designer provides a class UDSForJavaBean, in which the method *getResultSet()* creates instances for the interface JavaBeanDataProvider, and then uses the method *init()* to initialize the data of the created instances.

See the Java code for class definition below:

```
public class UDSForJavaBean implements JRUserDataSource
{  
    // Define data.  
    public ResultSet getResultSet(String param)  
            throws JRUserDataSourceException   
    {  
        	// Method body.  
    }  
  
    /**  
    * Free the resources such as : Connection, Statement, ResultSet.  
     */  
    public void releaseResultSet() throws JRUserDataSourceException  
    {  
            // Method body.  
    }  
}
```

The interface JavaBeanDataProvider is defined as follows:

```
public interface JavaBeanDataProvider  
{  
    public void init(String dataID, Properties initprops)  
         throws JavaBeanDataProviderException;  
    public Class getMetadataJavaBean()  
        throws ClassNotFoundException;  
    public Object next() throws JavaBeanDataProviderException;  
    public boolean requireDetails(String collectionPropName);  
    public int getMaxShareTimes(String collectionPropName);  
    public int getTimeoutForSubCollection(String collectionPropName);  
    public void exit()throws JavaBeanDataProviderException;  
}
```

For examples of how to use the Java object data interface, Logi Report provides you with two demos which are available in `<install_root>\help\samples\APIUDS\javaUDS`.

* [Demo 1: Using a Simple Java Object UDS](#Demo1)
* [Demo 2: Using a Java Object UDS with Multi-levels of Collections](#Demo2)

Before running the demos, you need to do the following:

1. Copy all the content in `<install_root>\help\samples\APIUDS\javaUDS` to `<install_root>\help\UDSForJavaBean`. You need to create the UDSForJavaBean directory.
2. Compile all the java files.

   `javac -classpath <install_root>\help\UDSForJavaBean;<install_root>\lib\JREngine.jar;<install_root>\lib\log4j-core-2.12.1.jar;<install_root>\lib\log4j-api-2.12.1.jar; <install_root>\help\UDSForJavaBean\jreport\uds\javabean\*.java`
3. Copy data.txt in `<install_root>\help\UDSForJavaBean` to `<install_root>\bin`.
4. Add the path `<install_root>\help\UDSForJavaBean` in the ADDCLASSPATH variable in setenv.bat in the `<install_root>\bin` directory.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

### Demo 1: Using a Simple Java Object UDS

In this demo, a Java object named Person will be used as the data source, you can find the person.java file in `<install_root>\help\UDSForJavaBean\jreport\uds\javabean\beans`. It is defined as follows:

```
public class Person implements Serializable  
    {  
    private String gender;  
    private String ssn;  
    private String emailAddress;  
    private Date birthDate;  
    private Long newbornWeight;  
    private YesNo isDataVerified;  
    private Name name;  
    private Address currentMailingAddress;  
    private Phone currentWorkPhone;n;  
/**  
* @return the birthDate.  
*/  
public Date getBirthDate()  
    {  
    return birthDate;  
    }  
}
```

Similar to the code above, other attributes of the Person object are defined by other Java objects, such as currentMailingAddress which is defined by the Address class.

**To create a report from the Person Java object**:

1. [Make the necessary preparations](#Preparation).
2. In Logi Report Designer, open an existing catalog, then in the Catalog Manager, expand the data source to which the UDS is to be added.
3. This demo uses generated data, in order to get the real collection of the data objects, create two parameters before importing the Person Java object as follows:
   * **Name**: pUseFakeData (Specify whether to use generated data when running the report.)  
     **Value Type**: Boolean   
     **Prompt Value**: True
   * **Name**: pNumOfFakeData (Specify the number of data records to generate that will be shown when running the report.)  
     **Value Type**: Integer  
     **Prompt Value**: Any integer number

   For details about how to create parameters, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog).
4. Right-click the data source node, and select **New User Defined Data Source** from the shortcut menu.
5. In the New User Defined Data Source dialog, type **Person** in the Name text box.
6. For the Class Name field, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\jreport\uds\javabean`, and then choose **UDSForJavaBean.class**, which will import the class jreport.uds.javabean.beans.Person with full class name.
7. In the Parameter box, type in the following string:

   `JavaBeanDS_DataProvider=jreport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=persions&GBeanProvider_BeanClsName=jreport.uds.javabean.beans.Person&GBeanProvider_UseFakeData=true&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_RptDataInitializer=jreport.uds.javabean.SubRptCollectionDataInitializer`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **JavaBeanDS\_DataProvider** is used to specify the Java class which implements jreport.uds.javabean.JavaBeanDataProvider interface, and will return the list of required data objects at runtime. In this demo, it is a list of Person objects.
   * **JavaBeanDS\_RuntimeDataID** is a reserved value used as a key to get data objects from the DataCenter.
   * **GBeanProvider\_\*** are required values for the special data provider, jreport.uds.javabean.GenericBeanDataProvider, which is specified by JavaBeanDS\_DataProvider.

   You can use this provider (jreport.uds.javabean.GenericBeanDataProvider) or create your own provider by implementing the interface jreport.uds.javabean.JavaBeanDataProvider.
8. Select **OK** to add the UDS.
9. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page) which is based on this UDS.
10. Select the **View** tab to run the report. In the Enter Parameter Values dialog, type **3** as the value of the parameter pNumOfFakeData, and select **OK**. Three records will be returned. However, the data you get now is the generated data, because in the parameter string of the UDS, you have specified the value of the key word GBeanProvider\_UseFakeData to true.
11. In order to get the real collection of data objects, the parameter pUseFakeData will be used to control the value of the key GBeanProvider\_UseFakeData value dynamically as follows.

    In the Catalog Manager, right-click the UDS **Person** and select **Edit User Defined Data Source** on the shortcut menu. In the Edit User Defined Data Source dialog, modify the value of GBeanProvider\_UseFakeData to **@pUseFakeData** in the Parameter box.
12. Run the report again and specify the value of pUseFakeData as **false** to get the real collection of data at runtime.

    **Note:** The key word GBeanProvider\_RptDataInitializer in the data provider jreport.uds.javabean.GenericBeanDataProvider is used to specify the Java class name which implements jreport.uds.javabean.RptDataInitializer interface. So if you are using the data provider jreport.uds.javabean.GenericBeanDataProvider, you just need to provide a class which implements jreport.uds.javabean.RptDataInitializer to return a collection, list, or array of the data objects according to different reports and parameters. Also, jreport.uds.javabean.GenericBeanDataProvider can recognize vector, collection and array of objects and retrieve the objects inside of the collection one by one.

**Methods in the demo**

* **jreport.uds.javabean.GenericBeanDataProvider**  
  jreport.uds.javabean.GenericBeanDataProvider implements the interface of jreport.uds.javabean.JavaBeanDataProvider by using the following methods:

  public void init(String dataID, Properties initprops) throws JavaBeanDataProviderException;  
  public Class getMetadataJavaBean() throws ClassNotFoundException;  
  public Object next() throws JavaBeanDataProviderException;  
  public boolean requireDetails(String collectionPropName);  
  public int getMaxShareTimes(String collectionPropName);  
  public void exit()throws JavaBeanDataProviderException;

  + **init()**  
    This method is called by UDSForJavaBean to ask the data provider to prepare the data collection/list by the given initProperties. Basically, the initProperties are the name and value pairs parsed from the UDS parameter string.  

    For example, the GenericBeanDataProvider will get the list of properties with the following keys:

    JavaBeanDS\_DataProvider  
    JavaBeanDS\_RuntimeDataID  
    GBeanProvider\_BeanClsName  
    GBeanProvider\_UseFakeData  
    GBeanProvider\_NumOfFakeData  
    GBeanProvider\_RptDataInitializer

    The values for those keys will be used by GenericBeanDataProvider to prepare the data collection. For example, if the value of GBeanProvider\_UseFakeData is true, the GeneridBeanDataProvider will use the fake data, otherwise it will create an instance by the class name provided by GBeanProvider\_RptDataInitializer and ask the data initializer object to return the collection of data objects.
  + **getMetadataJavaBean()**  
    This method is called back from the UDS to get the bean class in order to construct the metadata for UDS. For GenericBeanDataProvider, the Java bean class in the collection is passed in by the key GBeanProvider\_BeanClsName when you define this data source by UDS.
  + **next()**  
    This method is called back from the UDS to fetch the next data object as a record for the report at runtime. For GenericBeanDataProvider, the method *init()* constructs the data object collection, and the method *next()* is going to check if the collection is a Vector, Collection, or array of objects to determine automatically how to get the next object from the constructed collection.
  + **exit()**  
    This method is called back from the UDS when Logi Report Engine closes the result set returned by UDS. For GenericBeanDataProvider, it will call the data initializer to close if the data is constructed by data initializer.
  + **requireDetails()**  
    This method is called back by the UDS to check if a certain collection attribute from Java bean needs to be displayed in the metadata.
  + **getMaxShareTimes()**  
    The sub-collection attribute from the Java data object could be shared among subreports. This is the call-back method from the UDS to determine the maximum number of times that a certain sub-collection object is going to be shared by the current report. If your report is trying to share the same sub-collection of a Java data object more than this specified value, you will get an error at runtime. However, if your report actually needs to be shared less than the number specified, the data will stay in the buffer without being cleaned.
* **jreport.uds.javabean.RptDataInitializer**  
  The implementation of this interface will be used by GenericBeanDataProvider to provide the collection of Java objects for different reports and parameters.

  The following methods need to be implemented for this interface:

  public Object getDataCollection(Properties props)throws RptDataInitializerException;  
  public void close();

  + **getDataCollection()**  
    This method is called by GenericBeanDataProvider to return the data collection object. The input props are passed down from GenericBeanDataProvider and includes all the values passed down into the *init()* method of the GenericBeanDataProvider.
  + **close()**  
    This method is called back by GenericBeanDataProvider when the *exit()* function is called there.

### Demo 2: Using a Java Object UDS with Multi-levels of Collections

Sometimes, the attributes of a Java object are defined by other lists/collections, such as the Java object SimpleBeanTest in `<install_root>\help\UDSForJavaBean\jreport\uds\javabean\beans`. It is defined as follows:

```
public class SimpleBeanTest implements Serializable {  
    private String test;  
    private long l;  
    private int i;  
    private int[] intarray;  
    private Person[] persons;  
    private Collection addresses;  
    private Date dMyDate;  
}
```

From the code above, you can see that the Java class SimpleTestBean contains an array of Persons, a collection of addresses and an array of Int values.

For this kind of Java object, Logi Report Designer can create a report that gets records from the SimpleTestBean, but it cannot show the list of persons information in the same report. If you want to create such a report - each record comes from the SimpleBeanTest object, and for each record, display the list of persons information - you have to use a primary report and subreport to implement this function.

**Task 1: Create the primary report**

1. [Make the necessary preparations](#Preparation).
2. In Logi Report Designer, open an existing catalog, then in the Catalog Manager, expand the data source to which the UDS is to be added.
3. [Create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog) as follows, which is used to specify the number of data records to generate that will be shown when running the report.

   **Name**: pNumOfFakeData  
   **Value Type**: Integer  
   **Prompt Value**: Any integer number. Note that the parameter must have at least one value that is larger than 0, otherwise you will get exceptions when viewing reports.
4. Right-click the data source node and select **New User Defined Data Source** on the shortcut menu. The New User Defined Data Source dialog appears.
5. Type **SimpleTestBean** in the Name text box.
6. For the Class Name filed, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\jreport\uds\javabean`, and then choose **UDSForJavaBean.class**. The UDS class UDSForJavaBean.class will import the class jreport.uds.javabean.beans.SimpleTestBean with full class name.
7. In the Parameter box, type in the following string:

   `JavaBeanDS_DataProvider=jreport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=&GBeanProvider_BeanClsName=jreport.uds.javabean.beans.SimpleBeanTest&GBeanProvider_UseFakeData=true&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_FakeDateSubCollectionInfo=persons,jreport.uds.javabean.beans.Person&GBeanProvider_RptDataInitializer=&GBeanProvider_ListOfDetailProps=persons,1,30000`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **GBeanProvider\_ListOfDetailProps** specifies the following items:
     + The list of property names of sub-collections that will be displayed in the meta-data
     + How many times that this report is going to share the sub-collection per main object
     + The timeout for the shared data in the DataCenter in milliseconds (the default value is 1 minute).

     In this demo, only the sub-collection property persons will be imported from the SimpleTestBean class, and the share time is 1. If you want to create another subreport using addresses, you have to specify the value for this keyword as follows:

     `=&GBeanProvider_ListOfDetailProps=persons,1,30000$addresses,1,30000`

     and different properties are separated by the symbol $.
   * **GBeanProvider\_FakeDateSubCollectionInfo**  
     The value of this key word is used to construct the fake data for SimpleTestBean collections. Each Java class can have multiple sub-collection objects, and it is allowed to not construct the values of these sub-collection objects if you do not want to use it. However, if you do not specify them here in this parameter string as `<property name>,<property class name>$<property name>,<property class name>`, the fake data for those sub-collections will not be constructed, and problems will occur when running the report on fake data.
8. Select **OK** and the UDS SimpleTestBean is added. In the Catalog Manager, you will see that persons appears in the resource tree in the SimpleTestBean node.
9. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page) named MainRpt.cls, with a standard banded object in it as the primary report based on the UDS SimpleTestBean.

**Task 2: Create the subreport**

1. Expand the data source in the catalog to which you want to add the UDS for the subreport.
2. Create a parameter as follows, which is used to specify whether to use generated data when running the report.

   **Name**: pUseFakeData  
   **Value Type**: Boolean   
   **Prompt Value**: True
3. Create another parameter named pRunTimeDataInfo of String type, which will be used when setting up the link between the primary report and the subreport.

   **Name**: pRunTimeDataInfo  
   **Value Type**: String   
   **Prompt Value**: persons
4. Right-click the data source node and select **New User Defined Data Source** on the shortcut menu. The New User Defined Data Source dialog appears.
5. Type **PersonsAsSubRpt** in the Name text box.
6. For the Class Name text box, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\jreport\uds\javabean`, and then choose **UDSForJavaBean.class**.
7. In the Parameter box, type in the following string:

   `JavaBeanDS_DataProvider=jreport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=@pRunTimeDataInfo&GBeanProvider_BeanClsName=jreport.uds.javabean.beans.Person&GBeanProvider_UseFakeData=@pUseFakeData&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_RptDataInitializer=jreport.uds.javabean.SubRptCollectionDataInitializer`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **JavaBeanDS\_RuntimeDataID** is defined to use a parameter which will be the link point from the subreport to the sub-collections in the primary report.
   * **GBeanProvider\_RptDataInitializer**'s value is jreport.uds.javabean.SubRptCollectionDataInitializer, which is our built-in data provider set up especially for the subreport to return the collection of data by referencing the sub-collection in the primary report. The referencing information is passed via the parameter value @pRunTimeDataInfo which will be used when we set up the link between the primary report and the subreport.
   * The class name for GBeanProvider\_BeanClsName is Person because the subreport will use the Person object.
8. Select **OK**, and the UDS PersonsAsSubRpt is added.
9. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009613262-Creating-Reports#Page) named SubRpt.cls, with a table in it as the subreport based on the UDS PersonsAsSubRpt.

**Task 3: Link the primary report and the subreport**

1. In the Catalog Manager, [create a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009634201-Creating-Formulas-in-a-Catalog) named NotUseFakeData to return false all the time, for example, `return false`. This formula will be passed into the subreport as the value of the parameter pUseFakeData in the subreport, so that when the subreport runs with the primary report, it will always use the data from the primary report instead of constructing the fake data itself.
2. Open MainRpt.cls, add a new detail panel into the report.
3. Selected the newly added panel and select **Insert** > **Subreport**. When a box attached to your mouse pointer, select in the panel and the Subreport dialog is displayed.
4. Select the **Browse** button, choose **SubRpt.cls** as the subreport, then in the Parameters tab, specify values for the parameters as follows:

   | Parameter | Value |
   | --- | --- |
   | pNumOfFakeData | pNumOfFakeData |
   | pUseFakeData | NotUseFakeData (gives a false value to the parameter) |
   | pRunTimeDataInfo | persons (specifies to use the sub-collection persons of the primary report as the data source of the subreport at runtime) |
5. Select **OK** to insert the subreport. For more information about using subreports, see [Subreports](https://devnet.logianalytics.com/hc/en-us/articles/1500009606422-Subreports).
6. Run the primary report, and you will find that the corresponding persons information is displayed in the subreport.
7. If you want to insert another subreport which shares the same sub-collection with SubRpt.cls, you should modify the value of the key word GBeanProvider\_ListOfDetailProps in the primary report UDS parameter string to GBeanProvider\_ListOfDetailProps=persons,2,30000. That changes the share amount of the persons property from 1 to 2.

## Example 4: Adding a Dynamic UDS

Logi Report Designer supports the Dynamic UDS feature. This feature improves performance by retrieving only the selected fields and not all the fields. At runtime, an option is provided for you to pick up the columns you want to see in the report. In this way, Logi Report Designer generates a dynamic report according to your selection.

In this example, SQLDataSource is used to illustrate the usage and effect of the Dynamic UDS feature. Assume that you have generated SQLDataSource.class, start Logi Report Designer with the modified batch file (for details, see [Task 1: Compile and run SQLDataSource](#Compile) in Example 2).

1. Open an existing catalog.
2. In the Catalog Manager resource tree, expand the data source to which the UDS is to be added.
3. [Create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009611502-Creating-Parameters-in-a-Catalog) with the following information:
   * **Name**: sql
   * **Value Type**: String
   * **Prompt Values**:

     Select \* from employee   
     select salary from employee  
     select employeeid, employeeposition, hiredate, notes, salary, photo from employee
4. Right-click the data source node, and then select **New User Defined Data Source** from the shortcut menu.
5. In the New User Defined Data Source dialog, specify the following information:
   * **Name**: employees
   * **Class Name**: SQLDataSource
   * **Parameter**: `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\LogiReport\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=@sql`
6. Select **OK** to add the UDS.

Next, we will create a page report directly on the UDS to test the Dynamic UDS feature. If you want to create web reports and library components on this UDS, you need to first [create a business view](https://devnet.logianalytics.com/hc/en-us/articles/1500009613102-Creating-Business-Views-in-a-Catalog#Create) using this UDS.

1. Select **Home**/**File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog, specify the report title and choose the **Table (Group Left)** component. Select **OK**.
3. In the Data screen of the Table Wizard, choose the UDS **employees** from the User Defined node. Then, select **Next**.
4. In the Display screen, add the fields EMPLOYEEID, employees\_NOTES, employees\_SALARY and HIREDATE to be displayed in the table, edit their display names to **ID**, **Notes**, **Salary**, **Hire Date**, and then select **Next**.
5. In the Group screen, specify to group on the field **EMPLOYEEPOSITION**.
6. Skip the Summary, Chart and filter screens, and in the Style screen, specify to display the report in the Classic style.
7. Select **Finish** to create the report.
8. Select the **View** tab to view the report. You will then be prompted to specify a parameter.
9. Select **select \* from employee** as the parameter, and you will see that data for all fields has been retrieved.

   ![Report created on UDS with all fields](https://devnet.logianalytics.com/hc/article_attachments/4404904406679/cnctn_uds_add_exmpl4_all.gif)
10. Go back and run this report again. This time, choose **Select salary from employee**. You will notice that no groups are displayed and the group name changes to NULL. This is because only the field employees\_SALARY has been selected this time. Logi Report Designer will make no reference to the employees\_Position column, on which the group is based.

    ![View the report created on UDS with employees_SALARY field](https://devnet.logianalytics.com/hc/article_attachments/4404904407063/cnctn_uds_add_exmpl4_null.gif)

**Note:** To make a dynamic UDS work, if the SQL statement at runtime doesn't include all the UDS columns, you need to make sure that none of the UDS columns' properties were edited, that is the Specify Columns option in the New User Defined Data Source dialog should be unselected, otherwise exceptions will be produced when the SQL statement is used to generate a dynamic report from the UDS.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404911578903/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009607022-User-Data-Source-API) [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404911579543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009629681-Oracle-Stored-Procedure-UDS)
