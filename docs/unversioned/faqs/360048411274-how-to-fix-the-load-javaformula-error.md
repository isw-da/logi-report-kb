---
title: "How to Fix the \"Load javaFormula\" Error"
id: 360048411274
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048411274-How-to-Fix-the-Load-javaFormula-Error
updated_at: 2020-07-27T23:13:18Z
---

# How to Fix the "Load javaFormula" Error

There are three common scenarios where this error can occur:

1. **JDK version is incorrect:**
   * **Solution:** If a report contains a formula, then the environment variable **JAVA\_HOME** must use a JDK target rather than a JRE target. JAVAC is required to compile the formula, but the report (without formula) and server can run with JRE.
   * **Note 1:** The JDK version for running formulas must be the same version as the one used for compiling them.
   * **Note 2:** Make sure you have pointed the **JAVAHOME** to a JDK target instead of JRE target, check the setenv.bat/.sh file under the %report\_home/bin folder  
     **Example:**  
     set JAVAHOME=C:\Program Files\Java\jdk1.7.0\_51
2. **Temp path does not exist:**
   * **Solution:** Make sure that the TempPath exists.
   * **Note:** TempPath is a variable in report.ini file located under %installroot%\bin folder. This points to the temp folder of Logi Report Server which is used to store the compiled java formula class files at runtime.
3. **Formula not displaying in the correct format:**
   * **Solution:** Make sure the formula is displaying in the correct format which matches its return value.
   * **Example:** You may create a formula that returns a string first; the format of the formula is being displayed in the report as "xxxxxxxxx", which is the general format for strings. Later, you change the formula definition to make it return a number instead, but you do not delete/re-insert this formula into the report, to reflect the correct new format (e.g., "#,00"), but the report still remembers "xxxxxxxxx", which could cause error at runtime.
