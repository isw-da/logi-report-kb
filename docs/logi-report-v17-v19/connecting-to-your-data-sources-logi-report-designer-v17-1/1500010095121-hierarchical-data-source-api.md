---
title: "Hierarchical Data Source API"
id: 1500010095121
section: "Connecting to Your Data Sources - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010095121-Hierarchical-Data-Source-API
updated_at: 2021-07-23T19:14:53Z
---

# Hierarchical Data Source API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057602-Using-Hierarchical-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095101-Adding-Hierarchical-Data-Sources-to-a-Catalog)

# Hierarchical Data Source API

This topic provides a brief introduction to the Hierarchical Data Source API and introduces the three interfaces of the HDS API.

This topic contains the following sections:

* [Introduction to the HDS API](#Intro)
* [HDS API Interfaces](#Interface)
  + [jet.datasource.JRHierarchicalDataSource](#DataSource)
  + [jet.datasource.JRHierarchicalDataset](#Dataset)
  + [jet.datasource.JRHierarchicalDatasetMetaData](#MetaData)

## Introduction to the HDS API

The Hierarchical Data Source API is a part of the Logi Report Data Access Model as shown in the following diagram:

* It is a Java interface that provides a dataset to Logi Report.
* It has a PARAMETER string, which can be changed when the HDS object is added into Designer. The result set may differ according to the PARAMETER string. It is very flexible and convenient.

![Logi Report Data Access Model diagram](https://devnet.logianalytics.com/hc/article_attachments/4404857019159/cnctn_uds_api.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* PARAMETER here is the parameter string given to the HDS interface. That is, the HDS API provides the method *getResultSet (String strParam)*, and PARAMETER is the string strParam in the method. As a reminder, PARAMETER here is different from the parameter object in the catalog. To distinguish between them, an upper case PARAMETER is used to refer to the parameter string in the HDS, and a lower case parameter for the parameter object in a catalog.
* To design a report, Logi Report Engine requires a metadata (see java.sql.ResultSetMetaData) which corresponds with the ResultSet that the data source has returned.; to view or run a report, Logi Report Engine requires a ResultSet object. The hierarchical data source must provide both of these two parts to Logi Report Engine.

The HDS API is flexible and convenient to use. Before you implement it, you should make an overall consideration of the architecture. You can [import an XML hierarchical data source](https://devnet.logianalytics.com/hc/en-us/articles/1500010095101-Adding-Hierarchical-Data-Sources-to-a-Catalog#Import) directly from an external data source to Designer using the Logi Report built-in classes. You can also develop your own classes to implement the HDS APIs, and then import your customized hierarchical data source by [adding a general HDS](https://devnet.logianalytics.com/hc/en-us/articles/1500010095101-Adding-Hierarchical-Data-Sources-to-a-Catalog#General).

## HDS API Interfaces

The following explains the three interfaces of the HDS API you must implement:

* [jet.datasource.JRHierarchicalDataSource](#DataSource)
* [jet.datasource.JRHierarchicalDataset](#Dataset)
* [jet.datasource.JRHierarchicalDatasetMetaData](#MetaData)

**Reference:** The jet.datasource.JRHierarchicalDataSource, jet.datasource.JRHierarchicalDataset and jet.datasource.JRHierarchicalDatasetMetaData classes in the Logi Report Javadoc.

### jet.datasource.JRHierarchicalDataSource

Provides data to Logi Report for generating reports. The JRHierarchicalDataSource class is developed by users of Logi Report, and can provide data from a flat file, non-relational database, or application data. The data returned by this class is in JRHierarchicalDataset object, so that users are required to create a JRHierarchicalDataset instance for Logi Report to use this instance to fetch data. Users can also create their own JRHierarchicalDataset class.

The following are methods provided by the interface.

**public JRHierarchicalDataset getHierarchicalDataset (String param) throws Reused**

This method gets the data in Rhetorician according to the specified parameters.

* **PARAMETER**: param - A String value used to request and get different result sets. The format of the PARAMETER string is defined and also parsed by yourself.
* **Returns**: JRHierarchicalDataset object, which implements the interface JRHierarchicalDataset.
* **Throws**: JRUserDataSourceException - If a data access error occurs.

**public void releaseHierarchicalDataset() throws JRUserDataSourceException**

This method releases the data and related resources.

* **Throws**: JRUserDataSourceException - If a data access error occurs.

The class definition may be as follows:

```
public class HierarchicalDataSource implements JRHierarchicalDataSource {  
    // Define data.  
    public JRHierarchicalDataset getHierarchicalDataset(String param)  
            throws JRUserDataSourceException {  
        // Method body.  
    }  
    public void releaseHierarchicalDataset() throws JRUserDataSourceException {  
        // Method body.  
    }
}
```

### jet.datasource.JRHierarchicalDataset

Provides data to Logi Report for generating reports. The JRHierarchicalDataset class is developed by users of Logi Report, and can provide data from a flat file, non-relational database, or application data.

The following are methods provided by the interface.

```
public interface JRHierarchicalDataset  
{   
    /**   
     * Retrieves the number, types and properties of this object's leaves   
     */   
  public JRHierarchicalDatasetMetaData getMetaData();  
    /**   
     * Moves the cursor down one row from its current position in the current node.  
     * return true if the new current row is valid; false if there are no more rows  
 
     * in the current node.   
    */   
  public boolean next(String branchName);   
    /**   
     * Gets the value of the designated leaf node in the current branch node row as a boolean   
     * in the Java programming language.  
     */  
 
  public boolean getBoolean(int leafIndex);  
 
    /**  
 
     * Gets the value of the designated leaf in the current branch node row as a byte   
     * in the Java programming language.  
 
     */   
  public byte getByte(int leafIndex);  
    /**  
     * Returns the value of the designated leaf in the current branch node row as a short   
     * in the Java programming language.  
    */   
  public short getShort(int leafIndex);   
    /**   
     * Returns the value of the designated leaf in the current branch node row as an int   
     * in the Java programming language.   
     */   
  public int getInt(int leafIndex);  
 
     /**  
     * Returns the value of the designated leaf in the current branch node row as a long   
     * in the Java programming language.  
     */   
  public long getLong(int leafIndex);   
    /**  
 
     * Returns the value of the designated leaf in the current branch node row as a float   
     * in the Java programming language.  
     */   
  public float getFloat(int leafIndex);  
    /**   
     * Returns the value of the designated leaf in the current branch node row as a double  
     * in the Java programming language.  
 
     */   
  public double getDouble(int leafIndex);   
    /**   
     * Gets the value of the designated leaf in the current branch node row as a  
     * java.math.BigDecimal with full precision.  
     */   
  public java.math.BigDecimal getBigDecimal(int leafIndex);  
 
    /**  
     * Returns the value of the designated leaf in the current branch node row as a   
     * java.sql.Date object   
     * in the Java programming language.   
     */   
  public java.sql.Date getDate(int leafIndex);   
 
    /**   
 
     * Returns the value of the designated leaf in the current branch node row as a   
 
     * java.sql.Time object   
     * in the Java programming language.   
     */   
  public java.sql.Time getTime(int leafIndex);   
    /**   
 
     * Returns the value of the designated leaf in the current branch node row as   
     * a java.sql.Timestamp object   
     * in the Java programming language.   
     */   
  public java.sql.Timestamp getTimestamp(int leafIndex);   
    /**   
     * Returns the value of the designated leaf in the current branch node row as a String   
     * in the Java programming language.  
 
     */  
  public String getString(int leafIndex);  
    /**   
 
     * Returns the value of the designated leaf in the current branch node row as an Array object  
     * in the Java programming language.  
     */   
  public java.sql.Array getArray(int leafIndex);   
    /**   
     * Reports whether the last leaf read had a value of SQL NULL  
 
     */   
  public boolean wasNull(int leafIndex);   
    /**   
     * Releases this object's resource.   
     */   
  public void close();  
}
```

### jet.datasource.JRHierarchicalDatasetMetaData

Provides metadata for JRHierarchicalDataset. The JRHierarchicalDatasetMetaData class is developed by users of Logi Report, and it works together with a JRHierarchicalDataset.

The following are methods provided by the interface.

```
public interface JRHierarchicalDatasetMetaData  
 
{   
    /**   
     * Return root node names   
     */   
  public String[] getRoot() ;  
    /**   
     * Return the name of the parent.  
 
     */   
  public String getParentName(String name)  
    /**   
     * Return all leaf node names.  
     */   
  public String[] getLeafNames(String parentName);   
    /**   
 
     * Return the number of leaves of the specified branch node.   
     */   
  public int getLeafCount(String parentName);   
    /**   
     * Return all branch names for the specified parent node.  
 
     */   
  public String[] getBranchNames(String parentName);   
    /**   
     * Return the data type of the leaf.   
     */   
  public int getLeafType(String parentName, String leafName);// throws SQLException;   
    /**   
 
     * Return the name of data type.   
     */   
  public String getLeafTypeName(String parentName, String leafName);   
    /**   
     * Return the precision of the leaf.  
     */   
  public int getPrecision(String parentName, String leafName);   
    /**   
 
     * Return the scale of the leaf.  
     */   
  public int getScale(String parentName, String leafName);  
    /**   
     * Return the nullable state of the leaf.  
     */   
  public int isNullable(String parentName, String leafName);  
    /**   
     * Return the currency state of the leaf.  
 
     */   
 
  public boolean isCurrency(String parentName, String leafName);  
}
```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010057602-Using-Hierarchical-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010095101-Adding-Hierarchical-Data-Sources-to-a-Catalog)
