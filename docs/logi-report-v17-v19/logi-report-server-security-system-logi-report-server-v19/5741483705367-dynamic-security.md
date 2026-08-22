---
title: "Dynamic Security"
id: 5741483705367
section: "Logi Report Server Security System Logi Report Server v19"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/5741483705367-Dynamic-Security
updated_at: 2022-10-31T17:18:25Z
---

# Dynamic Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741455041943-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483732759-Server-Security-System)

# Dynamic Security

Logi Report Server administrators can change the security policy of a catalog at runtime, without having to edit the security in Logi Report Designer and publish the catalog again. This topic describes how you can create and apply dynamic security policies for catalogs using security files, which contain catalog security definitions.

Developer users can also [use API to manage dynamic security](https://devnet.logianalytics.com/hc/en-us/articles/5741415142807-Dynamic-Security-API).

This topic contains the following sections:

* [Creating Security Files](#CreateFile)
* [Creating Dynamic Security](#Createdyn)
* [Changing the Security File of a Dynamic Security Policy](#Change)
* [Downloading Dynamic Security](#Download)
* [Applying Dynamic Security](#Apply)

## Creating Security Files

The security files that you can use to create dynamic security on Logi Report Server are in XML format. You can create the security files by yourself, however, the best way to generate a security file is using Logi Report Designer.

A security file can contain security definitions of [Record Level Security](https://devnet.logianalytics.com/hc/en-us/articles/5741463498263-Record-Level-and-Column-Level-Security) (RLS), [Column Level Security](https://devnet.logianalytics.com/hc/en-us/articles/5741463498263-Record-Level-and-Column-Level-Security) (CLS), and [Business View Security](https://devnet.logianalytics.com/hc/en-us/articles/5741455041943-Business-View-Security). For how to define RLS and CLS in an XML file, refer to Importing/Exporting Security Information from/to External XML Files in the *Logi Report Designer Guide*. As for the format of business view security, you can refer to the sample file DynamicSecurity.xml in `<install_root>\help\samples\DynamicSecurity`.

Suppose that you defined a business view security policy as follows:

| Principal | Element | Visible Permission | Access Permission | Allowed Set | Denied Set | Allow Unspecified Members |
| --- | --- | --- | --- | --- | --- | --- |
| everyone | Customer.Country | Allow | Allow | China | Japan | True |

It is like this in the XML file:

![](https://devnet.logianalytics.com/hc/article_attachments/9905636829591/scrty_rsc_srv_dynscrty1.gif)

When you define the Allowed Set and Denied Set using expressions, for example:

| Principal | Element | Visible Permission | Access Permission | Allowed Set | Denied Set | Allow Unspecified Members |
| --- | --- | --- | --- | --- | --- | --- |
| everyone | Orders Detail.Order ID | Allow | Allow | "Order ID" > 3431 And "Order ID" < 3005 | "Order ID" between 3008 and 3011 | True |

In the XML file, the business view security policy will be like this:

![](https://devnet.logianalytics.com/hc/article_attachments/9905658226839/scrty_rsc_srv_dynscrty2.gif)

## Creating Dynamic Security

To create a dynamic security policy, take these steps:

1. On the system toolbar of the Server Console, navigate to **Administration** > **Security** > **Dynamic Security**. Server displays the Dynamic Security page.

   ![Security - Dynamic Security page](https://devnet.logianalytics.com/hc/article_attachments/9905658260887/scrty_rsc_rpt_dynscrty.gif)
2. Select **New Dynamic Security**. Server displays the [New Dynamic Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741414108439-New-Dynamic-Security-Dialog-Box-Properties).
3. Select **Browse** next to the Catalog box.
4. Server displays the Select Catalog dialog box. Browse to the catalog you want to create dynamic security for.
5. Select **OK**.
6. Select **Browse** next to the Security File box.
7. Select the security file based on which you want to create the dynamic security for the catalog.
8. Select **Open**.
9. Select **OK** to create the dynamic security. Server adds it to the dynamic security table.

One catalog can have several dynamic security policies. In this case, you can choose one of them as the default dynamic security of the catalog. To do this, select **false** in the **Is Default** column for the dynamic security.

If you want to remove a dynamic security policy, select it in the dynamic security table, then select **Delete**. You can delete multiple dynamic security policies at a time.

The following table describes the options in the Dynamic Security page:

| Option | Description |
| --- | --- |
| New Dynamic Security | Select to create a dynamic security in the [New Dynamic Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741414108439-New-Dynamic-Security-Dialog-Box-Properties). |
| Delete | Select to delete the selected dynamic security. |
| Search | Search for specific dynamic security.  * **Search category list**  Select the search category. For example, if you want to find the dynamic security which uses the catalog **SampleReprts.cat**, select **Catalog** from the list. Select from these search categories:    + **Catalog** Select to search for catalogs.   + **Security File** Select to search for catalog security file names.   + **Is Default** Select to search for *true* or *false* in the Is Default column. * **Keyword text box**  Type the search keyword, and then select the search iconSearch button in the text box to start the search. |
| Dynamic security table | |
| Checkbox | Select or clear a dynamic security. Select the checkbox on the column header to select all the dynamic security. |
| Catalog | Catalog for which a dynamic security is, with the full resource path, for example, `/Public Reports/SampleReports/SampleReports.cat`. You can select the column header to sort the column. |
| Security File | Name of the catalog security file for a dynamic security. You can select the column header to sort the column. |
| Is Default | Server shows whether a dynamic security is the default. The value is editable. Select **false** to set a dynamic security as the default. For a catalog, you can set only one dynamic security to true, and the latest setting takes effect.  You can select the column header to sort the column. |
| Controls | Control the dynamic security.  * **Upload**  Select to upload a catalog security file for a specific dynamic security in the [Upload Dynamic Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428021783-Upload-Dynamic-Security-Dialog-Box-Properties). * **Download**  Select to download the catalog security file from Server. |

## Changing the Security File of a Dynamic Security Policy

You can modify the security file based on which the dynamic security policy of a catalog is. To do this, select **Upload** in the Controls column for the dynamic security. Server displays the [Upload Dynamic Security dialog box](https://devnet.logianalytics.com/hc/en-us/articles/5741428021783-Upload-Dynamic-Security-Dialog-Box-Properties). Select another security file to create the dynamic security for the catalog.

## Downloading Dynamic Security

You can download the dynamic security you defined on Server to a file. To do this, select **Download** in the Controls column for the dynamic security. Server downloads it to your drive. You can then modify the security definitions in the file. After editing, you can upload the file to a dynamic security policy to change the security definitions in the policy.

## Applying Dynamic Security

After you specify a default dynamic security policy for a catalog, when running reports, dashboards, or analysis templates which use the catalog, no matter interactive, on-demand, or scheduled, Logi Report will always try to load the dynamic security for the catalog before running and try to use the security defined in the security file on which the dynamic security is based to replace the catalog security.

* **For business view**  
   For each given principal and business view, if there is security definition in the security file, it will replace the whole security definition for this principal on this business view.

  If the security file mentions a business view element, but the element is not in the catalog, Server will ignore the security file.
* **For security entry**  
   For a given principal and a security entry, if there is CLS definition in the security file, it will replace the CLS in the catalog security.
  If there is RLS definition in the file, it will replace the RLS in the catalog security.

If there is no default dynamic security specified for a catalog, the security definitions created in the catalog at design time will apply.

[![Back](https://devnet.logianalytics.com/hc/article_attachments/9905574448535/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/5741455041943-Business-View-Security)  [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/9905574466839/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/5741483732759-Server-Security-System)
