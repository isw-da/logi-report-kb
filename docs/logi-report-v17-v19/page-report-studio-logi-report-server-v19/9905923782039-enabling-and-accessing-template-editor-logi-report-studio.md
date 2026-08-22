---
title: "Enabling and Accessing Template Editor Logi Report Studio"
id: 9905923782039
section: "Page Report Studio Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/9905923782039-Enabling-and-Accessing-Template-Editor-Logi-Report-Studio
updated_at: 2022-10-31T17:15:21Z
---

# Enabling and Accessing Template Editor Logi Report Studio

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483083159-Searching-for-Text-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462847767-Saving-a-Page-Report)

# This image notes any new content for version 19.2 of the product. For more information please see the Release Notes or What's New topics.Enabling and Accessing Template Editor Logi Report Studio

Logi Report provides a template editor - [Logi Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/9905923717783-Working-with-Logi-Report-Studio) for building reports more intuitively and conveniently. This topic describes how you can enable and access Logi Report Studio.

This topic contains the following sections:

* [Enabling Template Editor](#Enable)
* [Displaying the Template button on the Toolbar](#DisplayTemplate)
* [Accessing Template Editor](#Access)

## Enabling Template Editor

You need to enable the template editor to use it.

1. Add the JVM parameter `-Denable.tpleditor=true` in the Server startup file and then start Server.

   If you are an administrator, you can instead temporarily enable the template editor within your user session by running the URL <http://localhost:8888/studio/rpc/sysctl?enable.tpleditor=true> after you start a local Server.
2. Navigate to the My Profile > Customize Profile page on the Server Console.
3. Select **Customize Profile**. Server displays the Customize Profile dialog box.
4. Select **Enable Customize Properties**. You need to do this at least once.
5. Select **OK** to close the dialog box.

## Displaying the Template button on the Toolbar

You can select the Template button to access the template editor Logi Report Studio after you display the button on the toolbar of Page Report Studio.

To display the Template button on the toolbar in the Interactive View of Page Report Studio,

1. Navigate to **Menu** > **View** > **Options**. Server displays the [Options dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741411515543-Options-Dialog-Box-Properties).
2. Select **Customize**.

   ![Add Template to a Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905933210135/pgrpt_edit_tmplt_option.gif)
3. In the Available Tools box, select **Template**, which is at the end of the tools list.
4. Select the **Add** button ![Add Item button](https://devnet.logianalytics.com/hc/article_attachments/9905612569111/btn_additem.gif). Server displays **Template** in the Selected Tools box.
5. Select **OK**. You will find the Template button ![Template button](https://devnet.logianalytics.com/hc/article_attachments/9905933242007/btn_lrstd_tmplt.gif) on the toolbar.

   ![Template Icon on the Toolbar](https://devnet.logianalytics.com/hc/article_attachments/9905904898199/pgrpt_edit_tmplt_tlbr.gif)

## Accessing Template Editor

You can access the template editor Logi Report Studio by selecting the Template button ![Template button](https://devnet.logianalytics.com/hc/article_attachments/9905933242007/btn_lrstd_tmplt.gif) on the toolbar in the Interactive View of Page Report Studio. Server displays a message asking whether you want to leave the page. Select **Leave** after making sure you have saved any changes that you made to the report in Page Report Studio. Server then leaves Page Report Studio and displays Logi Report Studio.

![Logi Report Studio](https://devnet.logianalytics.com/hc/article_attachments/9905931573783/lrstudio.gif)

You can also open Logi Report Studio by selecting **Blank Template** when you [create a page report or report tab](https://devnet.logianalytics.com/hc/en-us/articles/5741469017879-Creating-Page-Reports).

![Select Blank Template](https://devnet.logianalytics.com/hc/article_attachments/9905904972567/pgrpt_edit_tmplt_blktmplt.gif)

For more information about how to use Logi Report Studio, see [Working with Logi Report Studio](https://devnet.logianalytics.com/hc/en-us/articles/9905923717783-Working-with-Logi-Report-Studio).

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741483083159-Searching-for-Text-in-Page-Report)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741462847767-Saving-a-Page-Report)
