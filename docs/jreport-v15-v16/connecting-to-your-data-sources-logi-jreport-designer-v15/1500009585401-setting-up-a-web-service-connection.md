---
title: "Setting Up a Web Service Connection"
id: 1500009585401
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009585401-Setting-Up-a-Web-Service-Connection
updated_at: 2021-07-24T05:55:41Z
---

# Setting Up a Web Service Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564342-Web-Service-Data-Sources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585361-Adding-Tables-to-a-Web-Service-Connection)

# Setting Up a Web Service Connection

To set up a web service connection to connect a Logi JReport catalog to a web service data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog).
2. In the Catalog Manager, right-click the node of a data source and choose **New SOAP Web Services Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **SOAP Web Service**  connection type and select **OK**.

   The [SOAP Web Service Data Source](https://devnet.logianalytics.com/hc/en-us/articles/1500009567922-SOAP-Web-Service-Data-Source-Dialog) dialog appears.

   ![SOAP Web Service Data Source dialog](https://devnet.logianalytics.com/hc/article_attachments/4404889312919/wbsvc.gif)
3. Specify a WSDL file to create the web service connection.
   * If you want to use a WSDL file on your local disk, check the **Local File** radio button, then select the **Browse** button to browse for the file.
   * If you want to use a WSDL file through a URI, check the **URI** radio button, then input the URI string in the text field that follows and specify the user name and password for assessing the WSDL file.
4. Select the **Options** button to show the additional settings.
5. Select the **Time Zone and Locale** button to specify the time zone and the locale as required.
6. If you want the catalog or schema, or both of them to be used in data manipulation, make the selection in the Qualified Name Pattern box according to your requirements.
7. Input the number of seconds in the Time Out text field to specify how long to wait to get the WSDL file.
8. Select the **Security Configuration** button to display the [Security Configuration Setting](https://devnet.logianalytics.com/hc/en-us/articles/1500009588541-Security-Configuration-Setting-Dialog) dialog to configure the security policy.

   ![Security Configuration Setting dialog](https://devnet.logianalytics.com/hc/article_attachments/4404893857303/scrtyconfigset.gif)
9. Specify the user name and password for the user name token to be used in the security policy.
10. Specify the type for the key store from the Key Store Type drop-down list.
11. Select the **Browse** button next to the Key Store File field to specify the key store file.
12. Input the password in the Key Store Password text field to get the access to the key store file.
13. In the Client Key box, specify the alias name to be used as client signature in the key store, and set the password for the name.
14. In the Server Key box, specify the alias name and password to be used to get the server-side certification or public key in the key store.
15. When done, select **OK** to go back to the Web Service Data Source dialog.
16. Select the **OK** button in the Web Service Data Source dialog to set up the web service connection.

**Note:** When you configure the security policy for a web service connection, except for Key Store Type, all the other options in Security Configuration Setting dialog can be controlled by [constant level formulas](https://devnet.logianalytics.com/hc/en-us/articles/1500009589701-Formula-Levels#CLF). However, the formula control is only available after the web service connection is already set up, that is when you edit an existing web service connection.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009564342-Web-Service-Data-Sources)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585361-Adding-Tables-to-a-Web-Service-Connection)
