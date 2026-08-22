---
title: "Using the Migration Tool to Upgrade Logi Report Server from v16 to v17"
id: 360050379574
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360050379574-Using-the-Migration-Tool-to-Upgrade-Logi-Report-Server-from-v16-to-v17
updated_at: 2020-07-27T23:01:14Z
---

# Using the Migration Tool to Upgrade Logi Report Server from v16 to v17

**Question:**

How do I use the Migration Tool to upgrade Logi Report Server from v16 to v17?

**Answer:**

The Migration Tool allows you to keep existing catalogs, reports and scheduled tasks from an older instance of Logi Report when upgrading to v17.  When this process is completed, the old instance will remain active until it's disabled.  Follow these steps to upgrade a v16.1 instance:

Step 1: Check the original resources on v16.1, including scheduled tasks, catalogs and reports.

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360078176573/mceclip0.png)

![mceclip1.png](https://devnet.logianalytics.com/hc/article_attachments/360078176613/mceclip1.png)

![mceclip2.png](https://devnet.logianalytics.com/hc/article_attachments/360078176673/mceclip2.png)

![mceclip3.png](https://devnet.logianalytics.com/hc/article_attachments/360078176713/mceclip3.png)

Step 2: Shut down JReport 16.1 from server console.

![mceclip4.png](https://devnet.logianalytics.com/hc/article_attachments/360078176773/mceclip4.png)

Step 3: Backup the system data of JReport 16.1 by using the command “MigrationTool –backup: <path>” under %JReport Server%\bin, see below screenshot.

![mceclip5.png](https://devnet.logianalytics.com/hc/article_attachments/360078176853/mceclip5.png)

Step 4: Install a fresh new Logi Report 17. If Logi Report 17 server is running, shut it down now.

Step 5: In Command window, go to %Logi Report Server%\bin, and execute the command “Migration Tool –restore:<path>”, see below screenshot.

![mceclip6.png](https://devnet.logianalytics.com/hc/article_attachments/360078177213/mceclip6.png)

Step 6: Start Logi Report 17 Server.

**Further Reading**

<https://documentation.logianalytics.com/logireportserverguidev17/content/html/install/install_mgrt.htm>.
