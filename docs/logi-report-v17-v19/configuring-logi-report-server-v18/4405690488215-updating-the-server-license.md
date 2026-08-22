---
title: "Updating the Server License"
id: 4405690488215
section: "Configuring Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405690488215-Updating-the-Server-License
updated_at: 2024-11-28T13:19:46Z
---

# Updating the Server License

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690491799-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683582231-Changing-the-Server-Context-Path)

# Updating the Server License

Logi Report Server restricts specific features by [licenses](https://devnet.logianalytics.com/hc/en-us/articles/4405683899543-Logi-Report-Licenses). This topic describes the procedure of updating the server license via the Server Console.

While using Logi Report Server, you may need to update the server license with a new one that has more features. When your server license expires, Logi Report also prompts you to update the license when you start the server. You will be able to continue to use the server after you update the license information.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/28131194668311) You need to be an administrator to access the Administration menu on the Server Console to update the license.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** >  **License Key**. Server displays a page.
2. Select **here** to update the key.

   ![Update Server License](https://devnet.logianalytics.com/hc/article_attachments/4420461725463)
3. Type the valid user ID and license key you received from your Logi Analytics account manager.

   ![Update Server License](https://devnet.logianalytics.com/hc/article_attachments/4420447350039)
4. Select **Submit** to apply the new license key.

   Logi Report Server prompts you with the new access information of your server after the update succeeds.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/28131194668311)

* If your Logi Report Server license is machine specific, you can only use it to update the license of the Logi Report Server installed on the computer whose name is defined in the license file.
* You can apply a license key programmatically when running a Logi Report Server docker image, by setting the two environment variables: USERKEY and USERPASSWORD.

  Case 1: use the command line interface

  ```
  docker run -itd --name LogiReportServer -p 8888:8888 \  
    
  -e USERKEY=<User> -e USERPASSWORD=<licensekey> logianalytics/LogiReportServer:v18
  ```

  Case 2: use docker compose

  ```
  version: '3.7'  
  services:   
    # Other services...  
    server:   
      environment:  
       - USERKEY=<User>  
        - USERPASSWORD=<licensekey>  
      image: logianalytics/LogiReportServer:v18  
      ports:  
        - "8888:8888"  
      # Other settings for Logi Report Server container...
  ```

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405690491799-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405683582231-Changing-the-Server-Context-Path)
