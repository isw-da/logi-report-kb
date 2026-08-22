---
title: "Using JSPs to Print Page Reports"
id: 1500009649482
section: "Page Report Studio Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009649482-Using-JSPs-to-Print-Page-Reports
updated_at: 2021-07-24T20:53:53Z
---

# Using JSPs to Print Page Reports

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649502-Opening-Multiple-Reports-in-One-Session)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674081-Advanced-Exporting-with-JSPs)

# Using JSPs to Print Page Reports

Logi JReport Server provides the following demo JSPs which enable you to print a page report without any view in the client side, and they are available in `<install_root>\help\samples\JSPSamples\PrintReport`.

* **printDemo.jsp**  
   Provides frames to load printCustomerlist.jsp and printReport.jsp.
* **printCustomerlist.jsp**  
   Shows how to set parameters for printing the demo report CustomerAnalysis.cls by using the ViewerApplet. This JSP calls printReport.jsp. If you want to print the other reports, you can follow this JSP file as an example to write your own JSP. In your own JSP, you should modify the values of "cat" and "rptName".

  `String cat = "/SampleReports/SampleReports.cat"; //request.getParameter(APIConst.TAG_CATALOG);  
   String rptName = "/SampleReports/CustomerAnalysis.cls"; //request.getParameter(APIConst.TAG_REPORT);`
* **printReport.jsp**  
   Shows how to print reports by using the ViewerApplet. The example JSP printCustomerlist.jsp calls this JSP.

Before running the JSPs, copy them to `<intall_root>\public_html\jinfonet`. Then, start Logi JReport Server and access printDemo.jsp using the URL `http://localhost:8888/jinfonet/printDemo.jsp`. The following page appears:

![](https://devnet.logianalytics.com/hc/article_attachments/4404920433303/pgrpt_jspprint.gif)

**PrintInCurrentFrame**

Specifies to call printReport.jsp and load applet of Page Report Studio Frame.

**PrintInHiddenFrame**

Specifies to call printReport.jsp without loading applet of Page Report Studio Frame.

**Reset**

Resets the previous options.

**View**

Views this report.

**Interactive**

If checked, you could specify the print setup in the Print dialog.

**Background**

If checked, the print job will run in the background.

**UseJDK1.1**

If checked, you will use instance PrintJob of JDK11 to print the report.

**Wait**

If checked, you have to wait until the print job is finished.

**SeparateLargePage**

If checked, the large page will be separated into several pages automatically.

**NotifyComplete**

This parameter is used with the parameter wait. After the print job is finished, a box will pop up to note you, and you could do any other work instead of keep on waiting.

**Printer**

Specifies the printer to implement the print job.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009649502-Opening-Multiple-Reports-in-One-Session)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009674081-Advanced-Exporting-with-JSPs)
