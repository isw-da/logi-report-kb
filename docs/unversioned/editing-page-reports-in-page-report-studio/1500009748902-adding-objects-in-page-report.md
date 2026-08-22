---
title: "Adding Objects in Page Report"
id: 1500009748902
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009748902-Adding-Objects-in-Page-Report
updated_at: 2021-07-24T00:47:53Z
---

# Adding Objects in Page Report

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749042-Making-Simple-Modifications-to-Page-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749062-Applying-Web-Controls-in-Page-Report)

# Adding Objects in Page Report

You can add labels, images, banded objects, tables, crosstabs, charts, special fields, and web controls to page reports. This topic describes how you can insert objects in page reports and where you can place the objects.

However, for page reports that you created in Logi Report Designer, you can add objects to them only when the corresponding catalog contains business views.

You need a [Logi Report Live license for Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009776661-Logi-Report-Licenses#ServerLive) to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

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

1. Select **Menu** > **Insert**, then select the command corresponding to the object you want to add.
2. Point to the destination where you want the object to be added, and then select the mouse button.
   * If you specify to add a label, a label will be inserted there. Edit the text of the label and format it according to your requirements.
   * If you specify to add a banded object, table, crosstab, or chart, Server displays the corresponding report wizard. Specify the settings in the wizard according to your requirements. For more information, see the specific topic in [Creating a Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009748862-Creating-Page-Reports).
   * If you specify to add a special field, the special field is inserted there. For more information, see Special Fields in the *Logi Report Designer Guide*.
   * If you specify to add a parameter control, parameter form control, or filter control, Server displays the corresponding insert control dialog box. For how to specify the settings in the dialog box and the usage of the web control, see [Applying Web Controls in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009749062-Applying-Web-Controls-in-Page-Report).
   * If you specify to add a navigation control, a navigation control will be inserted there. For the usage of the navigation control, see [Applying Web Controls in Page Report](https://devnet.logianalytics.com/hc/en-us/articles/1500009749062-Applying-Web-Controls-in-Page-Report).
   * If you specify to add an image, Server displays the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009744722-Insert-Image-Dialog-Box-Properties) dialog box.
     Specify the source of the image file and the image to be inserted, then select **OK**.

     ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885402135/insrtimg.gif)

     + **Local File**  
       If the option is selected, in the File Name text box, you can type the path and name of the image file on the local file system, or use the Browse button to locate the image file.
     + **Web URL**  
        If the option is selected, in the Image URL text box, you can type the URL of the image file. Page Report Studio will record the latest 10 entered URLs in the drop-down list.  

       ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)If your Logi Report Server is in an intranet, to access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file **JRServer.bat** in `<install_root>\bin`.
     + **Library**  
        If the option is selected, you can choose an image from the My Images box which lists the images that have once been inserted into reports.

Alternatively, you can also use the Toolbox panel to add objects other than special fields into a report by dragging them from the panel to the destination.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009749042-Making-Simple-Modifications-to-Page-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009749062-Applying-Web-Controls-in-Page-Report)
