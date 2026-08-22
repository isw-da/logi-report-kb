---
title: "Applying a User Defined CSS to an HTML Result File"
id: 1500009771001
section: "Using the Server API"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009771001-Applying-a-User-Defined-CSS-to-an-HTML-Result-File
updated_at: 2021-07-24T00:49:38Z
---

# Applying a User Defined CSS to an HTML Result File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743162-Passing-Customized-Variables-to-User-Data-Source-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771181-Specifying-Parameter-Values)

# Applying a User Defined CSS to an HTML Result File

When you export a report to HTML format, Logi Report generates a .css file automatically to control the appearance and layout of the result file. You can apply your own .css file to the HTML result file when you perform the export via the Server API. This topic describes the procedure for applying a user-defined CSS to the HTML result file of a report.

1. Open the report in Logi Report Designer and specify the CSS selector in your own CSS for objects in the report as follows: select the object to which you want to apply the CSS, then in the Report Inspector, specify the selector in your .css file as the value of the External CSS Class Selector property.
2. [Publish the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009777241-Publishing-Resources) to Logi Report Server.
3. Edit your JSP file that invokes the interface used to export the report to HTML format.
4. Access the edited JSP file to export the report to HTML.

Report Server saves the demo JSP file **ApplyUserCSS.jsp** in `<install_root>\help\samples\JSPSamples\ApplyUserCSS` for your reference about the feature. You can copy the whole **ApplyUserCSS** folder to `<install_root>\public_html\jinfonet`, and then access the JSP via `http://host:port/jinfonet/ApplyUserCSS/ApplyUserCSS.jsp`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009743162-Passing-Customized-Variables-to-User-Data-Source-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009771181-Specifying-Parameter-Values)
