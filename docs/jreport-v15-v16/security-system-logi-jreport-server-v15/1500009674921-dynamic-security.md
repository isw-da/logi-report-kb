---
title: "Dynamic Security"
id: 1500009674921
section: "Security System Logi JReport Server v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009674921-Dynamic-Security
updated_at: 2021-07-24T20:53:42Z
---

# Dynamic Security

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674881-Business-View-Security)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650022-Server-Security-System)

# Dynamic Security

Logi JReport Server administrators can create dynamic security policies for catalogs published to the server using security files, which contain catalog internal security definitions. With dynamic security, administrators can dynamically change the security policy applied to a catalog.

Developer users can also [use API to manage dynamic security](https://devnet.logianalytics.com/hc/en-us/articles/1500009668621-Dynamic-Security-API).

Below is a list of the sections covered in this topic:

* [Creating Security Files](#CreateFile)
* [Creating Dynamic Security](#Createdyn)
* [Changing the Security File of a Dynamic Security Policy](#Change)
* [Downloading Dynamic Security](#Download)
* [Applying Dynamic Security](#Apply)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating Security Files

The security files that can be used to create dynamic security on Logi JReport Server are in XML format. You can create the security files by yourself, however, the best way to generate a security file is using Logi JReport Designer (for details, see "Exporting Catalog Security into a Security File" in the *Logi JReport Designer User's Guide*).

A security file can contain security definitions of [record-level security](https://devnet.logianalytics.com/hc/en-us/articles/1500009650002-Record-Level-Security-and-Column-Level-Security) (RLS), [column-level security](https://devnet.logianalytics.com/hc/en-us/articles/1500009650002-Record-Level-Security-and-Column-Level-Security) (CLS) and [business view security](https://devnet.logianalytics.com/hc/en-us/articles/1500009674881-Business-View-Security). For how to define RLS and CLS in an XML file, see the topic "Importing/Exporting Security Information from/to External XML Files" in the *Logi JReport Designer User's Guide*. As for the format of business view security, you can refer to the sample file DynamicSecurity.xml, which is stored in `<install_root>\help\samples\DynamicSecurity`.

Suppose that a business view security policy is defined as follows:

| Principal | Element | Visible Permission | Access Permission | Allowed Set | Denied Set | Allow Unspecified Members |
| --- | --- | --- | --- | --- | --- | --- |
| everyone | Customer.Country | Allow | Allow | China | Japan | True |

In the XML file, it will be written like below:

![](https://devnet.logianalytics.com/hc/article_attachments/4404920420631/scrty_rsc_srv_dynscrty1.gif)

When the Allowed Set and Denied Set are defined using expressions, for example:

| Principal | Element | Visible Permission | Access Permission | Allowed Set | Denied Set | Allow Unspecified Members |
| --- | --- | --- | --- | --- | --- | --- |
| everyone | Orders Detail.Order ID | Allow | Allow | "Order ID" > 3431 And "Order ID" < 3005 | "Order ID" between 3008 and 3011 | True |

In the XML file, the business view security policy will be like this:

![](https://devnet.logianalytics.com/hc/article_attachments/4404920421271/scrty_rsc_srv_dynscrty2.gif)

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Creating Dynamic Security

To create a dynamic security policy, take the following steps:

1. Log onto the Logi JReport Administration page.
2. Select **Security** on the system toolbar and select **Data Source**  from the drop-down menu to display the Security - Dynamic Security page.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404926662167/scrty_rsc_rpt_dynscrty.gif)
3. Select **New Dynamic Security** on the task bar.
4. In the [New Dynamic Security dialog](https://devnet.logianalytics.com/hc/en-us/articles/1500009646642-New-Dynamic-Security), select the **Browse** button next to the Catalog text field.
5. In the Select Catalog dialog, browse to the catalog you want to create dynamic security for and select **OK**.
6. Select the **Browse** button next to the Security File text field, select the security file based on which the dynamic security for the catalog will be created, then select **Open**.
7. Select **OK** in the dialog to create the dynamic security, and it is added to the dynamic security table.

One catalog can have several dynamic security policies. In this case, you can specify which one of them will be used as the default dynamic security of the catalog. To do this, select the **false** link in the Is Default column for the dynamic security.

If you want to remove a dynamic security policy, check it in the dynamic security table, then select the **Delete** link above the table. You can delete multiple dynamic security policies at a time.

The following are details about the options in the Security - Dynamic Security page:

| Option | Description |
| --- | --- |
| New Dynamic Security | Creates a dynamic security in the [New Dynamic Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009646642-New-Dynamic-Security) dialog. |
| Delete | Deletes the selected dynamic security. |
| Search | Searches for specific dynamic security.  * **Search category drop-down list**  Specifies the search category. For example, if you want to find the dynamic security which uses the catalog SampleReprts.cat, select Catalog from the drop-down list. There are the following search categories:    + **Catalog**  Searches for catalogs.   + **Security File**  Searches for catalog security file names.   + **Is Default**  Searches for *true* or *false* in the Is Default column. * **Keyword text box**  Specifies the search keyword. After inputting the text, select  in the text box to start the search. The **x** button in the text box is used to clear the input text. |
| Dynamic security table | | | |
| Checkbox | Specifies whether or not to select a dynamic security. Select the checkbox on the column header to select all the dynamic security. |
| Catalog | Displays the catalogs for which the dynamic security are created with the full resource path, for example, `/SampleReports/SampleReports.cat`. You can select the column header to sort the column. |
| Security File | Displays the names of the catalog security files for the dynamic security. You can select the column header to sort the column. |
| Is Default | Shows whether the dynamic security is set to the default. The value is editable. Select in the Is Default cell of a dynamic security and then select true or false from the drop-down list. For a catalog, only one dynamic security can be set to true and the latest setting takes effect. You can select the column header to sort the column. |
| Controls | Controls the dynamic security.  * **Upload**  Uploads a catalog security file for a specific dynamic security in the [Upload Dynamic Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009646882-Upload-Dynamic-Security) dialog. * **Download**  Download the catalog security file from the server. |

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Changing the Security File of a Dynamic Security Policy

The security file based on which the dynamic security policy of a catalog is created can be modified. To do this, select the **Upload** link in the Controls column for the dynamic security, then in the [Upload Dynamic Security](https://devnet.logianalytics.com/hc/en-us/articles/1500009646882-Upload-Dynamic-Security) dialog, select another security file to create the dynamic security for the catalog.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Downloading Dynamic Security

The dynamic security defined on server can be downloaded to a file. To do this, select the **Download** link in the Controls column for the dynamic security, in the displayed dialog, select **OK** to save it. You can then further modify the security definitions in the file. After editing, you can upload the file to a dynamic security policy to change the security definitions in the policy.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

## Applying Dynamic Security

When a catalog is specified with a default dynamic security policy, when running reports, dashboards, or analysis templates which use the catalog, no matter interactive, on-demand, or scheduled, Logi JReport will always try to load the dynamic security for the catalog before running and try to use the security defined in the security file on which the dynamic security is created to replace the catalog security.

* **For business view**  
   For each given principal and business view, if there is security definition in the security file, the whole security definition for this principal on this business view will be replaced.

  If the security file mentions a business view element, but the element is not in the catalog, it will be ignored.
* **For security entry**  
   For a given principal and a security entry, if there is CLS definition in the security file, it will replace the CLS in the catalog security.
  If there is RLS definition in the file, it will replace the RLS in the catalog security.

If there is no default dynamic security specified for a catalog, the security definitions created in the catalog at design time will be used.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404920354583/totop.png)Back to top](#top "Click to go to the top")

[![Back](https://devnet.logianalytics.com/hc/article_attachments/4404920354071/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009674881-Business-View-Security)   [Next Topic![Next](https://devnet.logianalytics.com/hc/article_attachments/4404920354327/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009650022-Server-Security-System)
