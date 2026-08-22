---
title: "Hierarchical Data Source API"
id: 1500009563962
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563962-Hierarchical-Data-Source-API
updated_at: 2021-07-24T05:55:51Z
---

# Hierarchical Data Source API

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584721-Hierarchical-Data-Sources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog)

# Hierarchical Data Source API

As a database application, Logi JReport Designer cannot only access data stored in a database through the JDBC connection and user data source (UDS), but also supports the importing of data from hierarchical data sources (HDS).

The HDS API is a part of the Logi JReport Data Access Model as shown in the following diagram:

![](https://devnet.logianalytics.com/hc/article_attachments/4404893965207/cnctn_uds_api.gif)

The hierarchical data source API:

* Is a Java interface that provides a dataset to Logi JReport.
* Has a PARAMETER string, which can be changed when the HDS object is added into Logi JReport Designer. The result set may differ according to the PARAMETER string. It is very flexible and convenient.

**Notes:**

* The PARAMETER here is the parameter string given to the HDS interface. That is, the HDS API provides a method getResultSet (String strParam), and PARAMETER is string strParam in the above method. As a reminder, PARAMETER here is different from the parameter object in the Logi JReport catalog. To distinguish between them, an upper case PARAMETER is used to refer to the parameter string in the HDS, and a lower case parameter for the parameter object in a catalog.
* To design a report, Logi JReport requires a metadata (see java.sql.ResultSetMetaData) which corresponds with the ResultSet that the data source has returned. To view or run a report, Logi JReport requires a ResultSet object. The hierarchical data source must provide both of these two parts to Logi JReport.

Below is a list of the sections covered in this topic:

> * [HDS API Interfaces](#Interface)
> * [Examples of Using the HDS API](#Example)

## HDS API Interfaces

The HDS API contains three interfaces as listed below that you must implement.

> [jet.datasource.JRHierarchicalDataSource](#DataSource)
>
> [jet.datasource.JRHierarchicalDataset](#Dataset)
>
> [jet.datasource.JRHierarchicalDatasetMetaData](#MetaData)

**Reference:** Logi JReport Javadoc jet.datasource.JRHierarchicalDataSource, jet.datasource.JRHierarchicalDataset and jet.datasource.JRHierarchicalDatasetMetaData classes in `<install_root>\help\api`.

### jet.datasource.JRHierarchicalDataSource

Provides data to Logi JReport for generating reports. The JRHierarchicalDataSource class is developed by users of Logi JReport, and can provide data from a flat file, non-relational database, or application data. The data returned by this class is in JRHierarchicalDataset object, so that users are required to create a JRHierarchicalDataset instance for Logi JReport to use this instance to fetch data. Users can also create their own JRHierarchicalDataset class.

The following are methods provided by the interface.

**public JRHierarchicalDataset getHierarchicalDataset (String param) throws JRUserDataSourceException**

This method gets the data in JRHierarchicalDataset according to the parameters set.

* **PARAMETER**: param - A String value used to request and get different result sets. The format of the PARAMETER string is defined and also parsed by yourself.
* **Returns**: JRHierarchicalDataset object, which implements the interface JRHierarchicalDataset.
* **Throws**: JRUserDataSourceException - If a data access error occurs.

**public void releaseHierarchicalDataset() throws JRUserDataSourceException**

This method releases the data and related resources.

* **Throws**: JRUserDataSourceException - If a data access error occurs.

The class definition may be as follows:

|  |
| --- |
| ``` public class HierarchicalDataSource implements JRHierarchicalDataSource { 	// Define data. 	public JRHierarchicalDataset getHierarchicalDataset(String param) 			throws JRUserDataSourceException { 		// Method body. 	} 	public void releaseHierarchicalDataset() throws JRUserDataSourceException { 		// Method body. 	} } ``` |

### jet.datasource.JRHierarchicalDataset

Provides data to Logi JReport for generating reports. The JRHierarchicalDataset class is developed by users of Logi JReport, and can provide data from a flat file, non-relational database, or application data.

The following are methods provided by the interface.

|  |
| --- |
| ``` public interface JRHierarchicalDataset {      /**      * Retrieves the number, types and properties of this object's leaves      */    public JRHierarchicalDatasetMetaData getMetaData();     /**      * Moves the cursor down one row from its current position in the current node.     * return true if the new current row is valid; false if there are no more rows      * in the current node.      */    public boolean next(String branchName);      /**      * Gets the value of the designated leaf node in the current branch node row as a boolean      * in the Java programming language.      */    public boolean getBoolean(int leafIndex);      /**      * Gets the value of the designated leaf in the current branch node row as a byte      * in the Java programming language.      */    public byte getByte(int leafIndex);     /**     * Returns the value of the designated leaf in the current branch node row as a short      * in the Java programming language.     */    public short getShort(int leafIndex);      /**      * Returns the value of the designated leaf in the current branch node row as an int      * in the Java programming language.      */    public int getInt(int leafIndex);      /**     * Returns the value of the designated leaf in the current branch node row as a long      * in the Java programming language.     */    public long getLong(int leafIndex);      /**      * Returns the value of the designated leaf in the current branch node row as a float      * in the Java programming language.     */    public float getFloat(int leafIndex);     /**      * Returns the value of the designated leaf in the current branch node row as a double     * in the Java programming language.      */    public double getDouble(int leafIndex);      /**      * Gets the value of the designated leaf in the current branch node row as a     * java.math.BigDecimal with full precision.     */    public java.math.BigDecimal getBigDecimal(int leafIndex);     /**     * Returns the value of the designated leaf in the current branch node row as a      * java.sql.Date object      * in the Java programming language.      */    public java.sql.Date getDate(int leafIndex);      /**      * Returns the value of the designated leaf in the current branch node row as a      * java.sql.Time object      * in the Java programming language.      */    public java.sql.Time getTime(int leafIndex);      /**      * Returns the value of the designated leaf in the current branch node row as      * a java.sql.Timestamp object      * in the Java programming language.      */    public java.sql.Timestamp getTimestamp(int leafIndex);      /**      * Returns the value of the designated leaf in the current branch node row as a String      * in the Java programming language.     */   public String getString(int leafIndex);     /**      * Returns the value of the designated leaf in the current branch node row as an Array object     * in the Java programming language.     */    public java.sql.Array getArray(int leafIndex);      /**      * Reports whether the last leaf read had a value of SQL NULL      */    public boolean wasNull(int leafIndex);      /**      * Releases this object's resource.      */    public void close(); } ``` |

### jet.datasource.JRHierarchicalDatasetMetaData

Provides meta data for JRHierarchicalDataset. The JRHierarchicalDatasetMetaData class is developed by users of Logi JReport, and it works together with a JRHierarchicalDataset.

The following are methods provided by the interface.

|  |
| --- |
| ``` public interface JRHierarchicalDatasetMetaData  {      /**      * Return root node names      */    public String[] getRoot() ;     /**      * Return the name of the parent.      */    public String getParentName(String name)     /**      * Return all leaf node names.     */    public String[] getLeafNames(String parentName);      /**      * Return the number of leaves of the specified branch node.      */    public int getLeafCount(String parentName);      /**      * Return all branch names for the specified parent node.      */    public String[] getBranchNames(String parentName);      /**      * Return the data type of the leaf.      */    public int getLeafType(String parentName, String leafName);// throws SQLException;      /**      * Return the name of data type.      */    public String getLeafTypeName(String parentName, String leafName);      /**      * Return the precision of the leaf.     */    public int getPrecision(String parentName, String leafName);      /**      * Return the scale of the leaf.     */    public int getScale(String parentName, String leafName);     /**      * Return the nullable state of the leaf.     */    public int isNullable(String parentName, String leafName);     /**      * Return the currency state of the leaf.     */    public boolean isCurrency(String parentName, String leafName); } ``` |

## Examples of Using the HDS API

The HDS API is flexible and convenient to use. Before you implement it, you should make an overall consideration of the architecture. Logi JReport provides you with several scenarios which use the Logi JReport HDS API. You can refer to them for assistance.

* You can import an XML format hierarchical data source directly from an external data source to Logi JReport Designer using the Logi JReport built-in classes. See [Example 2: Importing an HDS from an XML file to a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog#XML).
* You can also develop your own classes to implement the HDS APIs, and then import your customized hierarchical data source. See [Example 1: Adding a general HDS to a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog#General).

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584721-Hierarchical-Data-Sources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584741-Adding-an-HDS-to-a-Catalog)
