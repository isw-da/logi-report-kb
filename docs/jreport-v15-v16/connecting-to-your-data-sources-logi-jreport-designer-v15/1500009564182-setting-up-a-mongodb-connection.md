---
title: "Setting Up a MongoDB Connection"
id: 1500009564182
section: "Connecting to Your Data Sources - Logi JReport Designer v15"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009564182-Setting-Up-a-MongoDB-Connection
updated_at: 2021-07-24T05:55:45Z
---

# Setting Up a MongoDB Connection

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585201-Transforming-a-MongoDB-Schema-to-a-Relational-Schema)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585181-Managing-Schemas-in-a-MongoDB-Connection)

# Setting Up a MongoDB Connection

To set up a MongoDB connection to connect a Logi JReport catalog to a MongoDB data source, follow the steps below:

1. [Create a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562722-Creating-a-Catalog) or [open a catalog](https://devnet.logianalytics.com/hc/en-us/articles/1500009562822-Opening-a-Catalog), then in the Catalog Manager, right-click the node of a data source and select **New MongoDB Connection** from the shortcut menu.

   If you want to set up the connection in a new data source in the catalog, select any of the existing catalog data sources, select **New Data Source** on the Catalog Manager toolbar, then in the New Data source dialog, specify the name of the data source, select the **MongoDB** connection type and select **OK**.

   The [MongoDB Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/1500009566702-MongoDB-Connection-Wizard-Dialog) appears.

   ![MongoDB Connection Wizard - MongoDB Connection Information](https://devnet.logianalytics.com/hc/article_attachments/4404893867415/mngodb_infmtn.gif)
2. In the MongoDB Connection Information screen, type in the host and port of the MongoDB server, and also the user ID and password to connect to the MongoDB server. Select **Next**.
3. In the Connection Options screen, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a line for specifying the conditional replica set member for the MongoDB connection. If necessary, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a new replica set member. Select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove a selected replica set member. Then specify the options for the connection. Select **Next**.

   ![MongoDB Connection Wizard - Connection Options](https://devnet.logianalytics.com/hc/article_attachments/4404889328919/mngodb_optn.gif)
4. In the Add Database screen (this screen will be displayed only when you have no right to access all the databases in the MongoDB data source), select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a line for specifying the databases you can access in the MongoDB data source. If necessary, select ![Add button](https://devnet.logianalytics.com/hc/article_attachments/4404893791255/btn_add.gif) to add a new database. Select ![Remove button](https://devnet.logianalytics.com/hc/article_attachments/4404889276311/btn_rmv.gif) to remove a selected database. Select **Next**.

   ![MongoDB Connection Wizard - Add Database](https://devnet.logianalytics.com/hc/article_attachments/4404889329175/mngodb_dtbs.gif)
5. In the Add Schema screen, add the collection schemas that will be transformed to relational schemas into the catalog. Select **Next**.

   ![MongoDB Connection Wizard - Add Schema](https://devnet.logianalytics.com/hc/article_attachments/4404889329431/mngodb_adschma.gif)
6. In the Add Table screen, add the required tables that are transformed from the relational schemas.

   ![MongoDB Connection Wizard - Add Table](https://devnet.logianalytics.com/hc/article_attachments/4404893867671/mngodb_adtb.gif)
7. Select **Finish** to confirm the transformed result and complete the transformation process.

**Note:** When setting up the connection via SSL, you need to import the SSL certificate into the default JKS, and use the *-D* parameter to specify the system parameter in the file JRServer.bat in `<server_install_root>\server\bin` (the MongoDB Java driver mongo-java-driver-3.4.0.jar is already within Logi JReport). Then add *ssl=true* in the Options box of the Connection Options screen of the MongoDB Connection Wizard.

[![](https://devnet.logianalytics.com/hc/article_attachments/4404889273495/back.png)Previous Topic](https://devnet.logianalytics.com/hc/en-us/articles/1500009585201-Transforming-a-MongoDB-Schema-to-a-Relational-Schema)  [Next Topic![](https://devnet.logianalytics.com/hc/article_attachments/4404889273751/forward.png)](https://devnet.logianalytics.com/hc/en-us/articles/1500009585181-Managing-Schemas-in-a-MongoDB-Connection)
