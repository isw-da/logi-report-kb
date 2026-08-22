---
title: "Logi Report v17.1 Enhancements"
id: 1500010099581
section: "Release Notes for Logi Report Designer v17.1"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500010099581-Logi-Report-v17-1-Enhancements
updated_at: 2022-10-18T10:51:58Z
---

# Logi Report v17.1 Enhancements

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061162-Logi-Report-v17-1-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010092941-Logi-Report-Designer-Guide-v17-1-Overview)

# Logi Report v17.1 Enhancements

This topic introduces the significant features of Logi Report v17.1. This includes a variety of flexible time zone options and new ACL interfaces for JDK 14 support.

## Flexible Time Zone Options

You can now set time zone in both Logi Report Designer and Server in a variety of ways. On Server, you can change time zone at the server level for displaying date and time on Server UI and in reports and parameters.

![Server-Level Time Zone Setting](https://devnet.logianalytics.com/hc/article_attachments/4404856867095/time-zone.gif)

You can also set time zone at the session level to work in one report or user session, such as in the session and the URL for running reports or dashboards, using the property rpt\_timezone.

Furthermore, in the XML data source, you can set different time zones for different date and time values. To make the time zones work on the values, you can run the reports using URLs and add the parameter "CustomOffset=true" in the URLs.

Besides, in Logi Report Designer, you can view and export reports with value-level time zone that you set in the XML data source, by enabling the "Use value time zone" option.

## New ACL Interfaces for JDK 14 Support

Logi Report Server security functionality can now work well with
JDK 13 or above. Server has defined new ACL (Access Control List) interfaces to replace the interfaces that the package java.security.acl provides because Oracle removed this package from JDK 14.

You can see the following changes in Server API:

* Added the package com.jinfonet.security.jacl to define ACL.
* Added the class jet.server.api.BasePermissions to replace jet.server.api.Permissions.
* In the jet.server.api.ResourceManager interface, added two *checkBasePermission()* methods to replace two *checkPermission()* methods.
* In the jet.server.api.custom.security.AuthorizationProvider interface, added a method *isBasePermissionOk()* to replace *isPermissionOk()*.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404856790679/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500010061162-Logi-Report-v17-1-Release-Notes)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404856790935/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500010092941-Logi-Report-Designer-Guide-v17-1-Overview)
