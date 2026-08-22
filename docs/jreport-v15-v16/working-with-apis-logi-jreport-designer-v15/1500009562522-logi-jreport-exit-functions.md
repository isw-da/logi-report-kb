---
title: "Logi JReport Exit Functions"
id: 1500009562522
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009562522-Logi-JReport-Exit-Functions
updated_at: 2021-07-24T05:56:18Z
---

# Logi JReport Exit Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562402-Design-API-Samples)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582921-Security-Context-Support)

# Logi JReport Exit Functions

Logi JReport has developed three Exit functions: After Init Parameter, After Run and Before Run. These functions enable you to develop an action to be called before, during and after the process of running a report. A status will then be returned. If the returned status is true, the Logi JReport Engine will go on running. If false, the Logi JReport Engine will stop at this point.

Below is a list of the sections covered in this topic:

> * [Exit Function Properties](#Exit)
> * [Executive Interfaces](#Executive)
> * [Using the Exit Functions](#Use)

## Exit Function Properties

Open a report in Logi JReport Designer. In the Report Inspector, select the node that represents the report tab and you will find the three Exit function properties: After Init Parameter, After Run and Before Run.

![Report Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/4404894013207/wkapi_exitfctn_prpty.gif)

* **After Init Parameter**  
   When running the report, after you enter parameters in the parameter dialog, this function allows you to call a program developed by yourself.
* **After Run**  
   Allows you to call a program developed by yourself after running a report.
* **Before Run**  
   Calls a program developed by yourself just before running a report.

**Reference:** For API information, see Logi JReport Javadoc jet.util package and jet.exception package in `<install_root>\help\api`.

## Executive Interfaces

Three interfaces are provided for you to implement the Exit functions:

**jet.util.JURLExecutor**

This interface provides the following method, which is used to get the status of the Logi JReport Engine:

* **public boolean exec(String[] params) throws JURLExecuterException**
  + **Parameter**  
     params - Array of strings, each element is defined and parsed by yourself. You can enter the PARAMETERs in the Report Inspector. If no PARAMETER is entered, params.length will be zero.
  + **Return**  
     Boolean value. If true, the Logi JReport Engine will continue running. If false, Logi JReport Engine will stop at this point.

**jet.util.JURLEngineExecutor**

This interface provides the following method, which is used to get the status of the Logi JReport Engine:

* **public boolean exec(String[] params, EngineExecutor executor) throws JURLExecutorException**
  + **Parameter**  
     params - Array of strings, each element of which is defined by yourself and also parsed by yourself. You can enter the PARAMETERs in the Report Inspector. If no PARAMETERs are entered, then params.length is zero.  
     executor - Executor of EngineExecutor, which is another interface Logi JReport provides for exporting a report to HTML, TXT or PDF format within the Exit functions.
  + **Return**  
     boolean value. If true, the Logi JReport Engine will continue running. If false, the Logi JReport Engine will stop at this point.

**jet.util.EngineExecutor**

This interface provides three methods:

* **public boolean exportToHtml(String htmlFileName, boolean bChartApplet, boolean isMultiFile, boolean bUsingTable, boolean bHyperlink, boolean bPageNum, boolean bAbsolute, int iBrowser)** 

  This method is used to export the report result to HTML format.

  + **Parameter**  
     HtmlFileName - Name of the HTML format result file with full path.  
     bChartApplet - A Boolean value which specifies whether or not a chart in an HTML file is an applet.  
     isMultiFile - A Boolean value which specifies whether or not the HTML is generated to one or multiple files.  
     bUsingTable - A Boolean value which specifies whether or not to use the HTML table format for exporting HTML files.  
     bHyperLink - A Boolean value which specifies whether or not to generate hyperlinks.  
     bPageNum - A Boolean value which specifies whether or not to generate page number.  
     bAbsolute - A Boolean value which specifies whether or not the font size is absolute or relative.  
     iBrowser - An int value which specifies whether or not the web browser is IE.
  + **Return**  
     Boolean value for exporting status. If true, the report has been successfully exported and vice versa.
* **public boolean exportToPdf(String pdfFileName)** 

  This method is used to export the report result to PDF format.

  + **Parameter**  
     PdfFileName - The name of the PDF format result file with a full path.
  + **Return**  
     Boolean value for exporting status. If true, the report has been successfully exported and vice versa.
* **public boolean exportToText(String textFileName, boolean isNormalText, boolean isRepeat, char delimiter)** 

  This method is used for exporting the report result to text format.

  + **Parameter**  
     TextFileName - Name of the TEXT format result file with full path, where "true/false" sets whether or not the text file is of normal text format or of standard data format. A standard data format text file is a text file where each row represents a single record in a report. It can be used as a text data source for exchanging data with other applications.  
     isNormalText - A Boolean value which specifies whether or not a text file is in normal text format.  
     isRepeat - A Boolean value which specifies whether or not the contents will be repeated.  
     delimiter - A character which is be used in SDF (Standard Data Format). The delimiter will only be used when the "true/false" parameter is set to false. Delimiters can be ',' (the CSV format) or any other character. The default is ' ' (a blank), which is the SSV format.
  + **Return**  
     Boolean value for exporting status. If true, the report has been successfully exported and vice versa.

**Reference:** For API information, see JURExecutor, JUREngineExecutor and EngineExecutor interfaces in the Logi JReport Javadoc jet.util package located at `<install_root>\help\api`.

## Using the Exit Functions

**Example 1: Using parameters in the Exit functions**

In this example, we provide a simple application which will run at all the three times, Before Run, After Init Parameter, and After Run.

1. Develop your Java files to implement the methods. In the example, copy the following code and save it as **testa.java** to `C:\Logi JReport\Designer\help` (here it is assumed that you have installed your Logi JReport Designer to the default directory).

   |  |
   | --- |
   | ``` import java.io.*; import java.awt.*; import java.net.*; import jet.util.*; public class testa implements JURLExecuter { 	public boolean exec(String[] params)  	{ 		System.out.println("testa : "); 		for (int i = 0; i < params.length; i++)  		{ 			System.out.print("\"" + params[i] + "\","); 		} 		System.out.println(); 		return true; 	} } ``` |
2. Compile testa.java to generate the class file testa.class in `C:\Logi JReport\Designer\help`.
3. Modify the batch file setenv.bat in `C:\Logi JReport\Designer\bin` by appending the path `C:\Logi JReport\Designer\help` into the batch file's ADDCLASSPATH variable:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\Logi JReport\Designer\help;`
4. Start Logi JReport Designer, then open a report with parameter.
5. In the Report Inspector, select the node that represents the report tab and specify the class and give parameters for the three functions, for example:

   ![Report Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/4404894013463/wkapi_exitfctn_use.gif)

   **JURL:/** - The standard format, and followed by the class name. **testa** - The class name in this example. **aa;bb;cc** and **123;234;345** - The string type parameters of the class, which are divided by semicolons. **Param** - A predefined Logi JReport parameter used in the current report, which is introduced by the symbol @.

   As shown above, two types of Exit function parameters are supported, they are:

   * String type parameters, such as aa, C:\ and so on. In this case, the string will be passed directly to the Exit function.
   * Logi JReport predefined parameters used in the current report, which are introduced by the @ symbol. In this case, the parameter value will be passed to the Exit function.
6. Run the report, the report engine will call the class that you specified in the Report Inspector.

**Example 2: Using formulas in the Exit functions**

Logi JReport allows you to use formulas in the Exit functions. To do this, you can use the Data Container Link function which can return value of any formula to a parameter. And using the parameter in the Exit functions, you will get the value of the formula in the Exit functions.

1. Create a formula and insert it into a report. It should be put in the child data component.
2. Create a parameter with the same data type of the formula, leaving other options blank, and then insert it into the parent data component.
3. Right-click the parent data component and select **Data Container Link** on the shortcut menu.
4. In the Data Container Link dialog, select the **Return Value** tab, add the formula in the Field in Child Data Container to the Return Value box, then select **OK**.

   Now, you have finished passing value of the formula to a parameter.
5. Use this parameter in the Exit functions with the method described in Example 1, and then the final value of formula will be returned in the Exit functions.

**Notes:**

* When a Logi JReport parameter is used as the parameter of the Before Run function, no Logi JReport parameter value will be returned, and the returned value will be the Logi JReport parameter name with the @ symbol.
* For the Logi JReport parameter that are used as Exit function parameters, they must be used in the report. Otherwise, no value will be returned.
* If you want to publish the report to Logi JReport Server and run it there, you should publish both the report and the catalog file to Logi JReport Server. However, do not forget to add the path to the `-classpath` option in the batch file that starts Logi JReport Server.
* Using formulas in Exit functions can also be realized by using returning values in subreport. Thus, you need to pass value of a formula in the subreport to a parameter in the primary report.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562402-Design-API-Samples)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009582921-Security-Context-Support)
