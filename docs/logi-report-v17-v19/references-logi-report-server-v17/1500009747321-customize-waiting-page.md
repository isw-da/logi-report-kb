---
title: "Customize Waiting Page"
id: 1500009747321
section: "References Logi Report Server v17"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009747321-Customize-Waiting-Page
updated_at: 2021-07-25T07:19:43Z
---

# Customize Waiting Page

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720522-Change-Password)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747741-Dashboard-Properties)

# Customize Waiting Page

The Customized Waiting Page dialog box is used to customize the waiting screen. It appears when an admin user selects the Customize button in the Administration > Server Profile > Customize Server Preferences > Advanced tab in the server console as an administrator.

![Customize Waiting Page dialog](https://devnet.logianalytics.com/hc/article_attachments/4404936887319/cstmzscrn.gif)

**Default Format**

Applies the default format provided by Logi Report.

**Customize Format**

Allows to customize loading status image and tip text font.

* **Enable Customize Loading Status Image**  
   Allows to upload a local image to Logi Report Server as the loading status image appearing in waiting pages.   
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
   Uploads a JSP from the local disk. Note that the required JSP file is not exactly a complete JSP but a segment. Its body can contain only one root <div></div> tags and the non-body section can contain only tags that are allowed in the <body></body> tags.

  The following is a sample:

  ```
  <div>  
    <table  border="0" cellspacing="0" cellpadding="0" align="center">  
      <tr>  
        <td valign="middle" align="center">  
          <table cellpadding="5" cellspacing="0" border="0">  
            <tr>  
              <td><font style="font-size:12px;font-family:Verdana;">waiting....processing</font></td>  
            </tr>   
            <tr>  
              <td><img src="../images/loadingdefault.gif" /></td>  
            </tr>  
          </table>  
        </td>  
      </tr>  
    </table>  
  </div>
  ```
* **File Name**  
   This name will be used as the name of the JSP file after it is uploaded to server.

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404936712471/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009720522-Change-Password)[Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404942444695/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009747741-Dashboard-Properties)
