---
title: "Example 1: Accessing a Record for a UDO and Registering the UDO with the Report System"
id: 1500009563822
section: "Working with Components in Reports - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009563822-Example-1-Accessing-a-Record-for-a-UDO-and-Registering-the-UDO-with-the-Report-System
updated_at: 2021-07-24T05:55:54Z
---

# Example 1: Accessing a Record for a UDO and Registering the UDO with the Report System

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584501-Creating-a-UDO-Manually)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584521-Example-2-Making-a-Group-Based-on-a-UDO)

# Example 1: Accessing a Record for a UDO and Registering the UDO with the Report System

This topic describes how to access a record for your UDO and how to register your UDO with the report system.

1. A UDO needs to implement at least four classes from Logi JReport. The four classes are for template, result, creator and render files respectively.
   * **MyDbFld.java**

     |  |
     | --- |
     | ``` //Template  package myudo; import jet.report.*; import jet.controls.*; /**  * This class extends form JRObjectTemplate, add two properties "ColumnName" and  * "TextColor".  */ public class MyDbFld extends JRObjectTemplate { 	/** 	 * This property is for the column name of MyDbFld. 	 */ 	public JetColumnName columnName = new JetColumnName(this, "ColumnName"); 	/** 	 * This property is for the background color of MyDbFld.. 	 */ 	public JetColor backColor = new JetColor(this, "TextColor", null, true); 	public MyDbFld() { 		super(); 		columnName.setEditable(true); 		// set the default size. 		set("Width", 40); // before build575 should be width.set(40); 		set("Height", 20); // before build575 should be height.set(20); 		// add the property to group then they can displayed in ReportInspector. 		addPropertyToGroup("ColumnName", "Others"); 		addPropertyToGroup("TextColor", "Color"); 	} 	/** 	 * Return the instance name prefix. > 	 */ 	public String getPrefix() { 		return "MyDbField"; 	} } ``` |
   * **MyDbFldRst.java**

     |  |
     | --- |
     | ``` //Result package myudo; import jet.connect.Record; import jet.connect.DbValue; import jet.util.*; import jet.datastream.*; public class MyDbFldRst extends JRVisiableResult { 	public MyDbFldRst() { 	} 	// retrieve value from column. 	DbValue getValue() { 		// get the column name. 		String colName = (String) getPropertyByName("ColumnName").getObject(); 		// get the report record. 		Record record = getRecord(); 		// return the column value. 		return record.getCell(colName); 	} 	// make the text will be displayed. 	String getText() { 		String sRet; 		DbValue value = getValue(); 		if (value != null && !value.isNull()) { 			sRet = value.toString(); 		} else { 			sRet = "NULL"; 		} 		return sRet; 	} } ``` |
   * **MyDbFldCreator.java**

     |  |
     | --- |
     | ``` //Creator package myudo; import java.awt.*; import java.util.*; import jet.report.*; import jet.controls.*; import jet.connect.*; import jet.udo.*; import jet.datastream.*; import guitools.Painter; import jet.util.*; /**  * Implements JRObjectResultCreator for creating JRObjectResult in Logi JReport  * Engine Bean.  */ public class MyDbFldCreator implements JRObjectResultCreator { 	public MyDbFldCreator() { 	} 	public JRObjectResult createJRObjectResult(JRObjectTemplate rptobj, 			Record record) { 		MyDbFld rpt = (MyDbFld) rptobj; 		MyDbFldRst dsField = new MyDbFldRst(); 		dsField.setTemplate(rpt); 		return dsField; 	} } ``` |
   * **MyDbFldRender.java**

     |  |
     | --- |
     | ``` //Render package myudo; import java.awt.*; import java.awt.event.*; import java.util.*; import jet.datastream.*; import jet.connect.DbValue; import jet.connect.Record; import jet.udo.*; public class MyDbFldRender extends Component implements JRObjectRender { 	String text = null; 	Color color; 	Color background; 	/** 	 * The default constructor. 	 */ 	public MyDbFldRender() { 	} 	// retrieve property and data from JRObjectResult. 	public void setProperty(jet.util.PropertySetable dsPropSet) { 		text = ((MyDbFldRst) dsPropSet).getText(); 		color = (Color) dsPropSet.getPropertyByName("TextColor").getObject(); 		background = (Color) dsPropSet.getPropertyByName("Background") 				.getObject(); 		setBounds(((MyDbFldRst) dsPropSet).getBounds()); 	} 	/** 	 * Paint the text. 	 */ 	public void paint(Graphics g) { 		Dimension dim = getSize(); 		if (background != null) { 			g.setColor(background); 			g.fillRect(0, 0, dim.width, dim.height); 		} 		if (text != null) { 			if (color == null) 				color = Color.black; 			g.setColor(color); 			g.drawString(text, 10, 10); 		} 	} } ``` |

     **Note:** Since the compiling process of Logi JReport Designer differs with that of Logi JReport Server, when you run UDOs in these two applications, you should pay attention to some minor differences. For example, to get width and height, in Logi JReport Designer, you should use:  
     `w = guitools.toolkit.Unit.convertUnitToPixel(((Integer)propertySetable.getPropertyByName
     ("Width").getObject()).intValue());  
      h = guitools.toolkit.Unit.convertUnitToPixel(((Integer)propertySetable.getPropertyByName
     ("Height").getObject()).intValue());`

     While in Logi JReport Server, you should use the following instead:  
     `JRObjectResult obj = (JRObjectResult)propertySetable;  
      w = guitools.toolkit.Unit.convertUnitToPixel(obj.getTemplate().getWidth(obj));  
      h = guitools.toolkit.Unit.convertUnitToPixel(obj.getTemplate().getHeight(obj));`
2. Compile the Java files.

   To compile these four Java files, you should add report.jar and JREngine.jar with their path into the class path (make sure that the path of the file JREngine.jar is before that of the file report.jar). For example, use the following command:

   `Javac -classpath "C:\Logi JReport\Designer\lib\JRengine.jar;C:\Logi JReport\Designer\lib\report.jar;C:\test "MyDbFld.java`

   Here it is assumed that Logi JReport Designer is installed to `C:\Logi JReport\Designer`. The Java files for the example are in `C:\test\myudo`.
3. Modify the udo.ini file in the `<install_root>\lib` directory by appending the four classes as follows:

   |  |
   | --- |
   | ``` Begin name=MyDbField template=myudo.MyDbFld resultobject=myudo.MyDbFldRst resultcreator=myudo.MyDbFldCreator resultviewer=myudo.MyDbFldRender  End ``` |
4. Edit setenv.bat in `<install_root>\bin` by appending the path of the four classes to the batch file's ADDCLASSPATH variable. Assume that the four classes are located in `D:\test\myudo`.

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;D:\test;`
5. Start Logi JReport Designer.
6. Select **Insert** > **UDO**. You will now find a new UDO object named MyDbFld in the drop-down list of the Insert UDO dialog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009584501-Creating-a-UDO-Manually)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009584521-Example-2-Making-a-Group-Based-on-a-UDO)
