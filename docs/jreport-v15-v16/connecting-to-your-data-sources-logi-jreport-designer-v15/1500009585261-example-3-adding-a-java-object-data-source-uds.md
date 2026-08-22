---
title: "Example 3: Adding a Java Object Data Source UDS"
id: 1500009585261
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585261-Example-3-Adding-a-Java-Object-Data-Source-UDS
updated_at: 2021-12-31T02:44:18Z
---

# Example 3: Adding a Java Object Data Source UDS

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564262-Example-4-Adding-a-Dynamic-UDS)

# Example 3: Adding a Java Object Data Source UDS

The Logi JReport Designer UDS can use any Java object as a data source for you to create reports. To implement this function, Logi JReport Designer provides a class UDSForJavaBean, in which the getResultSet() method creates instances for the interface JavaBeanDataProvider, and then uses the method init() to initialize the data of the created instances.

Below is the Java code for class definition:

|  |
| --- |
| ``` public class UDSForJavaBean implements JRUserDataSource  { 	// Define data. 	public ResultSet getResultSet(String param) 			throws JRUserDataSourceException  	{ 		// Method body.    } 	/** 	 * Free the resources such as : Connection, Statement, ResultSet. 	 */ 	public void releaseResultSet() throws JRUserDataSourceException    { 		// Method body. 	} } ``` |

The interface JavaBeanDataProvider is defined as follows:

|  |
| --- |
| ``` public interface JavaBeanDataProvider {     public void init(String dataID, Properties initprops) 		  throws JavaBeanDataProviderException; 	 public Class getMetadataJavaBean() 		  throws ClassNotFoundException; 	 public Object next() throws JavaBeanDataProviderException; 	 public boolean requireDetails(String collectionPropName); 	 public int getMaxShareTimes(String collectionPropName); 	 public int getTimeoutForSubCollection(String collectionPropName); 	 public void exit()throws JavaBeanDataProviderException; } ``` |

For examples of how to use the Java object data interface, Logi JReport provides you with two demos which are available in `<install_root>\help\samples\APIUDS\javaUDS`.

Before running the demos, you need to do the following:

1. Copy all the content in `<install_root>\help\samples\APIUDS\javaUDS` to `<install_root>\help\UDSForJavaBean`. You need to create the UDSForJavaBean directory.
2. Compile all the java files.

   `javac -classpath <install_root>\help\UDSForJavaBean;<install_root>\lib\JREngine.jar;<install_root>\lib\log4j-core-2.7.jar;<install_root>\lib\log4j-api-2.7.jar; <install_root>\help\UDSForJavaBean\Logi JReport\uds\javabean\*.java`
3. Copy data.txt in `<install_root>\help\UDSForJavaBean` to `<install_root>\bin`.
4. Add the path `<install_root>\help\UDSForJavaBean` in the ADDCLASSPATH variable in setenv.bat in the `<install_root>\bin` directory.

