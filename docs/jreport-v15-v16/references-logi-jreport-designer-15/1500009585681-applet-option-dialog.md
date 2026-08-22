---
title: "Applet Option Dialog"
id: 1500009585681
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585681-Applet-Option-Dialog
updated_at: 2021-07-24T05:55:38Z
---

# Applet Option Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564542-Aggregate-On-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564582-Applet-Parameter-Dialog)

# Applet Option Dialog

The Applet Option dialog appears when you set the Default Format for Viewing Report property of a report tab to Applet and then select ![Choose button](https://devnet.logianalytics.com/hc/article_attachments/4404893790999/btn_chsr1.gif) in the value cell in the Report Inspector. It helps you to specify the parameters for running a report tab in Applet format. [See the dialog](javascript:%20void(null)).

![Applet Option dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889392023/apltoptn.gif)

The following are details about options in the dialog:

**Pop-up Window**

Specifies to show an Applet window when viewing a report.

**Zip Result**

Specifies to compress the result and its size would be smaller.

**Java Plug-in 1.2 for Windows**

Directs applets to run using Sun's 1.2 Java Runtime Environment (JRE).

**Java Plug-in 1.3 for Windows**

Directs applets to run using Sun's 1.3 Java Runtime Environment (JRE).

**Run Linked Report**

If the report is linked with other reports, you can check whether or not to generate the linked reports (not including the detail reports) in the Applet result. If you are only interested in the primary report, leave this option unchecked. Generating linked reports at the same time, especially when the linked reports contain a large amount of data, will cause performance issue.

**Note:** You'd better specify a file destination when exporting a report via Applet, such as `D:\folder\filename.pdf` in case you may not find the result. By default when exporting a report via Applet on Internet Explorer, the exported result will be located on the Desktop, and when on Firefox, it will be in its installation root.

If you do not have the Read or Write permission to the default location or the location you specified, you will get an access denied error. To handle this, add the required permission in jdk\jre\lib\security\java.policy that the applet uses:

For the default location "Desktop":

`permission java.util.PropertyPermission "user.dir", "read";   
 permission java.io.FilePermission "${user.home}${/}Desktop${/}*", "read,write";`

For user defined location:

`permission java.io.FilePermission "D:${/}temp${/}*", "read,write";`

**OK**

Applies the changes and closes the dialog.

**Cancel**

Cancels the changes and exits the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564542-Aggregate-On-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009564582-Applet-Parameter-Dialog)
