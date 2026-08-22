---
title: "Hierarchical Data Source API"
id: 5735527956503
section: "Connecting to Your Data Sources - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735527956503-Hierarchical-Data-Source-API
updated_at: 2022-11-02T04:28:56Z
---

# Hierarchical Data Source API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512701335-Using-Hierarchical-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog)

# Hierarchical Data Source API

This topic provides a brief introduction to the Hierarchical Data Source API and introduces the three interfaces of the HDS API.

This topic contains the following sections:

* [Introduction to the HDS API](#Intro)
* [HDS API Interfaces](#Interface)
  + [jet.datasource.JRHierarchicalDataSource](#DataSource)
  + [jet.datasource.JRHierarchicalDataset](#Dataset)
  + [jet.datasource.JRHierarchicalDatasetMetaData](#MetaData)

## Introduction to the HDS API

The Hierarchical Data Source API, a Java interface that provides a dataset to Logi Report, is a part of the Logi ReportData Access Model as shown in the following diagram. It has a PARAMETER string, which you can change when adding the HDS object to Designer, so the result set may differ according to the PARAMETER string.

![Logi Report Data Access Model diagram](https://devnet.logianalytics.com/hc/article_attachments/9898533708183/cnctn_uds_api.gif)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg)

* PARAMETER here is the parameter string given to the HDS interface. That is, the HDS API provides the *getResultSet (String strParam)* method, and PARAMETER is the string strParam in the method. As a reminder, PARAMETER here is different from the parameter object in the catalog. To distinguish between them, an uppercase PARAMETER is used to refer to the parameter string in the HDS, and a lowercase parameter for the parameter object in a catalog.
* To design a report, Logi Report Engine requires a metadata (see java.sql.ResultSetMetaData) which corresponds with the ResultSet that the data source has returned.; to view or run a report, Logi Report Engine requires a ResultSet object. The hierarchical data source must provide both of these two parts to Logi Report Engine.

The HDS API is flexible and convenient. Before you implement it, you should make an overall consideration of the architecture. You can [import an XML hierarchical data source](https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog#Import) directly from an external data source to Designer using the Logi Report built-in classes. You can also develop your own classes to implement the HDS APIs, and then import your customized hierarchical data source by [adding a general HDS](https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog#General).

## HDS API Interfaces

The following explains the three interfaces of the HDS API you must implement.

The interfaces include:

* [jet.datasource.JRHierarchicalDataSource](#DataSource)
* [jet.datasource.JRHierarchicalDataset](#Dataset)
* [jet.datasource.JRHierarchicalDatasetMetaData](#MetaData)

**Reference:** The jet.datasource.JRHierarchicalDataSource, jet.datasource.JRHierarchicalDataset and jet.datasource.JRHierarchicalDatasetMetaData classes in the Logi Report Java API Documentation.

### jet.datasource.JRHierarchicalDataSource

This interface provides data to Logi Report for generating reports. You can develop the JRHierarchicalDataSource class to provide data from a flat file, non-relational database, or application data. The data returned by this class is in the JRHierarchicalDataset object, so you need to create a JRHierarchicalDataset instance for Logi Report to use this instance to fetch data. You can also create your own JRHierarchicalDataset class.

The interface contains the following methods:

* **public JRHierarchicalDataset getHierarchicalDataset (String param) throws Reused**  
  You can use this method to get the data in Rhetorician according to the specified parameter and return the JRHierarchicalDataset object, which implements the JRHierarchicalDataset interface. The method throws JRUserDataSourceException, if a data access error occurs.

  This method has one parameter, *param*. It is a String value used to request and get different result sets. The format of the PARAMETER string is defined and also parsed by yourself.
* **public void releaseHierarchicalDataset() throws JRUserDataSourceException**  
  You can use this method to release the data and related resources. The method throws JRUserDataSourceException, if a data access error occurs.

  The class definition may be:

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

This interface provides data to Logi Report for generating reports. You can develop the JRHierarchicalDataset class to provide data from a flat file, non-relational database, or application data.

The interface contains the following methods:

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

This interface provides metadata for JRHierarchicalDataset. You can develop the JRHierarchicalDatasetMetaData class and have it work together with JRHierarchicalDataset.

The interface contains the following methods:

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735512701335-Using-Hierarchical-Data-Sources)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735499355159-Adding-Hierarchical-Data-Sources-to-a-Catalog)