* Below is a list of the sections covered in this topic:
* [Demo 1: Using a Simple Java Object UDS](#Demo1)

  [Demo 2: Using a Java Object UDS with Multi-levels of Collections](#Demo2)

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4411773980183/criticalicon.gif) In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information, select this link: *[Statement on Log4j and Log4Net Vulnerabilities](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751)*.

## Demo 1: Using a Simple Java Object UDS

In this demo, a Java object named Person will be used as the data source, you can find the person.java file in `<install_root>\help\UDSForJavaBean\Logi JReport\uds\javabean\beans`. It is defined as follows:

|  |
| --- |
| ``` public class Person implements Serializable     {     private String gender; 	 private String ssn; 	 private String emailAddress; 	 private Date birthDate; 	 private Long newbornWeight; 	 private YesNo isDataVerified; 	 private Name name; 	 private Address currentMailingAddress; 	 private Phone currentWorkPhone;n; /** * @return the birthDate. */ public Date getBirthDate()    {    return birthDate;    } } ``` |

Similar to the code above, other attributes of the Person object are defined by other Java objects, such as currentMailingAddress which is defined by the Address class.

**To create a report from the Person Java object**:

1. [Make the necessary preparations](#Preparation).
2. In Logi JReport Designer, open an existing catalog, then in the Catalog Manager, expand the data source to which the UDS is to be added.
3. This demo uses generated data, in order to get the real collection of the data objects, create two parameters before importing the Person Java object as follows:
   * **Name**: pUseFakeData (Specify whether to use generated data when running the report.)  
     **Value Type**: Boolean   
     **Prompt Value**: True
   * **Name**: pNumOfFakeData (Specify the number of data records to generate that will be shown when running the report.)  
     **Value Type**: Integer  
     **Prompt Value**: Any integer number

   For details about how to create parameters, see [Creating a Parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter).
4. Right-click the data source node, and select **New User Defined Data Source** from the shortcut menu.
5. In the New User Defined Data Source dialog, enter **Person** in the Name text field.
6. For the Class Name field, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\Logi JReport\uds\javabean`, and then choose **UDSForJavaBean.class**, which will import the class Logi JReport.uds.javabean.beans.Person with full class name.
7. In the Parameter box, type in the following string:

   `JavaBeanDS_DataProvider=Logi JReport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=persions&GBeanProvider_BeanClsName=Logi JReport.uds.javabean.beans.Person&GBeanProvider_UseFakeData=true&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_RptDataInitializer=Logi JReport.uds.javabean.SubRptCollectionDataInitializer`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **JavaBeanDS\_DataProvider** is used to specify the Java class which implements Logi JReport.uds.javabean.JavaBeanDataProvider interface, and will return the list of required data objects at runtime – in this demo, it is a list of Person objects.
   * **JavaBeanDS\_RuntimeDataID** is a reserved value used as a key to get data objects from the DataCenter.
   * **GBeanProvider\_\*** are required values for the special data provider - Logi JReport.uds.javabean.GenericBeanDataProvider - which is specified by JavaBeanDS\_DataProvider.

   You can use this provider (Logi JReport.uds.javabean.GenericBeanDataProvider) or create your own provider by implementing the interface Logi JReport.uds.javabean.JavaBeanDataProvider.
8. Select **OK** to add the UDS.
9. [Create a page report with a standard banded object in it](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) which is based on this UDS.
10. Select the **View** tab to run the report. In the Enter Parameter Values dialog, type **3** as the value of the parameter pNumOfFakeData, and select **OK**. Three records will be returned. However, the data you get now is the generated data, because in the parameter string of the UDS, you have specified the value of the key word GBeanProvider\_UseFakeData to true.
11. In order to get the real collection of data objects, the parameter pUseFakeData will be used to control the value of the key GBeanProvider\_UseFakeData value dynamically as follows.

    In the Catalog Manager, right-click the UDS **Person** and select **Edit User Defined Data Source** on the shortcut menu. In the Edit User Defined Data Source dialog, modify the value of GBeanProvider\_UseFakeData to **@pUseFakeData** in the Parameter box.
12. Run the report again and specify the value of pUseFakeData as **false** to get the real collection of data at runtime.

    **Note:** The key word GBeanProvider\_RptDataInitializer in the data provider Logi JReport.uds.javabean.GenericBeanDataProvider is used to specify the Java class name which implements Logi JReport.uds.javabean.RptDataInitializer interface. So if you are using the data provider Logi JReport.uds.javabean.GenericBeanDataProvider, you just need to provide a class which implements Logi JReport.uds.javabean.RptDataInitializer to return a collection, list, or array of the data objects according to different reports and parameters. Also, Logi JReport.uds.javabean.GenericBeanDataProvider can recognize vector, collection and array of objects and retrieve the objects inside of the collection one by one.

### Methods in the demo

**Logi JReport.uds.javabean.GenericBeanDataProvider**

Logi JReport.uds.javabean.GenericBeanDataProvider implements the interface of Logi JReport.uds.javabean.JavaBeanDataProvider by using the following methods:

public void init(String dataID, Properties initprops) throws JavaBeanDataProviderException;  
public Class getMetadataJavaBean() throws ClassNotFoundException;  
public Object next() throws JavaBeanDataProviderException;  
public boolean requireDetails(String collectionPropName);  
public int getMaxShareTimes(String collectionPropName);  
public void exit()throws JavaBeanDataProviderException;

* **init()**  
  This method is called by UDSForJavaBean to ask the data provider to prepare the data collection/list by the given initProperties. Basically, the initProperties are the name and value pairs parsed from the UDS parameter string.  

  For example, the GenericBeanDataProvider will get the list of properties with the following keys:

  JavaBeanDS\_DataProvider  
  JavaBeanDS\_RuntimeDataID  
  GBeanProvider\_BeanClsName  
  GBeanProvider\_UseFakeData  
  GBeanProvider\_NumOfFakeData  
  GBeanProvider\_RptDataInitializer

  The values for those keys will be used by GenericBeanDataProvider to prepare the data collection. For example, if the value of GBeanProvider\_UseFakeData is true, the GeneridBeanDataProvider will use the fake data, otherwise it will create an instance by the class name provided by GBeanProvider\_RptDataInitializer and ask the data initializer object to return the collection of data objects.
* **getMetadataJavaBean()**  
  This method is called back from the UDS to get the bean class in order to construct the meta data for UDS. For GenericBeanDataProvider, the Java bean class in the collection is passed in by the key GBeanProvider\_BeanClsName when you define this data source by UDS.
* **next()**  
  This method is called back from the UDS to fetch the next data object as a record for the report at runtime. For GenericBeanDataProvider, the init() method constructs the data object collection, and the next() method is going to check if the collection is a Vector, Collection, or array of objects to determine automatically how to get the next object from the constructed collection.
* **exit()**  
  This method is called back from the UDS when the Logi JReport engine closes the result set returned by UDS. For GenericBeanDataProvider, it will call the data initializer to close if the data is constructed by data initializer.
* **requireDetails()**  
  This method is called back by the UDS to check if a certain collection attribute from Java bean needs to be displayed in the metadata.
* **getMaxShareTimes()**  
  The sub-collection attribute from the Java data object could be shared among subreports. This is the call-back method from the UDS to determine the maximum number of times that a certain sub-collection object is going to be shared by the current report. If your report is trying to share the same sub-collection of a Java data object more than this specified value, you will get an error at runtime. However, if your report actually needs to be shared less than the number specified, the data will stay in the buffer without being cleaned.

**Logi JReport.uds.javabean.RptDataInitializer**

The implementation of this interface will be used by GenericBeanDataProvider to provide the collection of Java objects for different reports and parameters.

The following methods need to be implemented for this interface:

public Object getDataCollection(Properties props)throws RptDataInitializerException;  
public void close();

* **getDataCollection()**  
  This method is called by GenericBeanDataProvider to return the data collection object. The input props are passed down from GenericBeanDataProvider and includes all the values passed down into the init() method of the GenericBeanDataProvider.
* **close()**  
  This method is called back by GenericBeanDataProvider when exit() function is called there.

## Demo 2: Using a Java Object UDS with Multi-levels of Collections

Sometimes, the attributes of a Java object are defined by other lists/collections, such as the Java object SimpleBeanTest in `<install_root>\help\UDSForJavaBean\Logi JReport\uds\javabean\beans`. It is defined as follows:

|  |
| --- |
| ``` public class SimpleBeanTest implements Serializable {     private String test;     private long l;     private int i;     private int[] intarray;     private Person[] persons;     private Collection addresses;    	private Date dMyDate; } ``` |

From the code above, you can see that the Java class SimpleTestBean contains an array of Persons, a collection of addresses and an array of Int values.

For this kind of Java object, Logi JReport Designer can create a report that gets records from the SimpleTestBean, but it cannot show the list of persons information in the same report. If you want to create such a report - each record comes from the SimpleBeanTest object, and for each record, display the list of persons information - you have to use a primary report and subreport to implement this function.

**Task 1: Create the primary report**

1. [Make the necessary preparations](#Preparation).
2. In Logi JReport Designer, open an existing catalog, then in the Catalog Manager, expand the data source to which the UDS is to be added.
3. [Create a parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500009590261-Creating-a-Parameter) as follows, which is used to specify the number of data records to generate that will be shown when running the report.

   **Name**: pNumOfFakeData  
   **Value Type**: Integer  
   **Prompt Value**: Any integer number. Note that the parameter must have at least one value that is larger than 0, otherwise you will get exceptions when viewing reports.
4. Right-click the data source node and select **New User Defined Data Source** on the shortcut menu. The New User Defined Data Source dialog appears.
5. Type **SimpleTestBean** in the Name text field.
6. For the Class Name filed, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\Logi JReport\uds\javabean`, and then choose **UDSForJavaBean.class**. The UDS class UDSForJavaBean.class will import the class Logi JReport.uds.javabean.beans.SimpleTestBean with full class name.
7. In the Parameter box, type in the following string:

   `JavaBeanDS_DataProvider=Logi JReport.uds.javabean.GenericBeanDataProvider  
    &JavaBeanDS_RuntimeDataID=&GBeanProvider_BeanClsName=Logi JReport.uds.javabean.beans.SimpleBeanTest  
    &GBeanProvider_UseFakeData=true&GBeanProvider_NumOfFakeData=@pNumOfFakeData  
    &GBeanProvider_FakeDateSubCollectionInfo=persons,Logi JReport.uds.javabean.beans.Person  
    &GBeanProvider_RptDataInitializer=&GBeanProvider_ListOfDetailProps=persons,1,30000`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **GBeanProvider\_ListOfDetailProps** specifies the following items:
     + The list of property names of sub-collections that will be displayed in the meta-data
     + How many times that this report is going to share the sub-collection per main object
     + The timeout for the shared data in the DataCenter in milliseconds (the default value is 1 minute).

     In this demo, only the sub-collection property persons will be imported from the SimpleTestBean class, and the share time is 1. If you want to create another subreport using addresses, you have to specify the value for this key word as the following:

     =&GBeanProvider\_ListOfDetailProps=persons,1,30000$addresses,1,30000

     and different properties are separated by the symbol $.
   * **GBeanProvider\_FakeDateSubCollectionInfo**  
     The value of this key word is used to construct the fake data for SimpleTestBean collections. Each Java class can have multiple sub-collection objects, and it is allowed to not construct the values of these sub-collection objects if you do not want to use it. However, if you do not specify them here in this parameter string as `<property name>,<property class name>$<property name>,<property class name>`, the fake data for those sub-collections will not be constructed, and problems will occur when running the report on fake data.
8. Select **OK** and the UDS SimpleTestBean is added. In the Catalog Manager, you will see that persons appears in the resource tree in the SimpleTestBean node.
9. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) named MainRpt.cls, with a standard banded object in it as the primary report based on the UDS SimpleTestBean.

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
5. Type **PersonsAsSubRpt** in the Name text field.
6. For the Class Name text box, select the **Browse** button, go to `<install_root>\help\UDSForJavaBean\Logi JReport\uds\javabean`, and then choose **UDSForJavaBean.class**.
7. In the Parameter box, type in the following string:

   `JavaBeanDS_DataProvider=Logi JReport.uds.javabean.GenericBeanDataProvider&JavaBeanDS_RuntimeDataID=@pRunTimeDataInfo&GBeanProvider_BeanClsName=Logi JReport.uds.javabean.beans.Person&GBeanProvider_UseFakeData=@pUseFakeData&GBeanProvider_NumOfFakeData=@pNumOfFakeData&GBeanProvider_RptDataInitializer=Logi JReport.uds.javabean.SubRptCollectionDataInitializer`

   All the highlighted names in the parameter string above are the key words for the information required by this UDS and related Java class. See the detailed explanation below:

   * **JavaBeanDS\_RuntimeDataID** is defined to use a parameter which will be the link point from the subreport to the sub-collections in the primary report
   * **GBeanProvider\_RptDataInitializer**'s value is Logi JReport.uds.javabean.SubRptCollectionDataInitializer, which is our built-in data provider set up especially for the subreport to return the collection of data by referencing the sub-collection in the primary report. The referencing information is passed via the parameter value @pRunTimeDataInfo which will be used when we set up the link between the primary report and the subreport.
   * The class name for GBeanProvider\_BeanClsName is Person because the subreport will use the Person object.
8. Select **OK**, and the UDS PersonsAsSubRpt is added.
9. [Create a page report](https://devnet.logianalytics.com/hc/en-us/articles/1500009592821-Creating-a-Page-Report) named SubRpt.cls, with a table in it as the subreport based on the UDS PersonsAsSubRpt.

**Task 3: Link the primary report and the subreport**

1. In the Catalog Manager, [create a formula](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula) named NotUseFakeData to return false all the time, for example, `return false`. This formula will be passed into the subreport as the value of the parameter pUseFakeData in the subreport, so that when the subreport runs with the primary report, it will always use the data from the primary report instead of constructing the fake data itself.
2. Open MainRpt.cls, add a new detail panel into the report.
3. Selected the newly added panel and select **Insert** > **Subreport**. When a box attached to your mouse pointer, select in the panel and the Subreport dialog is displayed.
4. Select the **Browse** button, choose **SubRpt.cls** as the subreport, then in the Parameters tab, specify values for the parameters as follows:

   | Parameter | Value |
   | --- | --- |
   | pNumOfFakeData | pNumOfFakeData |
   | pUseFakeData | NotUseFakeData (gives a false value to the parameter) |
   | pRunTimeDataInfo | persons (specifies to use the sub-collection persons of the primary report as the data source of the subreport at runtime) |
5. Select **OK** to insert the subreport. For more information about using subreports, see the document [Subreports](https://devnet.logianalytics.com/hc/en-us/articles/1500009563582-Subreports).
6. Run the primary report, and you will find that the corresponding persons information is displayed in the subreport.
7. If you want to insert another subreport which shares the same sub-collection with SubRpt.cls, you should modify the value of the key word GBeanProvider\_ListOfDetailProps in the primary report UDS parameter string to GBeanProvider\_ListOfDetailProps=persons,2,30000. That changes the share amount of the persons property from 1 to 2.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564242-Example-2-Adding-an-SQL-Data-Source-UDS)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564262-Example-4-Adding-a-Dynamic-UDS)
