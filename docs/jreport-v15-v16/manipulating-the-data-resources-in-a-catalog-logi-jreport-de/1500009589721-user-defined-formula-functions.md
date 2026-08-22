---
title: "User Defined Formula Functions"
id: 1500009589721
section: "Manipulating the Data Resources in a Catalog - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009589721-User-Defined-Formula-Functions
updated_at: 2021-07-24T05:54:35Z
---

# User Defined Formula Functions

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568342-DBArray-in-Formulas)

# User Defined Formula Functions

When the built-in functions do not satisfy your requirements, you can design your own formula functions. Logi JReport provides you with an interface to build your own user defined formula (UDF) functions. You first write the code to implement a function, and then import it as a class when you build a formula.

However, when you want to develop a Java file to implement a function, only the following data types can be used for interacting with Logi JReport products (pass parameters and return parameters): DbBigInt, DbDouble, fCurrency, DbBit (using for boolean type), DbChar (using for String), DbDate, DbTime, DbTimestamp, DbBinary, fText (using for Long VarChar), fImage (using for long VarBinary), fIntArray, fNumArray, fCurArray, fBoolArray, fStrArray, fDateArray, fTimeArray, fDateTimeArray, fBinaryArray, fTextArray, fImageArray, fIntRange, fNumRange, fCurRange, fBoolRange, fStrRange, fDateRange, fTimeRange, fDateTimeRange. All the data types that start with 'f' belong to the package jet.formula.\*. The other data types belong to the package jet.connect.\*. For details, refer to Logi JReport Javadoc jet.formula and jet.connect packages in `<install_root>\help\api`.

Below is a list of the sections covered in this topic:

> * [Importing UDF Classes](#Import)
> * [Using UDF Functions](#Use)
> * [Example of Using UDF Functions](#Example)

## Importing UDF Classes

To import a user defined formula class, follow the steps below:

1. Develop your own Java program that implements the functions you need.
2. Compile the Java program and add it to the ADDCLASSPATH variable of the batch file setenv.bat/setenv.sh in `<install_root>\bin` on both Logi JReport Designer and Logi JReport Server.
3. Start Logi JReport Designer and open the Formula Editor.
4. Import your class file in either of the following two ways:
   * **Using the "import" statement:** 

     `import instName from "ClassName";`

     Where,

     + instName is the instance name that you give when you load the class. It is a global variable, you can use it in your formulas in the current data source.
     + ClassName is the class name defined in your class file. If the class file is put in the package jet.formula.javaformula, only the class name is required. However, if it is in your own package, you must specify the qualify name of the class.

       For example, the following declaration assumes the class MyFunctions is in package jet.formula.javaformula:

       `import myfunc from "MyFunctions";`

       And the following declaration allows user defined UDF class in any package, supposing the class is com.mycom.MyFunctions:

       `import myfunc from "com.mycom.MyFunctions";`

     **Notes:**

     + You should write the import statement only without anything else in a separate formula so as to avoid importing unwanted things.
     + You should avoid giving the same instance name when importing the same UDF.
   * **Using dialog:**
     1. In the Formula Editor, select **Menu** > **File** > **Import UDF Classes**.
     2. In the UDF Classes dialog, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif).
     3. In the Import UDF Class dialog, input the class name with full package path and then select **OK**.
     4. The class with package path is displayed. Select **OK**.

## Using UDF Functions

When your class is successfully imported, the functions defined in the class will be displayed in the UDF node in the Functions panel of the Formula Editor. You can then call the functions in a formula by double-clicking them or using the following statement:

`instName.MethodName(parameters);`

Where, MethodName is the method name in your class. You can call methods in your class as many times as you want by loading this class only once.

If you want to view the formula references of any UDF function, select the function and select **Menu** > **Formula** > **Formula References** on the toolbar, or right-click the function and select **Formula References** on the shortcut menu, then the UDF References dialog will be displayed, showing all the formulas that reference the UDF function if there are.

## Example of Using UDF Functions

In this example, a demo Java program MyFunctions.java which is put in the package jet.formula.javaformula will be used to illustrate how to write record data to a file using UDF functions. You can get the Java source file from `<install_root>\help\samples\APIUDFormula\jet\formula\javaformula`.

Take the following steps:

1. Compile this Java file to generate the class file (make sure that the path of the file JREngine.jar is before that of the file report.jar).

   `javac -classpath "<install_root>\lib\JREngine.jar;<install_root>\lib\report.jar;" MyFunctions.java`
2. Edit the batch file setenv.bat in `<install_root>\bin`.

   When you add class path, just add the root path. For example, suppose that the class file is located in `C:\Logi JReport\Designer\help\samples\APIUDFormula\jet\formula\javaformula`, you can append `C:\Logi JReport\Designer\help\samples\APIUDFormula` into the ADDCLASSPATH variable in the batch file.
3. Start Logi JReport Designer with the modified batch file.
4. Create a new formula to load this class and open a file on disk by calling the methods in MyFunctions.java. Here we define the formula (fmlA) to load the class and call the method to open a temp file:  

   `pagenumber;  
    import myfunc from "MyFunctions";  
    global integer filehandle = myfunc.openfile("e:\\test\\data.txt", false);`

   **Note:** If the class file is in your own package com.mycom other than jet.formula.javaformula, import the class in a formula as follows:

   `import myfunc from "com.mycom.MyFunctions";`
5. Compose a formula (fmlB) to call the method to write data into the temp file:  

   `string contents ="";  
    contents = @"Customer Name"+"\t"+ @Country+"\t"+ @Phone + "\t"+ PageNumber + "\n";  
    myfunc.write(filehandle, contents);`

   The return value of the last statement is the formula result.
6. Compose another formula (fmlC) to close the temp file:  

   `PageNumber;  
    myfunc.closefile(filehandle);`

   If the statement PageNumber is added to the formula, the formula will be calculated after the page break, which means that the calculation point is controlled. For more information, see [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels).
7. We have now defined three formulas (fmlA, fmlB, fmlC) in the above three steps. You can use it in a report as with a normal one.

**Note:** Now in Logi JReport, the '8859-1' encoding is not required any more and the UDF functions you define should be able to return the correct unicode strings. Thus, if you have UDF functions created in previous Logi JReport versions which still return '8859-1' encoded strings, you may need to modify them to make them return unicode strings.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009589661-Creating-a-Formula)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009568342-DBArray-in-Formulas)
