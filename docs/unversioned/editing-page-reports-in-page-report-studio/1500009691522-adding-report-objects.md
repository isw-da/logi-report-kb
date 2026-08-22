---
title: "Adding Report Objects"
id: 1500009691522
section: "Editing Page Reports in Page Report Studio"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009691522-Adding-Report-Objects
updated_at: 2021-11-03T06:56:48Z
---

# Adding Report Objects

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691662-Making-Simple-Modifications-to-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls)

# Adding Report Objects

You can add labels, images, banded objects, tables, crosstabs, charts, special fields and web controls to page reports. However, for page report created in Logi JReport Designer, you can add more objects to them only when the corresponding catalog contains business views.

A [Logi JReport Live license for Logi JReport Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009691022-Logi-JReport-licenses#ServerLive) is required in order to use this feature. If you do not have the license, contact your Logi Analytics account manager to obtain it.

**Object placement**

Objects can be placed within banded objects, tables, tabulars, as well as onto an empty area of a report. The following table lists the report areas that are valid targets for the various objects, listed on the left.

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
   * If you specify to add a banded object, table, crosstab, or chart, the corresponding report wizard is displayed. Specify the settings in the wizard according to your requirements. For details, see the specific topic in [Creating a Report Tab](https://devnet.logianalytics.com/hc/en-us/articles/1500009718121-Creating-Page-Reports).
   * If you specify to add a special field, the special field is inserted there. For details about the usage of each special field, see Special Fields in the *Logi JReport Designer User's Guide*.
   * If you specify to add a parameter control, parameter form control, or filter control, the corresponding insert control dialog is displayed. For how to specify the settings in the dialog and the usage of the web control, see [Applying Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls).
   * If you specify to add a navigation control, a navigation control will be inserted there. For the usage of the navigation control, see [Applying Web Controls](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls).
   * If you specify to add an image, the [Insert Image](https://devnet.logianalytics.com/hc/en-us/articles/1500009713461-Insert-Image) dialog is displayed.
     Specify the source of the image file and the image to be inserted, then select **OK**.

     ![Insert Image dialog](https://devnet.logianalytics.com/hc/article_attachments/4412131430807/insrtimg.gif)

     + **Local File**  
       If checked, in the File Name text box, enter the path and name of the image file on the local file system, or use the Browse button to locate the image file.
     + **Web URL**  
        If checked, in the Image URL text box, enter the URL of the image file. Logi JReport will record the latest 10 entered URLs in the drop-down list.  

       **Note:** If your Logi JReport Server is in an intranet, to successfully access the image via URL, you need to add the parameters `-Dhttp.proxyHost=XXX -Dhttp.proxyPort=XX` to the server's startup file JRServer.bat located in `<install_root>\bin`.
     + **Library**  
        If checked, you can choose an image from the My Images box which lists the images that have once been inserted into reports.

Alternatively, you can also use the Toolbox panel to add objects other than special fields into a report by dragging them from the panel to the destination.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4412131374359/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009691662-Making-Simple-Modifications-to-Report-Objects)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4412139481879/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009718201-Applying-Web-Controls)
