---
title: "Using the Exit Functions"
id: 4405664349591
section: "Working with APIs - Logi Report Designer v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405664349591-Using-the-Exit-Functions
updated_at: 2022-01-27T20:34:17Z
---

# Using the Exit Functions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661321239-Running-the-Design-API-Samples)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661323671-Applying-Security-Context-Support)

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

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420394642839/noteicon.jpg) You can apply the Exit functions to page reports only.

## Exit Function Properties

Open a page report in Designer, then in the Report Inspector, select the node that represents the report tab and you can find the three Exit function properties: After Init Parameter, After Run, and Before Run.

![Report Inspector panel](https://devnet.logianalytics.com/hc/article_attachments/4420410946199/wkapi_exitfctn_prpty.gif)

For more information about the three properties, see [Page Report Tab Properties](https://devnet.logianalytics.com/hc/en-us/articles/4405661880343-Page-Report-Tab-Properties#ExitFunction).

## Executive Interfaces of the Exit Functions

Logi Report provides you with three interfaces to implement the Exit functions.

**jet.util.JURLExecutor**

This interface contains the method *public boolean exec(String[] params) throws JURLExecuterException*. You can use it to get the status of Logi Report Engine and return a Boolean value. If the method returns "true", Logi Report Engine continues running; if it returns "false", Logi Report Engine stops at this point.

Parameter in the method:

* **params**  
  Array of strings. You need to define and parse each element by yourself. You can specify the PARAMETERs in the Report Inspector. If you do not specify any PARAMETERs, params.length is zero.

**jet.util.JURLEngineExecutor**

This interface contains the method *public boolean exec(String[] params, EngineExecutor executor) throws JURLExecutorException*. You can use it to get the status of Logi Report Engine and return a Boolean value. If the method returns "true", Logi Report Engine continues running; if it returns "false", Logi Report Engine stops at this point.

Parameter in the method:

* **params**  
  Array of strings. You need to define and parse each element by yourself. You can specify the PARAMETERs in the Report Inspector. If you do not specify any PARAMETERs, params.length is zero.  
  executor - Executor of EngineExecutor, which is another interface Logi Report provides for exporting a report to HTML, TXT, or PDF within the Exit functions.

**jet.util.EngineExecutor**

This interface contains three methods:

* **public boolean exportToHtml(String htmlFileName, boolean bChartApplet, boolean isMultiFile, boolean bUsingTable, boolean bHyperlink, boolean bPageNum, boolean bAbsolute, int iBrowser)**  
  You can use this method to export the report to HTML and return a Boolean value for the exporting status. If the method exports the report successfully, it returns "true"; otherwise, it returns "false".

  Parameters in the method:

  + **HtmlFileName**  
    Full path of the HTML output file.
  + **bChartApplet**A Boolean value which specifies whether a chart in an HTML file is an applet. This parameter is deprecated and you should not use it.
  + **isMultiFile**  
    A Boolean value which specifies whether to generate the HTML output in one or multiple files.
  + **bUsingTable**  
    A Boolean value which specifies whether to use the HTML table format for exporting HTML files.
  + **bHyperLink**  
    A Boolean value which specifies whether to generate hyperlinks.
  + **bPageNum**  
    A Boolean value which specifies whether to generate page number.
  + **bAbsolute**  
    A Boolean value which specifies whether the font size is absolute or relative.
  + **iBrowser**  
    An int value which specifies whether the web browser is IE.
* **public boolean exportToPdf(String pdfFileName)**  
  You can use this method to export the report to PDF and return a Boolean value for the exporting status. If the method exports the report successfully, it returns "true"; otherwise, it returns "false".

  Parameter in the method:

  + **PdfFileName**  
    Full path of the PDF output file.
* **public boolean exportToText(String textFileName, boolean isNormalText, boolean isRepeat, char delimiter)**  
  You can use this method to export the report to Text and return a Boolean value for the exporting status. If the method exports the report successfully, it returns "true"; otherwise, it returns "false".

  Parameters in the method:

  + **TextFileName**  
    Full path of the text output file, where "true/false" sets whether the text file is of normal text format or of standard data format. A standard data format text file is a text file where each row represents a single record in a report. You can use it as a text data source for exchanging data with other applications.
  + **isNormalText**  
    A Boolean value which specifies whether a text file is in normal text format.
  + **isRepeat**  
    A Boolean value which specifies whether the contents are repeated.
  + **delimiter**  
    A character to be used in SDF (Standard Data Format). The method applies the delimiter only when the "true/false" parameter is set to "false". Delimiters can be ',' (the CSV format) or any other character. The default is a blank, which is the SSV format.

**Reference:** For API information, see the JURExecutor, JUREngineExecutor, and EngineExecutor interfaces in the jet.util package in the Logi Report Javadoc.

## Using the Exit Functions

Here are some tips for you when using the Exit functions:

* When you use a Logi Report parameter as the parameter of the Before Run function, the function returns no Logi Report parameter value, instead, the return value is the Logi Report parameter name with the "@" symbol.
* If you want to use Logi Report parameters as the Exit function parameters, you must use them in a report; otherwise, the function returns no value.
* When you want to publish a report that applies the Exit functions to Server and run it there, you should publish both the report and the catalog file to Server. In addition, you should add the path to the *-classpath* option in the batch file that starts Server.
* You can also apply formulas in the Exit functions by using [returning values](https://devnet.logianalytics.com/hc/en-us/articles/4405664401431-Working-with-Subreports#Value) in subreports. In this case, you need to pass value of a formula in the subreport to a parameter in the primary report.

The following two examples show using the Exit functions to achieve specific goals.

### Example 1: Using Parameters in the Exit Functions

In this example, we provide a simple application which runs at all the three points, Before Run, After Init Parameter, and After Run.

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
3. Modify the batch file **setenv.bat** in `C:\LogiReport\Designer\bin` by appending the path `C:\LogiReport\Designer\help` into the batch file's ADDCLASSPATH variable:

   `set ADDCLASSPATH=%JAVAHOME%\lib\tools.jar;C:\LogiReport\Designer\help;`
4. Start Designer.
5. Open a page report with parameter.
6. In the Report Inspector, select the node that represents the report tab and specify the class and give parameters for the three functions, for example:

   ![Report Inspector Panel](https://devnet.logianalytics.com/hc/article_attachments/4420410949655/wkapi_exitfctn_use.gif)

   **JURL:/** - The standard format, and followed by the class name.  
   **testa** - The class name in this example.  
   **aa;bb;cc** and **123;234;345** - The string type parameters of the class, which are divided by semicolons.  
   **Param** - A predefined Logi Report parameter used in the current report, which is introduced by the "@" symbol.

   As described earlier in this topic, Designer supports two types of the Exit function parameters. They are:

   * String type parameters, such as "aa" and "C:\". In this case, Logi Report Engine passes the string directly to the Exit function.
   * Logi Report predefined parameters used in the current report, which are introduced by the "@" symbol. In this case, Logi Report Engine passes the parameter to the Exit function.
7. Run the report and Logi Report Engine calls the class that you specify in the Report Inspector.

### Example 2: Using Formulas in the Exit Functions

You can use formulas in the Exit functions. To do this, you need to use the [Data Container Link](https://devnet.logianalytics.com/hc/en-us/articles/4405664367511-Setting-Up-Data-Container-Links-in-Banded-Objects) feature which can return value of any formula to a parameter. Using the parameter in the Exit functions, you can get the value of the formula in the Exit functions.

1. Create a formula and insert it into a report. You should place the formula in the child data component.
2. Create a parameter with the same data type as the formula, leaving other options blank.
3. Insert the parameter into the parent data component.
4. Right-click the parent data component and select **Data Container Link** on the shortcut menu.
5. In the Data Container Link dialog box, select the **Return Value** tab, add the formula in the **Fields in Child Data Container** box to the **Return Value** box, then select **OK**.

   Now, you have finished passing value of the formula to a parameter.
6. Use this parameter in the Exit functions with the method described in Example 1. Logi Report Engine then returns the final value of the formula in the Exit functions.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420394625303/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405661321239-Running-the-Design-API-Samples)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420394625687/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405661323671-Applying-Security-Context-Support)
