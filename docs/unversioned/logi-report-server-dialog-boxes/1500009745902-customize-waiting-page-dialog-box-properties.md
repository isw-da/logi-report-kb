---
title: "Customize Waiting Page Dialog Box Properties"
id: 1500009745902
section: "Logi Report Server Dialog Boxes"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009745902-Customize-Waiting-Page-Dialog-Box-Properties
updated_at: 2021-07-24T00:48:49Z
---

# Customize Waiting Page Dialog Box Properties

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773961-Change-Password-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746262-Dashboard-Properties)

# Customize Waiting Page Dialog Box Properties

Use the Customized Waiting Page dialog box to customize the waiting screen. This topic describes how to customize the Waiting Page.

Server displays the dialog box when an admin user selects the Customize button in the Administration > Server Profile > Customize Server Preferences > Advanced tab in the Server Console.

![Customize Waiting Page dialog](https://devnet.logianalytics.com/hc/article_attachments/4404885514391/cstmzscrn.gif)

**Default Format**

Server applies the default format.

**Customize Format**

Select to customize loading status image and tip text font.

* **Enable Customize Loading Status Image**  
   Select if you want to upload a local image to Server as the loading status image in waiting pages.   
  + **Loading Status Image File**  
     Select **Browse** to upload an image from the local disk. You can select these types of images: GIF, JPG, BMP, and PNG.
  + **Server-side File Name**  
    Type the name of the image file for use on Server after it is uploaded to Server.
  + **Alignment to**  
     Select the relative position of the image as compared to tip text in waiting pages.
* **Tip Text Font**  
   Specify font face, font size, and the style of tip text in the waiting pages.

**Specify a JSP as Waiting Page**

Select if you want to customize a JSP to implement the waiting page.

* **JSP File**  
   Select **Browse** to upload a JSP from the local disk.

  ![Note icon](https://devnet.logianalytics.com/hc/article_attachments/4404885305111/noteicon.jpg)The required JSP file is not exactly a complete JSP but a segment. Its body can contain only one pair of root <div></div> tags and the non-body section can contain only tags that are allowed in the <body></body> tags.

  See the following sample code:

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
   Type the name of the JSP file for use on Server after it is uploaded to Server.

**OK**

Applies the changes and closes the dialog box.

**Cancel**

Does not retain any changes and closes the dialog box.

**Help**

Displays the help document about this feature.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404880134167/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009773961-Change-Password-Dialog-Box-Properties)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404880134423/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009746262-Dashboard-Properties)
