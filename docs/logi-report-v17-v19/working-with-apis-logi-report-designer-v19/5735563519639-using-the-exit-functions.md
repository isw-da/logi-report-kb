---
title: "Using the Exit Functions"
id: 5735563519639
section: "Working with APIs - Logi Report Designer v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5735563519639-Using-the-Exit-Functions
updated_at: 2022-11-02T08:17:11Z
---

# Using the Exit Functions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498221463-Running-the-Design-API-Samples)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511625623-Applying-Security-Context-Support)

# Using the Exit Functions

When you run a report, Logi Report Engine accomplishes the display of the report, and you have no control over this. However, Logi Report enables you to interact with this mechanism at three points:

* After Logi Report initiates the parameter a report uses.
* At the point Logi Report Engine is about to run the report. If the report contains parameters, Logi Report Engine has initiated the parameters at this stage, and you have given the parameter values.
* Immediately after Logi Report Engine displays the report.

At any or all of these three points, you have the option of executing a class of your choice. Logi Report develops three Exit functions for you: After Init Parameter, Before Run, and After Run. These functions enable you to develop an action that you want to call before, after, or during the process of running a report, and return a status to Logi Report Engine. If the returned status is "true", Logi Report Engine goes on running; if "false", Logi Report Engine stops at this point. This topic describes the properties and interfaces of the Exit functions, and how you can use the Exit functions.

This topic contains the following sections:

