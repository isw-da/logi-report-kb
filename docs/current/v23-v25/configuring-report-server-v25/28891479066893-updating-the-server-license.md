---
title: "Updating the Server License"
id: 28891479066893
section: "Configuring Report Server v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/28891479066893-Updating-the-Server-License
updated_at: 2026-02-26T02:11:18Z
source_host: docs-report.zendesk.com
---
# 
Updating the Server License 

Report Server restricts specific features by licenses. This topic describes the procedure of updating the server license via the Server Console.

While using Report Server, you may need to update the server license with a new one that has more features. When your server license expires, Report also prompts you to update the license when you start the server.  You will be able to continue to use the server after you update the license information. 

 You need to be an administrator to access the Administration menu on the Server Console to update the license.

- On the system toolbar of the Server Console, navigate to Administration > Configuration >  License Key. Server displays a page. 

- Select here to update the key.
    

- Type the valid user ID and license key you received from your Logi Analytics account manager.

- Select Submit to apply the new license key.
    Report Server prompts you with the new access information of your server after the update succeeds.

- If your Report Server license is machine specific, you can only use it to update the license of the Report Server installed on the computer whose name is defined in the license file.

- You can apply a license key programmatically when running a Report Server docker image, by setting the two environment variables: USERKEY and USERPASSWORD.
        Case 1: use the command line interface

docker run -itd --name LogiReportServer -p 8888:8888 \

-e USERKEY=Intersystems -e USERPASSWORD=<licensekey> logianalytics/LogiReportServer:v18
Case 2:  use docker compose

version: '3.7'
services:

  # Other services...
  server: 
    environment:
      - USERKEY=Intersystems
      - USERPASSWORD=<licensekey>
    image: logianalytics/LogiReportServer:v18
    ports:
      - "8888:8888"
    # Other settings for Report Server container...
