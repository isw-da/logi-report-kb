---
title: "Applying a User-Defined CSS to HTML Result File"
id: 1500009643962
section: "Working With APIs Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009643962-Applying-a-User-Defined-CSS-to-HTML-Result-File
updated_at: 2021-07-24T20:55:30Z
---

# Applying a User-Defined CSS to HTML Result File

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668681-Loading-User-Data-Source-Classes-at-Runtime)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668741-Specifying-Parameter-Values)

# Applying a User-Defined CSS to HTML Result File

When exporting a report to HTML format, a .css file will be generated automatically by Logi JReport to control the appearance and layout of the result file. When exporting a report to HTML format with Server API, Logi JReport enables you to apply your own .css file to the HTML result file.

**To apply user-defined CSS to HTML result file:**

1. In Logi JReport Designer, specify the CSS selector in your own CSS for report objects.

   Select the object which you want to apply in your own CSS, and in Report Inspector, specify a value for the CSS property External CSS Class Selector. The value of the property should be the selector in your .css file.
2. Publish the report to Logi JReport Server (for details, see [Publishing Resources](https://devnet.logianalytics.com/hc/en-us/articles/1500009673621-Publishing-Resources)).
3. Edit your JSP file that invokes the interface used to export the report to HTML format.
4. Export the report to HTML format using Logi JReport Server.

Logi JReport provides a demo JSP file ApplyUserCSS.jsp which is stored in `<install_root>\help\samples\JSPSamples\ApplyUserCSS` for your reference. You can copy the whole ApplyUserCSS folder to `<install_root>\public_html\jinfonet`, then

access the JSP via `http://host:port/jinfonet/ApplyUserCSS/ApplyUserCSS.jsp`.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009668681-Loading-User-Data-Source-Classes-at-Runtime)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009668741-Specifying-Parameter-Values)