* [Exit Function Properties](#Exit)
* [Executive Interfaces of the Exit Functions](#Interface)
* [Using the Exit Functions](#Use)
  + [Example 1: Using Parameters in the Exit Functions](#Example1)
  + [Example 2: Using Formulas in the Exit Functions](#Example2)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/9898403122327/noteicon.jpg) You can apply the Exit functions to page reports only.

## Exit Function Properties

Open a page report in Designer, then in the Report Inspector, select the node that represents the report tab and you can find the three Exit function properties: After Init Parameter, After Run, and Before Run.

![Report Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/9898536360983/wkapi_exitfctn_prpty.gif)

For more information about the three properties, see [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/5735554819863-Page-Report-Tab-Properties#ExitFunction).

## Executive Interfaces of the Exit Functions

Logi Report provides you with three interfaces to implement the Exit functions.

**jet.util.JURLExecutor**

This interface contains the *public boolean exec(String[] params) throws JURLExecuterException* method. You can use it to get the status of Logi Report Engine and return a Boolean value. If the method returns "true", Logi Report Engine continues running; if it returns "false", Logi Report Engine stops at this point.

Parameter in the method:

* **params**  
  Array of strings. You need to define and parse each element by yourself. You can specify the PARAMETERs in the Report Inspector. If you do not specify any PARAMETERs, params.length is zero.

**jet.util.JURLEngineExecutor**

This interface contains the *public boolean exec(String[] params, EngineExecutor executor) throws JURLExecutorException* method. You can use it to get the status of Logi Report Engine and return a Boolean value. If the method returns "true", Logi Report Engine continues running; if it returns "false", Logi Report Engine stops at this point.

Parameter in the method:

* **params**  
  Array of strings. You need to define and parse each element by yourself. You can specify the PARAMETERs in the Report Inspector. If you do not specify any PARAMETERs, params.length is zero.  
  executor - Executor of EngineExecutor, which is another interface Logi Report provides for exporting a report to HTML, TXT, or PDF within the Exit functions.

**jet.util.EngineExecutor**

This interface contains three methods:

* **public boolean exportToHtml(String htmlFileName, boolean bChartApplet, boolean isMultiFile, boolean bUsingTable, boolean bHyperlink, boolean bPageNum, boolean bAbsolute, int iBrowser)**  
  You can use this method to export the report to HTML and return a Boolean value for the exporting status. If the method exports the report successfully, it returns "true"; otherwise, it returns "false".

  Parameters in the method:

  + **htmlFileName**  
    Full path of the HTML output file.
  + **bChartApplet**  
    A Boolean value that specifies whether a chart in an HTML file is an applet. This parameter is deprecated and you should not use it.
  + **isMultiFile**  
    A Boolean value that specifies whether to generate the HTML output in one or multiple files.
  + **bUsingTable**  
    A Boolean value that specifies whether to use the HTML table format for exporting HTML files.
  + **bHyperLink**  
    A Boolean value that specifies whether to generate hyperlinks.
  + **bPageNum**  
    A Boolean value that specifies whether to generate page number.
  + **bAbsolute**  
    A Boolean value that specifies whether the font size is absolute or relative.
  + **iBrowser**  
    An int value that specifies whether the web browser is IE.
* **public boolean exportToPdf(String pdfFileName)**  
  You can use this method to export the report to PDF and return a Boolean value for the exporting status. If the method exports the report successfully, it returns "true"; otherwise, it returns "false".

  Parameter in the method:

  + **pdfFileName**  
    Full path of the PDF output file.
* **public boolean exportToText(String textFileName, boolean isNormalText, boolean isRepeat, char delimiter)**  
  You can use this method to export the report to Text and return a Boolean value for the exporting status. If the method exports the report successfully, it returns "true"; otherwise, it returns "false".

  Parameters in the method:

  + **textFileName**  
    Full path of the text output file, where "true"/"false" specifies whether the text file is in normal text format or standard data format. A standard data format text file is a text file where each row represents a single record in a report. You can use it as a text data source for exchanging data with other applications.
  + **isNormalText**  
    A Boolean value that specifies whether a text file is in normal text format.
  + **isRepeat**  
    A Boolean value that specifies whether to repeat the content.
  + **delimiter**  
    A character to be used in SDF (Standard Data Format). The method applies the delimiter only when the "true/false" parameter is set to "false". Delimiters can be ',' (the CSV format) or any other character. The default is a blank, which is the SSV format.

**Reference:** For API information, see the JURExecutor, JUREngineExecutor, and EngineExecutor interfaces in the jet.util package in the Logi Report Java API Documentation.

## Using the Exit Functions

Here are some tips for you when using the Exit functions:

* When you use a Logi Report parameter as the parameter of the Before Run function, the function returns no Logi Report parameter value, instead, the return value is the Logi Report parameter name with the "@" symbol.
* If you want to use Logi Report parameters as the Exit function parameters, you must use them in a report; otherwise, the function returns no value.
* When you want to publish a report that applies the Exit functions to Server and run it there, you should publish both the report and the catalog file to Server. In addition, you should add the path to the CLASSPATH environment variable of the batch file that starts Server.
* You can also apply formulas in the Exit functions by using [returning values](https://devnet.logianalytics.com/hc/en-us/articles/5735521147415-Working-with-Subreports#Value) in subreports. In this case, you need to pass value of a formula in the subreport to a parameter in the primary report.

The following two examples show using the Exit functions to achieve specific goals.

### Example 1: Using Parameters in the Exit Functions

In this example, we provide a simple application that runs at all the three points, Before Run, After Init Parameter, and After Run.

1. Develop your Java files to implement the methods. In the example, copy the following code and save it as **testa.java** to `C:\LogiReport\Designer\help` (here it is assumed that you have installed your Designer to the default directory).

   ```
   import java.io.*;  
   import java.awt.*;  
   import java.net.*;  
   import jet.util.*;  
     
   public class testa implements JURLExecuter  
   {  
       public boolean exec(String[] params)  
       {  
           System.out.println("testa : ");  
           for (int i = 0; i < params.length; i++)  
    
           {  
               System.out.print("\"" + params[i] + "\",");  
           }  
           System.out.println();  
           return true;  
       }  
   }
   ```
2. Compile testa.java to generate the class file **testa.class** in `C:\LogiReport\Designer\help`.
3. Modify **setenv.bat** in `C:\LogiReport\Designer\bin` by appending the path `C:\LogiReport\Designer\help` to the batch file's ADDCLASSPATH variable:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\LogiReport\Designer\help;`
4. Start Designer.
5. Open a page report with parameter.
6. In the Report Inspector, select the node that represents the report tab and specify the class and give parameters for the three functions, for example:

   ![Report Inspector Panel](https://devnet.logianalytics.com/hc/article_attachments/9898536366871/wkapi_exitfctn_use.gif)

   Where,

   * **JURL:/** is the standard format, and should be followed by the class name.
   * **testa** is the class name in this example.
   * **123;234;345** are String type parameters of the class.
   * **Param** is a predefined Logi Report parameter used in the current report.

   As described earlier in this topic, Designer supports two types of the Exit function parameters. They are:

   * String type parameters, such as "aa" and "C:\" that are divided by semicolons. In this case, Logi Report Engine passes the string directly to the Exit function.
   * Logi Report predefined parameters used in the current report, which are introduced by the "@" symbol. In this case, Logi Report Engine passes the parameter to the Exit function.
7. Run the report and Logi Report Engine calls the class that you specify in the Report Inspector.

### Example 2: Using Formulas in the Exit Functions

You can use formulas in the Exit functions. To do this, you need to use the [Data Container Link](https://devnet.logianalytics.com/hc/en-us/articles/5735586301207-Setting-Up-Data-Container-Links-in-a-Report) feature that can return value of any formula to a parameter. Using the parameter in the Exit functions, you can get the value of the formula in the Exit functions.

1. Create a formula and insert it into a report. You should place the formula in the child data component.
2. Create a parameter with the same data type as the formula, leaving other options blank.
3. Insert the parameter into the parent data component.
4. Right-click the parent data component and select **Data Container Link** on the shortcut menu.
5. In the Data Container Link dialog box, select the **Return Value** tab, add the formula in the **Fields in Child Data Container** box to the **Return Value** box, then select **OK**.
   Now, you have finished passing value of the formula to a parameter.
6. Use this parameter in the Exit functions with the method described in [Example 1](#Example1). Logi Report Engine then returns the final value of the formula in the Exit functions.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9898402961815/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5735498221463-Running-the-Design-API-Samples)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9898402971543/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5735511625623-Applying-Security-Context-Support)
