---
title: "Applying a User Defined CSS to an HTML Output File"
id: 45203849504397
section: "Working with APIs Report Server"
category: "Logi Report"
url: https://logi-report-v26.insightsoftware.com/hc/en-us/articles/45203849504397-Applying-a-User-Defined-CSS-to-an-HTML-Output-File
updated_at: 2026-04-30T14:07:46Z
source_host: logi-report-v26.insightsoftware.com
---
# 
Applying a User Defined CSS to an HTML Output File 

When you export a report to HTML, Report generates a .css file automatically to control the appearance and layout of the output file. You can apply your own .css file to the HTML output file when you perform the export via the Server API. This topic describes the procedure for applying a user-defined CSS to the HTML output file of a report.

- Open the report in Report Designer.

- Specify the CSS selector in your own CSS for objects in the report: select the object to which you want to apply the CSS, then in the Report Inspector, specify the selector in your .css file as the value of the External CSS Class Selector property.
            

- 
Publish the report to Report Server.
			

- Edit your JSP file that invokes the interface used to export the report to HTML.
			

- Access the edited JSP file to export the report to HTML.
            

Server saves the demo JSP file ApplyUserCSS.jsp in <install_root>\help\samples\JSPSamples\ApplyUserCSS for your reference about the feature. You can copy the whole ApplyUserCSS folder to <install_root>\public_html\jinfonet, and then access the JSP via http://host:port/jinfonet/ApplyUserCSS/ApplyUserCSS.jsp.
