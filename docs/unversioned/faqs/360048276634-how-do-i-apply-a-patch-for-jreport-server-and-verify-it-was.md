---
title: "How do I apply a patch for JReport Server and verify it was applied successfully?"
id: 360048276634
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360048276634-How-do-I-apply-a-patch-for-JReport-Server-and-verify-it-was-applied-successfully
updated_at: 2020-07-27T22:33:49Z
---

# How do I apply a patch for JReport Server and verify it was applied successfully?

**Overview:**

Logi Support will inform you when a patch is available to fix a product bug/issue.  There are two scenarios: Logi Report Server as stand-alone or embedded into a J2EE server.  Follow the steps outlined below to apply the patch for the scenario that matches your installation type.

**Stand-alone Mode:**

1. Save the patch onto the same machine where Logi Report Server is running.
2. Edit the startup script of Logi Report Server to include the patch with its full path as the very first item in the classpath.  Example:

```
:LabelRUN  
@call "%ENVHOME%"setenv.bat  
  
set CLASSPATH=C:\patch\JIP_S_xxxxxxxx.jar;%REPORTHOME%\derby\lib\*;%REPORTHOME%\resources\common;%REPORTHOME%\lib\plugin.jar;%REPORTHOME%\lib\JREngine.jar;%REPORTHOME%\lib\JRESServlets.jar;%REPORTHOME%\lib\JRStructuredEngine.jar;
```

      3.  If the patch also contains "public\_html" folder, please also extract it to %installroot\_LogiReportServer%\public\_html folder to overwrite the current files.  
      4.  Restart Logi Report Server.  
  
**Embedded Mode:**

1. Create a folder named "classes" under **/ContextRoot<war\_filename>/WEB-INF** folder (please make sure the "classes" folder is a sibling to the "lib" folder).
2. Extract the patch JIP\_S\_xx\_xx\_xxxxxxxx.jar.
3. Copy all the folders excluding the "public\_html" folder from the extracted folder into the "classes" folder.
4. Back up the files/folders located in /ContextRoot, and then copy the folders and files under /public\_html into /ContextRoot.  Overwrite any files and folders that already exist.
5. Clear the cache under your web application server.
6. Clear the browser cache before attempting to run a report.

To verify whether the patch has been successfully applied, please follow the steps below:  
  
      1.  Open the **LogConfig.properties** under %installroot\_LogiReportServer%\bin folder or                      %reporthome\_LogiReportServer%\bin folder, and set the event logging level to "TRIVIAL":  logger.Event.level = TRIVIAL.  
      2.  Restart JReport Server, and then check the event.log after a restart.  If you see the following message in the log, then the patch has been installed correctly:  The patch JIP\_S\_xxxxxxxxxx.jar has been installed successfully!
