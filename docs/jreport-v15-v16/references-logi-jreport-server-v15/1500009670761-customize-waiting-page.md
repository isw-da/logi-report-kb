---
title: "Customize Waiting Page"
id: 1500009670761
section: "References Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009670761-Customize-Waiting-Page
updated_at: 2021-07-24T20:54:50Z
---

# Customize Waiting Page

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009670961-Catalog-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009670981-Dashboard-Properties)

# Customize Waiting Page

The Customize Waiting Page dialog appears when you select the Customize button in the Profile > Customize Server Preferences > Advanced tab on the Logi JReport Administration page. It helps you to customize the waiting screen according to your requirements. [See the dialog](javascript:%20void(null)).

![](https://devnet.logianalytics.com/hc/article_attachments/4404920576279/cstmzscrn.gif)

**Default Format**

Applies the default format provided by Logi JReport.

**Customize Format**

Allows to customize loading status image and tip text font.

* **Enable Customize Loading Status Image**  
   Allows to upload a local image to Server as the loading status image appearing in waiting pages.   
  + **Loading Status Image File**  
     Uploads an image from the local disk. These types of images are supported: GIF, JPG, BMP, and PNG.
  + **Server-side File Name**  
    This name will be used as the name of the image file after it is uploaded to server.
  + **Alignment to**  
     Specifies the relative position of the image as compared to tip text in waiting pages.
* **Tip Text Font**  
   Specifies font face and size and style of tip text in the waiting pages.

**Specify a JSP as Waiting Page**

Allows customized JSP files to implement the waiting pages.

* **JSP File**  
   Uploads a JSP from the local disk.   
  ![](https://devnet.logianalytics.com/hc/article_attachments/4404926737431/noteicon.jpg)The required JSP file is not exactly a complete JSP but a segment. Its body can contain only one root tags and the non-body section can contain only tags that are allowed in the tags.

  The following is a sample:

  |  |
  | --- |
  | ``` <div>     <table  border="0" cellspacing="0" cellpadding="0" align="center">         <tr>             <td valign="middle" align="center">                 <table cellpadding="5" cellspacing="0" border="0">                     <tr>                         <td>                             <font                                  style="font-size:12px;font-family:Verdana;">                                 waiting....processing                             </font>                         </td>                     </tr>                      <tr>                         <td>                             <img src="../images/loadingdefault.gif" />                         </td>                     </tr>                 </table>             </td>         </tr>     </table> </div> ``` |
* **File Name**  
   This name will be used as the name of the JSP file after it is uploaded to server.

**OK**

Applies the changes and closes the dialog.

**Cancel**

Does not retain any changes and closes the dialog.

**Help**

Displays the help document about this feature.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009670961-Catalog-Properties)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009670981-Dashboard-Properties)
