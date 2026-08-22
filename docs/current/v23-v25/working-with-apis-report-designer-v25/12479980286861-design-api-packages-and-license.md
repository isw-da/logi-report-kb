---
title: "Design API Packages and License"
id: 12479980286861
section: "Working with APIs - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12479980286861-Design-API-Packages-and-License
updated_at: 2026-02-25T23:50:51Z
source_host: docs-report.zendesk.com
---
# 
Design API Packages and License

Report provides two Design API packages: the workstation version and the server version. The workstation package is the Design API, and the server package is the Server Design API. This topic describes the differences between the two packages and the license of the Design API.

The main difference between the two packages of the Design API is that when invoking the special methods for editing catalogs, queries, reports, and parameters in the Server Design API, you also have to provide an additional parameter: UID (used to distinguish between different users, and can be a Number or a String). However when invoking them in the Design API, you do not need to provide this parameter.

Design API and Server Design API use an independent license from other Report products. You need to contact your Logi Analytics sales to obtain this special license key if you want to use either the Design API or Server Design API on your machine with Designer or Server. Report will apply the license to your program instead of applying it to the installation of the Design API or Server Design API.

The keys for Design API and Server Design API are different. For example, you cannot use the Design API key on Server Design API, and vice versa. Which key is required is based on where you set your class path at runtime. If you want to obtain the classes from <server_install_root>\lib, you need to use the Server Design API key; if you want to obtain the classes from <designer_install_root>\lib, you need to use the Design API key.

To use the key, you need to create a DesignerUserInfo instance. You can use the following constructor to provide the user ID and the Server Designer License Key or Designer License Key you receive when you purchase Report.

 DesignerUserInfo userInfo=new DesignerUserInfo(Uid, key);
  Designer desg = new Designer(catalogPath, catalogName, userInfo); 

If you want to use the Design API or Server Design API package for workstations without using Designer and Server, you need to obtain a valid license for each work station.
