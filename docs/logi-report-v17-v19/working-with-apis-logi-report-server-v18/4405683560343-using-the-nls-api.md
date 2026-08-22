---
title: "Using the NLS API"
id: 4405683560343
section: "Working with APIs Logi Report Server v18"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405683560343-Using-the-NLS-API
updated_at: 2022-01-27T08:00:04Z
---

# Using the NLS API

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683552919-Applying-the-Implementations-of-the-Dashboard-Listener-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690475927-Dynamic-Connection-API)

# Using the NLS API

You can use NLS API to run reports in different languages. This topic describes the global NLS API, catalog level NLS API, report level NLS API, and resource tree NLS API.

This topic contains the following sections:

* [Global NLS API](#Global)
* [Catalog Level NLS API](#Catalog)
* [Report Level NLS API](#Report)
* [Resource Tree NLS API](#Resource)

## Global NLS API

With the global NLS API, you can add a language, then specify to translate text in another language into a version in this language, or specify to replace a font face and size with another face and size. Likewise, you can get, update, or remove a language, a text translation, or a font replacement. Moreover, you can reload Logi Report global NLS resources from Java applications outside of Logi Report via either [Java API](#Java) or [URL API](#URL).

Server applies all text translations and font replacements specified for the global NLS each time it runs a report.

Text is classified into four groups. You will find the four types in NLSType in the Logi Report Javadoc.

* **COLUMN**  
   Text for columns. This type is for reports running in Page Report Studio.
* **LABEL**  
   Text for labels and web controls.
* **PROMPT**  
   Text for prompt information.
* **TOC**  
   Text for resources displayed in the TOC tree.

**Java API**

* **For local environment**
  + Use this interface: public interface RptServer.
  + Invoke GlobalNLSLibrary getGlobalNLSLibrary().
  + Call the methods that can help with your purposes. For example, to reload Logi Report global NLS resources, call the method *reload()*.
* **For RMI usage**
  + Use this interface: public interface RemoteRptServer.
  + Invoke RemoteGlobalNLSLibrary getGlobalNLSLibrary().
  + Call the methods that can help with your purposes.

**URL API**

With the following URL API method, you can reload Logi Report global NLS resources from Java applications outside of Logi Report: `http://localhost:8888/admin/reloadGlobalNLSLibrary.jsp`. A message {"success":true,"customMsg":"OK"} displays in the web page if the global NLS resources have reloaded successfully.

## Catalog Level NLS API

With the catalog-level NLS API, you can translate object names in a catalog to different languages.

**For local environment**

* Use this interface: public interface NLSLibraryManager.
* Invoke CatalogNLSLibrary getCatalogNLSLibrary().
* Call the methods that can help with your purposes.

**For RMI usage**

* Use this interface: public interface RemoteNLSLibraryManager.
* Invoke RemoteCatalogNLSLibrary getCatalogNLSLibrary().
* Call the methods that can help with your purposes.

## Report Level NLS API

With the report-level NLS API, you can translate object names in a report to different languages.

**For local environment**

* Use this interface: public interface NLSLibraryManager.
* Invoke ReportNLSLibrary getReportNLSLibrary().
* Call the methods that can help with your purposes.

**For RMI usage**

* Use this interface: public interface RemoteNLSLibraryManager.
* Invoke RemoteReportNLSLibrary getReportNLSLibrary().
* Call the methods that can help with your purposes.

## Resource Tree NLS API

With the resource tree NLS API, you can translate object names in the resource tree of Logi Report Server to different languages.

**For local environment**

* Use this interface: public interface RptServer.
* Invoke ResourceNLSManager getResourceNLSManager().
* Call the methods that can help with your purposes.

**For RMI usage**

* Use this interface: public interface RemoteRptServer.
* Invoke RemoteResourceNLSManager getResourceNLSManager().
* Call the methods that can help with your purposes.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4420453372695/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/4405683552919-Applying-the-Implementations-of-the-Dashboard-Listener-API)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4420453372951/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/4405690475927-Dynamic-Connection-API)
