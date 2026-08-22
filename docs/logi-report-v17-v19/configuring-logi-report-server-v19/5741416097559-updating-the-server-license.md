---
title: "Updating the Server License"
id: 5741416097559
section: "Configuring Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741416097559-Updating-the-Server-License
updated_at: 2024-11-28T13:20:32Z
---

# Updating the Server License

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741409443095-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741401150871-Changing-the-Server-Context-Path)

# Updating the Server License

Logi Report Server restricts specific features by [licenses](https://devnet.logianalytics.com/hc/en-us/articles/5741452341143-Logi-Report-Licenses). This topic describes the procedure of updating the server license via the Server Console.

While using Logi Report Server, you may need to update the server license with a new one that has more features. When your server license expires, Logi Report also prompts you to update the license when you start the server. You will be able to continue to use the server after you update the license information.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/28131196467479) You need to be an administrator to access the Administration menu on the Server Console to update the license.

1. On the system toolbar of the Server Console, navigate to **Administration** > **Configuration** >  **License Key**. Server displays a page.
2. Select **here** to update the key.

   ![Update Server License](https://devnet.logianalytics.com/hc/article_attachments/9905818463383)
3. Type the valid user ID and license key you received from your Logi Analytics account manager.

   ![Update Server License](https://devnet.logianalytics.com/hc/article_attachments/28131257350807)
4. Select **Submit** to apply the new license key.

   Logi Report Server prompts you with the new access information of your server after the update succeeds.

![Note icon](https://devnet.logianalytics.com/hc/article_attachments/28131196467479)

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

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741409443095-Configuring-Proxy-for-Connecting-to-a-REST-Web-Service)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741401150871-Changing-the-Server-Context-Path)
