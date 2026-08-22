---
title: "Applying a User Defined CSS to an HTML Result File"
id: 1500009744281
section: "Work With APIs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009744281-Applying-a-User-Defined-CSS-to-an-HTML-Result-File
updated_at: 2021-07-25T07:20:24Z
---

# Applying a User Defined CSS to an HTML Result File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744381-Loading-User-Data-Source-Classes-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744421-Specifying-Parameter-Values)

# Applying a User Defined CSS to an HTML Result File

When you export a report to HTML format, a .css file will be generated automatically by Logi Report to control the appearance and layout of the result file. If you perform the export via the Server API, Logi Report allows you to apply your own .css file to the HTML result file.

See the main steps for applying a user defined CSS to the HTML result file of a report:

1. Open the report in Logi Report Designer to specify the CSS selector in your own CSS for objects in the report as follows: select the object which you want to apply the CSS, then in the Report Inspector, specify the selector in your .css file as the value of the External CSS Class Selector property.
2. [Publish the report](https://devnet.logianalytics.com/hc/en-us/articles/1500009750101-Publishing-Resources) to Logi Report Server.
3. Edit your JSP file that invokes the interface used to export the report to HTML format.
4. Access the edited JSP file to export the report to HTML.

The demo JSP file ApplyUserCSS.jsp stored in `<install_root>\help\samples\JSPSamples\ApplyUserCSS` is provided for your reference about the feature. You can copy the whole ApplyUserCSS folder to `<install_root>\public_html\jinfonet`, then access the JSP via `http://host:port/jinfonet/ApplyUserCSS/ApplyUserCSS.jsp`.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009744381-Loading-User-Data-Source-Classes-at-Runtime)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009744421-Specifying-Parameter-Values)
