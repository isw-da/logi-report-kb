---
title: "Adding Objects in Page Report"
id: 4405690648471
section: "Page Report Studio Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690648471-Adding-Objects-in-Page-Report
updated_at: 2022-01-27T07:59:42Z
---

# Adding Objects in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683960343-Making-Simple-Modifications-to-Page-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683962775-Applying-Web-Controls-in-Page-Report)

# Adding Objects in Page Report

You can add labels, images, banded objects, tables, crosstabs, charts, special fields, and web controls to page reports. This topic describes how you can insert objects in page reports and where you can place the objects.

However, for page reports that you created in Logi Report Designer, you can add objects to them only when the corresponding catalog contains business views.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/4405683899543-Logi-Report-Licenses#ServerLive) to use this feature. For more product information, including new purchases and upgrades, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

**Object placement**

You can place objects within banded objects, tables, tabulars, as well as onto an empty area of a report. The following table lists the report areas that are valid targets for the various objects, listed on the left.

|  | Report Layout Area | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Object | Page Header/Footer | Report Header/Footer | Report Body | Banded Detail | Banded Page Header/Footer | Banded Header/Footer | Banded Group Header/Footer | Table Cell | Tabular Cell |
| Banded object | Y | N | Y | Y | Y | Y | Y | N | Y |
| Chart | Y | Y | Y | Y | Y | Y | Y | N | Y |
| Crosstab | Y | Y | Y | Y | Y | Y | Y | N | Y |
| Table | Y | Y | Y | Y | Y | Y | Y | N | Y |
| Group object | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Detail object | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Aggregation object | N | N | Y | N | N | Y | Y | N | N |
| Formula | Y | Y | Y | Y | Y | Y | Y | Y | Y |
| Label | Y | N | Y | Y | Y | Y | Y | Y | Y |
| Special field | Y | N | Y | Y | Y | Y | Y | Y | Y |
| Image | Y | N | Y | Y | Y | Y | Y | Y | Y |
| Web control | Y | Y | Y | Y | Y | Y | Y | N | Y |

**To add an object into a report:**

1. Select **Menu** > **Insert**, then select the object you want to add.
2. Select the destination in the report where you want to add the object.
   * If you specify to add a label, Server inserts a label there. Edit the text of the label and format it.
   * If you specify to add a banded object, table, crosstab, or chart, Server displays the corresponding report wizard. Specify the settings in the wizard. For more information, see the specific topic in [Creating a Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/4405683950743-Creating-Page-Reports).
   * If you specify to add a special field, Server inserts the special field there. For more information, see Special Fields in the *Logi Report Designer Guide*.
   * If you specify to add a parameter control, parameter form control, or filter control, Server displays the corresponding insert control dialog box. For more information, see [Applying Web Controls in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/4405683962775-Applying-Web-Controls-in-Page-Report).
   * If you specify to add a navigation control, Server inserts a navigation control there. For more information, see [Applying Web Controls in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/4405683962775-Applying-Web-Controls-in-Page-Report).
   * If you specify to add an image, Server displays the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/4405683662743-Insert-Image-Dialog-Box-Properties) dialog box.
     Specify the source of the image file and the image you want, then select **OK**.

     ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4420447163031/insrtimg.gif)

     + **Local File**  
       Select this option if you want to use an image in the local disk. Then in the **File Name** text box, type the path and name of the image file in the local file system, or select **Browse** to locate the image file.
     + **Web URL**  
        Select this option if you want to use an image via URL. Then in the **Image URL** text box, type the URL of the image file. Server stores the latest 10 typed URLs in the drop-down list.  

       ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4420447034135/noteicon.jpg)If your Logi Report Server is in an intranet, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
     + **Library**  
        Select this option if you want to use an image in the server image library. Then select an image from the My Images box, which lists the images you have once inserted into reports.

Alternatively, you can also use the Toolbox panel to add objects other than special fields into a report by dragging them from the panel to the destination.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683960343-Making-Simple-Modifications-to-Page-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683962775-Applying-Web-Controls-in-Page-Report)
