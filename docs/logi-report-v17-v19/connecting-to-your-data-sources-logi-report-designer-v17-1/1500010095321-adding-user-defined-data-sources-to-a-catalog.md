---
title: "Adding User-Defined Data Sources to a Catalog"
id: 1500010095321
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095321-Adding-User-Defined-Data-Sources-to-a-Catalog
updated_at: 2022-09-07T06:17:46Z
---

# Adding User-Defined Data Sources to a Catalog

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057822-User-Data-Source-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057842-Oracle-Stored-Procedure-UDS)

# Adding User-Defined Data Sources to a Catalog

This topic describes the procedure to add user-defined data sources (UDS) into a catalog, and provides examples about adding UDSs of different types.

This topic contains the following sections:

* [Adding a UDS to a Catalog](#Add)
* [Example 1: Adding a Flat File UDS](#Example1)
* [Example 2: Adding an SQL Data Source UDS](#Example2)
* [Example 3: Adding a Java Object Data Source UDS](#Example3)
  + [Demo 1: Using a Simple Java Object UDS](#Demo1)
  + [Demo 2: Using a Java Object UDS with Multi-levels of Collections](#Demo2)
* [Example 4: Adding a Dynamic UDS](#Example4)

## Adding a UDS to a Catalog

The general steps to add a UDS to a catalog are as follows:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open), then in the Catalog Manager, right-click the node of a data source and choose **New User Defined Data Source** from the shortcut menu.

   If you want to add the UDS to a new data source in the catalog, select any of the existing catalog data source, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog box, specify the name of the data source, select the **User Defined** connection type and select **OK**.

   Designer displays the [New User Defined Data Source dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010098081-New-User-Defined-Data-Source-Dialog-Box).

   ![Add User Defined Data Source dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404856906647/nwuds.gif)
2. In the **Name** text box, specify a name for the UDS.
3. In the **Class Name** text box, provide the class name with package name. You can also select **Browse** to find the class file. The class you specify must exist and can be found by Designer, which means the class should be in the class path of the system environment or set in ADDCLASSPATH of setenv.bat/setenv.sh. After you fill in this text box, Designer automatically displays the class name of the interface that the class implements behind "The class implements:".
4. In the **Parameter** box, specify the parameter for the UDS. The parameter string must match the format defined in the [UDS class](https://devnet.logianalytics.com/hc/en-us/articles/1500010057822-User-Data-Source-API#ParamString).

   You can reference [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010099721-Working-with-Parameters) and [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels#CLF) predefined in the current catalog data source in the format *@FieldName*, and the special field "[User Name](https://devnet.logianalytics.com/hc/en-us/articles/1500010094881-Working-with-Special-Fields#UserName)" as *@username* in the parameter string. For example, if the parameter string of a UDS is `SQL=select * from employee`, and you want to use the predefined parameter **p\_sql** to replace the part after "=", then the parameter string is **SQL=@p\_sql**.
5. When you reference parameters and formulas in the parameter string, you can select the **Edit Format** button to edit the format of their values.
6. Select the **Specify Columns** checkbox to enable the column definitions list and add column definitions. If you don't specify the column definitions, Designer gets them from the result set automatically.
   * **Name**  
     The name of a column. It should have the same validation with a common table column. The default names for column definitions are ‘column1', ‘column2', and so on.
   * **SQLType**  
     The data type of the column.
   * **Precision**, **Length**, **Scale**, **Radix**  
     The default value for each SQL type. You can select the cell and modify the value.
   * **Nullable**  
     Indicates whether the value of the column can be null. "X" stands for NoNulls, "√" stands for Nullable, and "?" stands for Nullable Unknown.
7. Select **OK** to add the UDS.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If you reference parameters in the parameter string, Designer runs the UDS with the default parameters and uses the returned data to determine the data type of the columns. If you use formulas in the parameter string, you need to put temporary values in the formulas since Designer does not prompt you to provide values for the parameter string when you add the UDS.

## Example 1: Adding a Flat File UDS

This example uses three classes and their source code are AddressListUDS.java, AddressListResultSet.java, and AddressListResultSetMetaData.java. The data file is AddressesList.txt. You can get all these files in `<install_root>\help\samples\APIUDS\txtUDS`.

AddressesList.txt is a plain text file which contains data information in a table:

Laurena    Croft    34826 Atwood St.     New York City    NY    10004     USA...  
Jonathan    Hopkins    5062 Brandon Green Ave.     Minneapolis    MN    55402     USA...  
Jeremy    Miner    9283 Cherry Leaf Lane     Palo Alto    CA    94303     USA...  
....

You can notice that each line sequentially records the name, address, state, region, zip code, country, e-mail address, and other information.

If you use your own UDS classes, you must be sure that the directory is classpath/package name so that Server can find the class files at runtime. For this demo's UDS classes, they belong to a package named "help". Copy the above necessary files to `<install_root>\help`, and add the additional entry to the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`.

**Task 1: Compile and run the Address UDS**

For example, on Windows, if you have installed Designer into the default directory `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer`,

1. Copy the above necessary files to `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help`.
2. Compile the Java files.

   `javac -classpath "C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\lib\JREngine.jar" Address*.java`
3. Add the additional entry into the ADDCLASSPATH variable of **setenv.bat** in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\bin`.

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help;`

**Task 2: Add the Address UDS to a catalog**

After compilation, you can now add the UDS to a catalog.

1. Start Designer.
2. Open an existing catalog.
3. In the Catalog Manager resource tree, right-click the data source to which you want to add the UDS, then select **New User Defined Data Source** from the shortcut menu.
4. In the New User Defined Data Source dialog box, specify the following information:
   * **Name**: The name you want to use for identifying the UDS in Designer. Here we use **Address**.
   * **Class Name**: The class name of the UDS. You can type one in or select **Browse** to select a class file. Here we use **help.AddressListUDS**.
   * **Parameter**: AddressesList.txt
5. Select **OK** to add the UDS.

## Example 2: Adding an SQL Data Source UDS

This is a fairly complex example, which executes an SQL statement and returns a result set through the JDBC API.

See the following Java code for class definition of the example:

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

  For example, we use HSQL DB as the data source, and `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\Demo\db\JRDemo` as the HSQL DB path; "sa" as the user's name, "" as the password, and `Select * from authors` as the SQL string. The parameter string may be similar to:

  `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=select * from employee`

  If you want to use predefined parameters in the catalog, you can type the parameter string as:

  `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\Demo\\db\\JRDemo"&USER=@un&PSWD=&SQL=@sql`

  Where, "@sql" is a parameter predefined in the catalog, and its default value is "select \* from employee".

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Every time when running, java.sql.Resultset must return the same metadata (UDS fields), including the number and order of fields, and the field properties such as column name, SQL type, precision, scale, nullable, currency, and array.
* The method *getResultSet()* parses the parameter string, builds a connection to the URL, and then executes the SQL statement.
* The method *releaseResultSet()* releases the resource such as Connection, Statement, and ResultSet.

**Task 1: Compile and run SQLDataSource**

This example uses one class and its source code is SQLDataSource.java, which is available in `<install_root>\help\samples\APIUDS\sqlUDS`. In this example, SQLDataSource returns the result set from the demo HSQL DB. You should set up the HSQL DB path in the URL string and point it to the demo database at `<install_root>\Demo\db\JRDemo`.

Copy SQLDataSource.java to `<install_root>\help`, and compile it to generate SQLDataSource.class. Append the path `<install_root>\help` to the ADDCLASSPATH variable of the batch file setenv.bat in `<install_root>\bin`, so that SQLDataSource can be found at runtime.

**Task 2: Add the SQLDataSource UDS to a catalog**

After compilation, you can now add the UDS to a catalog.

1. Start Designer.
2. Open an existing catalog.
3. In the Catalog Manager resource tree, right-click the data source to which you want to add the UDS, then select **New User Defined Data Source** from the shortcut menu.
4. In the New User Defined Data Source dialog box, specify the required information.

   If you select the **Specify Columns** checkbox, Designer enables the column definitions list and you can add column definitions. If you don't specify column definitions, Designer obtains them from the result set automatically. Here, we do not specify column definitions, instead, we use the default ones from ResultSet and ResultSetMetaData.

   Type **employees** in the **Name** text box and **SQLDataSource** in the **Class Name** text box. In the **Parameter** box, type:

   `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=select * from employee`

   Make sure that the five bold parts in the above line are capitalized.
5. Select **OK** to add the UDS.

## Example 3: Adding a Java Object Data Source UDS

The Designer UDS can use any Java object as a data source to create reports. To implement this function, Designer provides the class, UDSForJavaBean, in which the method *getResultSet()* creates instances for the interface JavaBeanDataProvider, and then uses the method *init()* to initialize the data of the created instances.

See the following Java code for class definition of the example:

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

For examples about how to use the Java object data interface, Designer provides you with two demos which are available in `<install_root>\help\samples\APIUDS\javaUDS`.

* [Demo 1: Using a Simple Java Object UDS](#Demo1)
* [Demo 2: Using a Java Object UDS with Multi-levels of Collections](#Demo2)

Before running the demos, you need to do the following:

1. Copy all the content in `<install_root>\help\samples\APIUDS\javaUDS` to `<install_root>\help\UDSForJavaBean`. You need to create the **UDSForJavaBean** directory.
2. Compile all the java files.

   `javac -classpath <install_root>\help\UDSForJavaBean;<install_root>\lib\JREngine.jar;<install_root>\lib\log4j-core-2.13.3.jar;<install_root>\lib\log4j-api-2.13.3.jar; <install_root>\help\UDSForJavaBean\jreport\uds\javabean\*.java`
3. Copy **data.txt** in `<install_root>\help\UDSForJavaBean` to `<install_root>\bin`.
4. Add the path `<install_root>\help\UDSForJavaBean` in the ADDCLASSPATH variable in **setenv.bat** in the `<install_root>\bin` directory.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

### Demo 1: Using a Simple Java Object UDS

In this demo, we use a Java object named "Person" as the data source. You can find the file person.java in `<install_root>\help\UDSForJavaBean\jreport\uds\javabean\beans`. The file is defined as follows:

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
2. In Designer, open an existing catalog, then in the Catalog Manager, expand the data source to which you want to add the UDS.
3. This demo uses generated data, in order to get the real collection of the data objects, create two parameters before importing the Person Java object as follows:
   * **Name**: pUseFakeData (Specify whether to use generated data when running the report.)  
     **Value Type**: Boolean   
     **Prompt Value**: True
   * **Name**: pNumOfFakeData (Specify the number of data records to generate what will be shown when running the report.)  
     **Value Type**: Integer  
     **Prompt Value**: Any integer number

   For more information about creating parameters, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog).
4. Right-click the data source node, and select **New User Defined Data Source** from the shortcut menu.
5. In the New User Defined Data Source dialog box, type **Person** in the **Name** text box.
6. For the **Class Name** text box, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\jreport\uds\javabean`, and then choose **UDSForJavaBean.class**, which imports the class jreport.uds.javabean.beans.Person with full class name.
7. In the **Parameter** box, type in the following string:

   `JavaBeanDS_DataProvider=jreport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=persions&GBeanProvider_BeanClsName=jreport.uds.javabean.beans.Person&GBeanProvider_UseFakeData=true&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_RptDataInitializer=jreport.uds.javabean.SubRptCollectionDataInitializer`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **JavaBeanDS\_DataProvider** is used to specify the Java class which implements jreport.uds.javabean.JavaBeanDataProvider interface, and returns the list of required data objects at runtime. In this demo, it is a list of the Person objects.
   * **JavaBeanDS\_RuntimeDataID** is a reserved value used as a key to get data objects from DataCenter.
   * **GBeanProvider\_\*** are required values for the special data provider, jreport.uds.javabean.GenericBeanDataProvider, which is specified by JavaBeanDS\_DataProvider.

   You can use this provider (jreport.uds.javabean.GenericBeanDataProvider) or create your own provider by implementing the interface jreport.uds.javabean.JavaBeanDataProvider.
8. Select **OK** to add the UDS.
9. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) which is based on this UDS.
10. Select the **View** tab to preview the report. In the Enter Parameter Values dialog box, type **3** as the value of the parameter pNumOfFakeData, and select **OK**. Three records are returned. However, the data you get now is the generated data, because in the parameter string of the UDS, you have specified the value of the key word GBeanProvider\_UseFakeData to true.
11. In order to get the real collection of data objects, you can use the parameter pUseFakeData to control the value of the key GBeanProvider\_UseFakeData value dynamically as follows.

    In the Catalog Manager, right-click the UDS **Person** and select **Edit User Defined Data Source** on the shortcut menu. In the Edit User Defined Data Source dialog box, modify the value of GBeanProvider\_UseFakeData to **@pUseFakeData** in the **Parameter** box.
12. Preview the report again and specify the value of pUseFakeData as **false** to get the real collection of data at runtime.

    ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) Designer applies the key word "GBeanProvider\_RptDataInitializer" in the data provider jreport.uds.javabean.GenericBeanDataProvider to specify the Java class name which implements jreport.uds.javabean.RptDataInitializer interface. Therefore, if you use the data provider jreport.uds.javabean.GenericBeanDataProvider, you just need to provide a class which implements jreport.uds.javabean.RptDataInitializer to return a collection, list, or array of the data objects according to different reports and parameters. Also, jreport.uds.javabean.GenericBeanDataProvider can recognize vector, collection, and array of objects and retrieve the objects inside of the collection one by one.

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
    UDSForJavaBean calls this method to ask the data provider to prepare the data collection/list by the given initProperties. Basically, the initProperties are the name and value pairs parsed from the UDS parameter string.  

    For example, the GenericBeanDataProvider gets the list of properties with the following keys:

    JavaBeanDS\_DataProvider  
    JavaBeanDS\_RuntimeDataID  
    GBeanProvider\_BeanClsName  
    GBeanProvider\_UseFakeData  
    GBeanProvider\_NumOfFakeData  
    GBeanProvider\_RptDataInitializer

    GenericBeanDataProvider applies the values of those keys to prepare the data collection. For example, if the value of GBeanProvider\_UseFakeData is true, GeneridBeanDataProvider uses the fake data; otherwise, it creates an instance by the class name provided by GBeanProvider\_RptDataInitializer and asks the data initializer object to return the collection of data objects.
  + **getMetadataJavaBean()**  
    This method is called back from the UDS to get the bean class in order to construct the metadata for UDS. For GenericBeanDataProvider, the Java bean class in the collection is passed in by the key GBeanProvider\_BeanClsName when you define this data source by UDS.
  + **next()**  
    This method is called back from the UDS to fetch the next data object as a record for the report at runtime. For GenericBeanDataProvider, the method *init()* constructs the data object collection, and the method *next()* is going to check if the collection is a Vector, Collection, or array of objects to determine automatically how to get the next object from the constructed collection.
  + **exit()**  
    This method is called back from the UDS when Logi Report Engine closes the result set returned by UDS. For GenericBeanDataProvider, it calls the data initializer to close if the data is constructed by data initializer.
  + **requireDetails()**  
    This method is called back by the UDS to check if a certain collection attribute from Java bean needs to display in the metadata.
  + **getMaxShareTimes()**  
    The sub-collection attribute from the Java data object could be shared among subreports. This is the call-back method from the UDS to determine the maximum number of times that a certain sub-collection object is going to be shared by the current report. If your report is trying to share the same sub-collection of a Java data object more than this specified value, you will get an error at runtime. However, if your report actually needs to be shared less than the number specified, the data will stay in the buffer without being cleaned.
* **jreport.uds.javabean.RptDataInitializer**  
  GenericBeanDataProvider applies the implementation of this interface to provide the collection of Java objects for different reports and parameters.

  You need to implement the following methods for this interface:

  public Object getDataCollection(Properties props)throws RptDataInitializerException;  
  public void close();

  + **getDataCollection()**  
    This method is called by GenericBeanDataProvider to return the data collection object. The input props are passed down from GenericBeanDataProvider and includes all the values passed down into the *init()* method of the GenericBeanDataProvider.
  + **close()**  
    This method is called back by GenericBeanDataProvider when the *exit()* function is called there.

### Demo 2: Using a Java Object UDS with Multi-levels of Collections

Sometimes, you define the attributes of a Java object by other lists/collections, such as the Java object SimpleBeanTest in `<install_root>\help\UDSForJavaBean\jreport\uds\javabean\beans`, which is defined as follows:

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

For this kind of Java object, Designer can create a report that gets records from SimpleTestBean, but it cannot show the list of persons information in the same report. If you want to create such a report - each record comes from the SimpleBeanTest object, and for each record, display the list of persons information - you have to use a primary report and subreport to implement this function.

**Task 1: Create the primary report**

1. [Make the necessary preparations](#Preparation).
2. In Designer, open an existing catalog, then in the Catalog Manager, expand the data source to which you want to add the UDS.
3. [Create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog) as follows, which we use to specify the number of data records to generate what to show.

   **Name**: pNumOfFakeData  
   **Value Type**: Integer  
   **Prompt Value**: Any integer number. Note that the parameter must have at least one value that is larger than 0; otherwise, you will get exceptions when you run the reports.
4. Right-click the data source node and select **New User Defined Data Source** on the shortcut menu.
5. In the New User Defined Data Source dialog box, type **SimpleTestBean** in the **Name** text box.
6. For the **Class Name** text box, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\jreport\uds\javabean`, and then choose **UDSForJavaBean.class**. The UDS class UDSForJavaBean.class imports the class jreport.uds.javabean.beans.SimpleTestBean with full class name.
7. In the **Parameter** box, type in the following string:

   `JavaBeanDS_DataProvider=jreport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=&GBeanProvider_BeanClsName=jreport.uds.javabean.beans.SimpleBeanTest&GBeanProvider_UseFakeData=true&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_FakeDateSubCollectionInfo=persons,jreport.uds.javabean.beans.Person&GBeanProvider_RptDataInitializer=&GBeanProvider_ListOfDetailProps=persons,1,30000`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **GBeanProvider\_ListOfDetailProps** specifies the following items:
     + The list of property names of sub-collections that are displayed in the metadata
     + How many times that this report is going to share the sub-collection per main object
     + The timeout for the shared data in the DataCenter in milliseconds (the default value is 1 minute).

     In this demo, Designer only imports the sub-collection property persons from the SimpleTestBean class, and the share time is 1. If you want to create another subreport using addresses, you have to specify the value for this keyword as follows:

     `=&GBeanProvider_ListOfDetailProps=persons,1,30000$addresses,1,30000`

     and separate different properties by the "$" symbol.
   * **GBeanProvider\_FakeDateSubCollectionInfo** - Designer uses the value of this key word to construct the fake data for SimpleTestBean collections. Each Java class can have multiple sub-collection objects, and Designer allows not constructing the values of these sub-collection objects if you do not want to use them. However, if you do not specify them here in this parameter string as `<property name>,<property class name>$<property name>,<property class name>`, Designer does not construct the fake data for those sub-collections, and problems occur when you run the report on fake data.
8. Select **OK** and Designer adds the UDS **SimpleTestBean**. In the Catalog Manager, you can see that **persons** appears in the resource tree under the SimpleTestBean node.
9. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) named "MainRpt.cls", with a standard banded object in it as the primary report based on the UDS SimpleTestBean.

**Task 2: Create the subreport**

1. Expand the data source in the catalog to which you want to add the UDS for the subreport.
2. Create a parameter as follows, which we use to specify whether to use generated data when running the report.

   **Name**: pUseFakeData  
   **Value Type**: Boolean   
   **Prompt Value**: True
3. Create another parameter named "pRunTimeDataInfo" of String type, which we use when setting up the link between the primary report and the subreport.

   **Name**: pRunTimeDataInfo  
   **Value Type**: String   
   **Prompt Value**: persons
4. Right-click the data source node and select **New User Defined Data Source** on the shortcut menu.
5. In the New User Defined Data Source dialog box, type **PersonsAsSubRpt** in the **Name** text box.
6. For the **Class Name** text box, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\jreport\uds\javabean`, and then choose **UDSForJavaBean.class**.
7. In the **Parameter** box, type in the following string:

   `JavaBeanDS_DataProvider=jreport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=@pRunTimeDataInfo&GBeanProvider_BeanClsName=jreport.uds.javabean.beans.Person&GBeanProvider_UseFakeData=@pUseFakeData&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_RptDataInitializer=jreport.uds.javabean.SubRptCollectionDataInitializer`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **JavaBeanDS\_RuntimeDataID** is defined to use a parameter which is the link point from the subreport to the sub-collections in the primary report.
   * **GBeanProvider\_RptDataInitializer**'s value is jreport.uds.javabean.SubRptCollectionDataInitializer, which is Logi Report's built-in data provider set up especially for the subreport to return the collection of data by referencing the sub-collection in the primary report. Logi Report Engine passes the referencing information via the parameter value @pRunTimeDataInfo which we use when setting up the link between the primary report and the subreport.
   * The class name for **GBeanProvider\_BeanClsName** is Person because the subreport uses the Person object.
8. Select **OK** to add the UDS **PersonsAsSubRpt**.
9. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500010101181-Creating-Reports#Page) named "SubRpt.cls", with a table in it as the subreport based on the UDS PersonsAsSubRpt.

**Task 3: Link the primary report and the subreport**

1. In the Catalog Manager, [create a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog) named "NotUseFakeData" to return false all the time, for example, `return false`. Designer passes this formula into the subreport as the value of the parameter **pUseFakeData** in the subreport, so that when the subreport runs with the primary report, it always uses the data from the primary report instead of constructing the fake data itself.
2. Open **MainRpt.cls**, add a new detail panel into the report.
3. Selected the newly added panel and select **Insert** > **Subreport**. When a box attached to your mouse pointer, select in the panel and Designer displays the Subreport dialog box.
4. Select the **Browse** button, choose **SubRpt.cls** as the subreport, then in the **Parameters** tab, specify values for the parameters as follows:

   | Parameter | Value |
   | --- | --- |
   | pNumOfFakeData | pNumOfFakeData |
   | pUseFakeData | NotUseFakeData (gives a false value to the parameter) |
   | pRunTimeDataInfo | persons (specifies to use the sub-collection persons of the primary report as the data source of the subreport at runtime) |
5. Select **OK** to insert the subreport. For more information about using subreports, see [Subreports](https://devnet.logianalytics.com/hc/en-us/articles/1500010094861-Working-with-Subreports).
6. Select the **View** tab to preview the primary report. Designer displays the corresponding persons information in the subreport.
7. If you want to insert another subreport which shares the same sub-collection with SubRpt.cls, you should modify the value of the key word GBeanProvider\_ListOfDetailProps in the primary report's UDS parameter string to **GBeanProvider\_ListOfDetailProps=persons,2,30000**. That changes the share amount of the persons property from 1 to 2.

## Example 4: Adding a Dynamic UDS

Designer supports the Dynamic UDS feature, which can improve performance by retrieving only the selected fields and not all the fields. At runtime, Server provides an option for picking up the columns the report users want to see in the report. In this way, Server generates a dynamic report according to your selection.

In this example, we use SQLDataSource to illustrate the usage and effect of the Dynamic UDS feature. Assume that you have generated SQLDataSource.class, start Designer with the modified batch file (for more information, see [Task 1: Compile and run SQLDataSource](#Compile) in Example 2).

1. Open an existing catalog.
2. In the Catalog Manager resource tree, expand the data source to which the UDS is to be added.
3. [Create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog) with the following information:
   * **Name**: sql
   * **Value Type**: String
   * **Prompt Values**:

     Select \* from employee   
     select salary from employee  
     select employeeid, employeeposition, hiredate, notes, salary, photo from employee
4. Right-click the data source node, and then select **New User Defined Data Source** from the shortcut menu.
5. In the New User Defined Data Source dialog box, specify the following information:
   * **Name**: employees
   * **Class Name**: SQLDataSource
   * **Parameter**: `DRIVER="org.hsqldb.jdbcDriver"&URL="jdbc:hsqldb:C:\\(Undefined variable: Logi_Variables.LogiReport)\\Designer\\Demo\\db\\JRDemo"&USER=sa&PSWD=&SQL=@sql`
6. Select **OK** to add the UDS.

Next, we create a page report using the UDS to test the Dynamic UDS feature. If you want to create web reports and library components on this UDS, you need to first [create a business view](https://devnet.logianalytics.com/hc/en-us/articles/1500010101061-Creating-Business-Views-in-a-Catalog#Create) using this UDS.

1. Select **Home**/**File** > **New** > **Page Report**.
2. In the Select Component for Page Report dialog box, specify the report title and choose the **Table (Group Left)** component. Select **OK**.
3. In the **Data** screen of the Table Wizard dialog box, choose the UDS **employees** from the User Defined node. Then, select **Next**.
4. In the **Display** screen, add the fields **EMPLOYEEID**, **employees\_NOTES**, **employees\_SALARY**, and **HIREDATE** to display in the table, edit their display names to **ID**, **Notes**, **Salary**, **Hire Date**. Select **Next**.
5. In the **Group** screen, specify to group on the field **EMPLOYEEPOSITION**.
6. Skip the Summary, Chart, and Filter screens.
7. In the **Style** screen, select the **Classic** style.
8. Select **Finish** to create the report.
9. Select the **View** tab to preview the report. Designer prompts you to specify a parameter.
10. Select **select \* from employee** as the parameter. You can see that Designer retrieves data for all of the fields.

    ![Report created on UDS with all fields](https://devnet.logianalytics.com/hc/article_attachments/4404848651031/cnctn_uds_add_exmpl4_all.gif)
11. Select the **Design** tab to go back to design mode and preview the report again. This time, choose **Select salary from employee** as the parameter value. You can see that the report displays no groups and the group name changes to NULL. This is because Designer selects the field employees\_SALARY this time, and makes no reference to the employees\_Position column, on which the group is based.

    ![View the report created on UDS with employees_SALARY field](https://devnet.logianalytics.com/hc/article_attachments/4404857019415/cnctn_uds_add_exmpl4_null.gif)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) To make a dynamic UDS work, if the SQL statement at runtime does not include all the UDS columns, you need to make sure that you do not edit any of the UDS columns' properties, that is, you should clear the Specify Columns option in the New User Defined Data Source dialog box; otherwise, you get exceptions when using the SQL statement to generate a dynamic report from the UDS.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057822-User-Data-Source-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010057842-Oracle-Stored-Procedure-UDS)
