---
title: "Design API Packages & License"
id: 1500009582741
section: "Working with APIs - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009582741-Design-API-Packages-License
updated_at: 2021-07-24T05:56:20Z
---

# Design API Packages & License

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562342-Logi-JReport-Design-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562362-Installing-the-Design-API)

# Design API Packages & License

There are two Logi JReport Design API packages: the workstation version and the server version. The workstation package is the Design API, and the server package is the Server Design API. The main difference between these two packages is that when invoking the special methods for editing catalogs, queries, reports, and parameters in the Server Design API, you also have to provide an additional parameter: UID (used to distinguish between different users, and can be a Number or a String). However when invoking them in the Design API, you do not need to provide this parameter.

Logi JReport Design API and Logi JReport Server Design API use an independent license from other Logi JReport products. You need to contact Jinfonet sales to obtain this special license key if you want to use either Logi JReport Design API or Logi JReport Server Design API on your machine with Logi JReport Designer or Logi JReport Server. The license will be applied to your program instead of being applied to the installation of Logi JReport Design API or Logi JReport Server Design API.

The keys for Logi JReport Design API and Logi JReport Server Design API are different. For example, you cannot use the Logi JReport Design API key on Logi JReport Server Design API, and vice versa. Which key is required is based on where you set your class path at runtime. If the classes are obtained from `<server_install_root>\lib` you need to use the Server Design API key. If the classes are obtained from `<designer_install_root>\lib` you need to use the Design API key.

To use the key you need to create a DesignerUserInfo instance. Use the following constructor to provide the user ID and the Server Designer License Key or Designer License Key you received when you purchased Logi JReport.

`DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key);  
 Designer desg = new Designer(catalogPath, catalogName, userInfo);`

If you want to use Logi JReport Design API or Logi JReport Server Design API package for workstations without using Logi JReport Designer and Logi JReport Server, you will need to obtain a valid license for each work station.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009562342-Logi-JReport-Design-API)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009562362-Installing-the-Design-API)
