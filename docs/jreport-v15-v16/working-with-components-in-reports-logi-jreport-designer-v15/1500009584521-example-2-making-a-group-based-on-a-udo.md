---
title: "Example 2: Making a Group Based on a UDO"
id: 1500009584521
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009584521-Example-2-Making-a-Group-Based-on-a-UDO
updated_at: 2021-07-24T05:55:54Z
---

# Example 2: Making a Group Based on a UDO

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584541-Inserting-a-UDO-into-a-Report)

# Example 2: Making a Group Based on a UDO

This topic describes how to make a group based on a UDO. This sample is similar to a summary field. This example includes the implementation of four classes and shares a class with Example 1.

1. Create the template, result, creator and render files as follows:
   * **MySumFld.java**

     |  |
     | --- |
     | ``` //Template package myudo; import jet.report.*; import jet.controls.*; /**  * This class extends from JRObjectTemplate, add two properties "ColumnName" and  * "TextColor".  */ public class MySumFld extends MyDbFld { 	public MySumFld() { 		super(); 	} 	/** 	 * Return the instance name prefix. 	 */ 	public String getPrefix() { 		return "MySumField"; 	} 	public boolean isGroupListener() { 		return true; 	} } ``` |
   * **MySumFldRst.java**

     |  |
     | --- |
     | ``` //Result package myudo; import jet.JRStopEngineException; import jet.connect.Record; import jet.connect.DbValue; import jet.util.*; import jet.datastream.*; import java.io.*; public class MySumFldRst extends MyDbFldRst { 	double value; 	public MySumFldRst() { 	} 	// make the text will be displayed.  	String getText() { 		return "" + value; 	} 	/**   	 * Read the data from DataInput.  	 * UDO can override this method to restore its own data.  	 * @throws JRStopEngineException  	 * */ 	protected void readProperties(DataInput in, DSDataStreamable ds) 			throws IOException, JRStopEngineException { 		super.readProperties(in, ds); 		value = in.readDouble(); 	} 	/**   	 * Write the data to DataInput.  	 * UDO can override this method to save its own data.  	 * */ 	protected void writeProperties(DataOutput out) throws IOException { 		super.writeProperties(out); 		out.writeDouble(value); 	} } ``` |
   * **MySumFldCreator.java**

     |  |
     | --- |
     | ``` //Creator package myudo; import java.awt.*; import java.util.*; import jet.report.*; import jet.controls.*; import jet.connect.*; import jet.udo.*; import jet.datastream.*; import guitools.Painter; import jet.util.*; /**  * * Implements JRObjectResultCreator for creating JRObjectResult in Logi JReport *  * Engine Bean.  */ public class MySumFldCreator implements JRObjectResultCreator, JRGroupListener {  	// This interface must implement by JRObjectCreator. 	MySumFld rpt; 	MySumFldRst dsField; 	double value; 	public MySumFldCreator() { 	} 	public void setTemplate(JRObjectTemplate rptobj) { 		rpt = (MySumFld) rptobj; 	} 	public JRObjectResult createJRObjectResult(JRObjectTemplate rptobj, 			Record record) { 		rpt = (MySumFld) rptobj; 		MySumFldRst dsField = new MySumFldRst(); 		dsField.setTemplate(rpt); 		dsField.value = value; 		return dsField; 	} 	/** * This method will be called before the first record. */ 	public void prepareFetchRecords() { 		value = 0.0; 	} 	/** * This method will be called after the last record. */ 	public void finishFetchRecords() { 	} 	/** * This method will be called each record. */ 	public void fetchNewRecord(Record record) { 		String colName = (String) rpt.getPropertyByName("ColumnName") 				.getObject(); 		// return the column value. 		DbNumber num = (DbNumber) record.getCell(colName); 		if (!num.isNull()) { 			value += num.intValue(); 		} 	} } ``` |
   * **MyDbFldRender.java** (See [Example 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System#MyDbFldRender) for details.)
2. Compile the four Java files in the same way as [Example 1](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System#complie).
3. Modify udo.ini in `<install_root>\lib\` by appending the four classes as follows:

   |  |
   | --- |
   | ``` Begin name=MySumFld  template=myudo.MySumFld  resultobject=myudo.MySumFldRst  resultcreator=myudo.MySumFldCreator  resultviewer=myudo.MyDbFldRender End ``` |
4. Edit setenv.bat in `<install_root>\bin` by appending the path of the four classes to the batch file's ADDCLASSPATH variable. Assume that the four classes are located in `D:\test\myudo`.

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;D:\test;`
5. Start Logi JReport Designer.
6. Select **Insert** > **UDO**. You will now find a new UDO object named MySumFld in the drop-down list of the Insert UDO dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584541-Inserting-a-UDO-into-a-Report)
