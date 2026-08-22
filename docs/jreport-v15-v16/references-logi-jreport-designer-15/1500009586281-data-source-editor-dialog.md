---
title: "Data Source Editor Dialog"
id: 1500009586281
section: "References - Logi JReport Designer 15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009586281-Data-Source-Editor-Dialog
updated_at: 2021-07-24T05:55:29Z
---

# Data Source Editor Dialog

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565122-Data-Source-Drivers-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586261-Display-Attributes-Dialog)

# Data Source Editor Dialog

The Data Source Editor appears when you select the New button, or select a data source driver and then select Edit in the [Data Source Drivers](https://devnet.logianalytics.com/hc/en-us/articles/1500009565122-Data-Source-Drivers-Dialog) dialog. It allows you to simplify using cached query results by [adding or editing a data source driver](https://devnet.logianalytics.com/hc/en-us/articles/1500009570622-Cached-Query-Results#Manage) in a Logi JReport catalog. [See the editor](javascript:%20void(null)).

![Data Source Editor dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893825047/dtsrcedtr.gif)

The following are details about options in the editor.

**Driver Name**

Specifies the name you want to use for the data source driver.

**URL**

Specifies the URL of the driver definition.

The URL is composed of three parts: scheme, qualified class name and arguments. If the Data Source Driver does not use arguments, the argument part will not appear on the URL. Its syntax is: URL = "jrquery" ":" "/" qualified\_classname[ ";" params].

**Driver**

Selects to specify the driver configuration if you don't specify the URL.

* **Scheme**  
   Specifies the scheme of the driver. Presently only "jrquery" is available.
* **Class Name**  
   Specifies the qualified class name.
* **Parameters**  
   Specifies the arguments for the Data Source Driver. In the parameters field, the arguments should be separated by semicolons (";").

**OK**

Accepts the changes and closes the dialog.

**Cancel**

Does not retain changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009565122-Data-Source-Drivers-Dialog)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009586261-Display-Attributes-Dialog)
