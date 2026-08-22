---
title: "Applying a User Defined CSS to an HTML Output File"
id: 5741415075095
section: "Working with APIs Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741415075095-Applying-a-User-Defined-CSS-to-an-HTML-Output-File
updated_at: 2022-10-31T17:15:48Z
---

# Applying a User Defined CSS to an HTML Output File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394905879-Passing-Customized-Variables-to-User-Data-Source-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415347351-Specifying-Parameter-Values)

# Applying a User Defined CSS to an HTML Output File

When you export a report to HTML, Logi Report generates a .css file automatically to control the appearance and layout of the output file. You can apply your own .css file to the HTML output file when you perform the export via the Server API. This topic describes the procedure for applying a user-defined CSS to the HTML output file of a report.

1. Open the report in Logi Report Designer.
2. Specify the CSS selector in your own CSS for objects in the report: select the object to which you want to apply the CSS, then in the Report Inspector, specify the selector in your .css file as the value of the External CSS Class Selector property.
3. [Publish the report](https://devnet.logianalytics.com/hc/en-us/articles/5741453495191-Publishing-Resources) to Logi Report Server.
4. Edit your JSP file that invokes the interface used to export the report to HTML.
5. Access the edited JSP file to export the report to HTML.

Server saves the demo JSP file **ApplyUserCSS.jsp** in `<install_root>\help\samples\JSPSamples\ApplyUserCSS` for your reference about the feature. You can copy the whole **ApplyUserCSS** folder to `<install_root>\public_html\jinfonet`, and then access the JSP via `http://host:port/jinfonet/ApplyUserCSS/ApplyUserCSS.jsp`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741394905879-Passing-Customized-Variables-to-User-Data-Source-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741415347351-Specifying-Parameter-Values)
