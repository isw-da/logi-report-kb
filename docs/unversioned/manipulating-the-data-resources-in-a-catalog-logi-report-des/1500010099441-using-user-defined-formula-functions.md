---
title: "Using User-Defined Formula Functions"
id: 1500010099441
section: "Manipulating the Data Resources in a Catalog - Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099441-Using-User-Defined-Formula-Functions
updated_at: 2022-04-29T03:24:03Z
---

# Using User-Defined Formula Functions

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties)

# Using User-Defined Formula Functions

When you create formulas in a catalog, if the [built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions) do not satisfy your requirements, you can design your own formula functions by using the User Defined Function Editor or importing them from Java files. This topic describes how you can create and import user-defined functions and use them in formulas.

This topic contains the following sections:

* [Creating User-Defined Functions in a Catalog](#Create)
* [Importing User-Defined Functions from Java Files](#Import)
* [Using User-Defined Functions](#Use)
  + [Example of Using Imported UDF](#Example)

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) You cannot apply user-defined functions saved in a catalog in [dynamic formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500010101361-Using-Dynamic-Resources-and-Local-Parameters-in-Reports). If you want to do this, you need to create the user-defined functions via the dynamic resource list.

## Creating User-Defined Functions in a Catalog

1. [Open the required catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500010056622-Creating-Opening-and-Saving-Catalogs#Open).
2. In the Catalog Manager, expand the data source in which to create the function, then:
   * Select the **User Defined Functions** node or any existing function in the data source and select **New Function** on the toolbar.
   * Right-click the **User Defined Functions** node in the data source and select **New Function** on the shortcut menu.
3. In the Enter Function Name dialog box, provide a name for the function and select **OK**. Designer displays the [User Defined Function Editor dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099101-User-Defined-Function-Editor-Dialog-Box).

   ![User Defined Function Editor](https://devnet.logianalytics.com/hc/article_attachments/4404856869399/udfedtr.gif)
4. Compose the function by selecting the required fields from the **Fields** panel (including DBFields, formulas, summaries, and [parameters](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog#RefParam) in the current catalog data source, as well as [some special fields](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog#RefSpecial)), functions from the **Functions** panel (including [built-in functions](https://devnet.logianalytics.com/hc/en-us/articles/1500010093961-Appendix-1-Formula-Functions) and other user-defined functions), and [operators](https://devnet.logianalytics.com/hc/en-us/articles/1500010093981-Appendix-2-Formula-Operators) from the **Operators** panel. When the predefined user-defined functions, summaries, and parameters cannot meet you requirement, you can create new function, [summary](https://devnet.logianalytics.com/hc/en-us/articles/1500010061062-Working-with-Summaries#Predefine), and [parameter](https://devnet.logianalytics.com/hc/en-us/articles/1500010099761-Creating-Parameters-in-a-Catalog) to be referenced by the function using the New XXX option on the toolbar. Designer then saves the newly created objects into the same catalog data source as the function. You can also write the function by yourself in the editing panel.

   The function syntax is as follows:

   arguments: VariableType1 VariableName1, VariableType2 VariableName2, ...;

   For example, `arguments: integer age, string name;`

   An argument works the same as a local variable except that you cannot assign any value to it, like `arguments: integer age=10;`. For more information about the syntax, see [Formula Syntax](https://devnet.logianalytics.com/hc/en-us/articles/1500010061042-Formula-Syntax).
5. Make use of the buttons on the toolbar above the editing panel to edit the function. To comment a line, select the **Comment/Uncomment** button ![Comment/Uncomment button](https://devnet.logianalytics.com/hc/article_attachments/4404856869783/btn_cmtuncmnt.gif) on the toolbar. If you want to bookmark a line so that you can search for it easily later, select the **Add Bookmark** button ![Add Bookmark button](https://devnet.logianalytics.com/hc/article_attachments/4404856870039/btn_bkmrk.gif). To check whether or not the syntax of your function is correct, select the **Check** button ![Check button](https://devnet.logianalytics.com/hc/article_attachments/4404856870295/btn_check.gif).
6. Save the function and close the editor.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg)

* When you refer to any field in a user-defined function, you need to add the "@" symbol as the prefix of the field's reference name. If the field name contains spaces, you need to quote the reference name with double quotation marks (""). For example, if the field name is Customer Name, the reference name is @"Customer Name".
* When user-defined functions reference display names or mapping names, the names should not contain any of following characters if you do not quote the names using double quotation marks:

  "~", "`", "!", "@", "#", "$", "%", "^", "&", "\*", "(", ")", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", "\", " ' ", "<", ",", ">", ".", "?", "/"

  Examples:

  + Expression `@Customer#;` causes a syntax error, but `@"Customer#"` is correct.
  + If a field has the display name Category.Measure, when you add it to a user-defined function, quote it as "Category.Measure" or "Category"."Measure".
* Logi Report limits the number of the "if-else" statements to 190. When this number is reached, you should use the "select-case" statement instead.

## Importing User-Defined Functions from Java Files

To import a user-defined function, you first need to develop a Java file to implement a function, and then import it as a class. You can use the following data types for interacting with the Logi Report products (passing parameters and returning parameters): DbBigInt, DbDouble, fCurrency, DbBit (using for Boolean type), DbChar (using for String), DbDate, DbTime, DbTimestamp, DbBinary, fText (using for Long VarChar), fImage (using for Long VarBinary), fIntArray, fNumArray, fCurArray, fBoolArray, fStrArray, fDateArray, fTimeArray, fDateTimeArray, fBinaryArray, fTextArray, fImageArray, fIntRange, fNumRange, fCurRange, fBoolRange, fStrRange, fDateRange, fTimeRange, and fDateTimeRange. All the data types that start with "f'" belong to the "jet.formula.\*" package; the other data types belong to the "jet.connect.\*" package. For more information, see the jet.formula and jet.connect packages in the Logi Report Javadoc.

1. Develop your own Java program that implements the functions you need.
2. Compile the Java program and add it to the ADDCLASSPATH variable of the batch file **setenv.bat**/**setenv.sh** in `<install_root>\bin` of both Designer and Server.
3. Start Designer and open the Formula Editor or User Defined Function Editor dialog box.
4. Import your class file in either of the following two ways:

   + **Using the "import" statement:** 

     `import instName from "ClassName";`

     Where,

     - "instName" is the instance name that you give when you load the class. It is a global variable. You can use it in formulas and user-defined functions in the current catalog data source.
     - "ClassName" is the class name defined in your class file. If you put the class file in the jet.formula.javaformula package, you only need to provide the class name; however, if it is in your own package, you must specify the qualify name of the class.

       For example, the following declaration assumes the class MyFunctions is in the jet.formula.javaformula package:

       `import myfunc from "MyFunctions";`

       And the following declaration allows user-defined UDF class in any package, supposing the class is com.mycom.MyFunctions:

       `import myfunc from "com.mycom.MyFunctions";`

     ![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif)

     - You should write the "import" statement only without anything else in a separate formula or user-defined function so as to avoid importing unwanted things.
     - You should avoid giving the same instance name when importing the same UDF.  
   * **Using dialog box:** 
     1. In the Formula Editor or User Defined Function Editor dialog box, select **Menu** > **File** > **Import UDF Classes**. Designer displays the [UDF Classes dialog box](https://devnet.logianalytics.com/hc/en-us/articles/1500010099081-UDF-Classes-Dialog-Box).

        ![UDF Classes dialog box](https://devnet.logianalytics.com/hc/article_attachments/4404848471063/udfcls.gif)
     2. Select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404848403095/btn_add.gif), then in the Import UDF Class dialog box, type in the class name with full package path and select **OK**.
     3. Designer displays the class with the package path in the UDF Classes dialog box. Select **OK**.

## Using User-Defined Functions

In the Functions panel of the Formula Editor and User Defined Function Editor, you can find the user-defined functions created using the User Defined Function Editor under the User Defined Functions node and those imported from Java files under the UDF node. You can then call the functions when creating formulas or user-defined functions by double-clicking them.

Suppose a user-defined function named "function1" is `arguments: integer age, string name;`, you can call it as follows:

* `@function1(25, "John Smith");`
* `@'function1'(25, "John Smith");`
* `@"function1"(25, "John Smith");`

For imported UDFs, you can also call them using the following statement:

`instName.MethodName(parameters);`

Where, "MethodName" is the method name in your class. You can call methods in your class as many times as you want by loading this class only once.

The following shows an example. First, a user-defined function named "function2" calls an imported UDF:

`Import a from jet.formula.javaformula.UDF;  
arguments: string countries;  
return a.getvalue(@country, @amount, countries);`

Then a formula calls "function2":

`@function2("USA, China")`

You can view the formula references of an imported UDF in the Formula Editor. Select the function and select **Menu** > **Formula** > **Formula References** on the toolbar, or right-click the function and select **Formula References** on the shortcut menu, then Designer displays the UDF References dialog box, showing all the formulas that reference the imported UDF if there are.

### Example of Using Imported UDF

In this example, we use a demo Java program MyFunctions.java which is put in the jet.formula.javaformula package to illustrate how to write record data to a file using UDF functions. You can get the Java source file from `<install_root>\help\samples\APIUDFormula\jet\formula\javaformula`.

Take the following steps:

1. Compile the Java file **MyFunctions.java** to generate the class file (make sure that the path of the file **JREngine.jar** is before that of the file **report.jar**).

   `javac -classpath "<install_root>\lib\JREngine.jar;<install_root>\lib\report.jar;" MyFunctions.java`
2. Edit the batch file **setenv.bat** in `<install_root>\bin`.

   When you add class path, just add the root path. For example, suppose that the class file is located in `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help\samples\APIUDFormula\jet\formula\javaformula`, you can append `C:\(Undefined variable: Logi_Variables.LogiReport)\Designer\help\samples\APIUDFormula` into the ADDCLASSPATH variable in the batch file.
3. Start Designer.
4. Create a new formula to load this class and open a file on disk by calling the methods in MyFunctions.java. Here we define the formula "fmlA" to load the class and call the method to open a temp file:  

   `pagenumber;  
    import myfunc from "MyFunctions";  
    global integer filehandle = myfunc.openfile("e:\\test\\data.txt", false);`

   ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404856814359/noteicon.jpg) If the class file is in your own package com.mycom other than jet.formula.javaformula, you need to import the class in a formula as follows:

   `import myfunc from "com.mycom.MyFunctions";`
5. Compose a formula "fmlB" to call the method to write data into the temp file:  

   `string contents ="";  
    contents = @"Customer Name"+"\t"+ @Country+"\t"+ @Phone + "\t"+ PageNumber + "\n";  
    myfunc.write(filehandle, contents);`

   The return value of the last statement is the formula result.
6. Compose another formula "fmlC" to close the temp file:  

   `PageNumber;  
    myfunc.closefile(filehandle);`

   If you add "PageNumber" in the formula, Logi Report executes the formula after the page break, which means that the calculation point is controlled. For more information, see [Formula Levels](https://devnet.logianalytics.com/hc/en-us/articles/1500010061022-Formula-Levels).
7. We have now defined three formulas, fmlA, fmlB, fmlC. You can use them in a report as with a normal one.

![Critical icon](https://devnet.logianalytics.com/hc/article_attachments/4404856819991/criticalicon.gif) Designer does not require the "8859-1" encoding anymore and the UDF functions you define should be able to return the correct unicode strings. Thus, if you have UDF functions created in previous Designer versions which still return "8859-1" encoded strings, you may need to modify them to make them return unicode strings.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010060982-Creating-Formulas-in-a-Catalog)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010061002-Using-Formulas-to-Control-Object-Properties)
