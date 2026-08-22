---
title: "MongoDB Connection Properties"
id: 12480283458573
section: "References - Report Designer v25"
category: "Logi Report"
url: https://docs-report.zendesk.com/hc/en-us/articles/12480283458573-MongoDB-Connection-Properties
updated_at: 2026-02-25T23:48:13Z
source_host: docs-report.zendesk.com
---
# 
MongoDB Connection Properties

This topic describes the properties of a MongoDB Connection object in a catalog.

| Property Name | Description |
| --- | --- |
| Connection Options | Specifies the options used to connect to the MongoDB server, which are "name=value" pairs separated by "&". You can reference parameters and constant level formulas in the current catalog data source in the format @FieldName, and the User Name special field as @username in the value.Data type: String |
| Default | Specifies whether the connection is the default connection in the current catalog data source. By default, the first connection you create in a data source is the default connection of the data source. A data source can have zero or one default connection. Data type: Boolean |
| Description | Specifies the description of the connection. Data type: String |
| Name | Specifies the mapped name of the connection in the catalog. Data type: String |
| Password | Specifies the password for connecting to the MongoDB database. You can reference a parameter or constant level formula in the current catalog data source in the format @FieldName, or the User Name special field as @username in the password. If you save the catalog in XML, Designer encrypts the password using a internal algorithm and stores it in the XML catalog file. Designer decrypts the password when loading the XML catalog. Data type: String |
| Push Down Group Query | Specifies whether to push down group level summary computations to the database at runtime. true Select to push down the group level summary computations to the database if it can perform the computations; otherwise, Report Engine do the computations itself. false Select to have Report Engine perform the group level summary computations itself. Data type: Boolean |
| Server Address | Shows a list of replica set members or MongoDBs, including IP/host name and port pairs. Read only. If the list contains no IP/host name and port pairs, it means connecting to the local host with the default MongoDB port. For each pair in the list, the IP/host name cannot be null, while the port can be. When the port is null, it means connecting to the MongoDB by the default port. |
| User | Specifies the user ID for connecting to the MongoDB database. You can reference a parameter or constant level formula in the current catalog data source in the format @FieldName, or the User Name special field as @username in the user ID. Data type: String |
