---
title: "How to Configure a Secure Connection to SQL Server Database"
id: 360049658633
section: "Tactics"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049658633-How-to-Configure-a-Secure-Connection-to-SQL-Server-Database
updated_at: 2024-02-26T12:32:29Z
---

# How to Configure a Secure Connection to SQL Server Database

### **Overview** This article covers two options for creating a secure, SSL-enabled connection to SQL Server.

### **Solution**

**Option 1:** Set the **encrypt** property to true and the **trustServerCertificate** property to true.  For example: 

```
 jdbc:sqlserver://hostName:1433;databaseName=AdventureWorks;integratedSecurity=true;encrypt=true;trustServerCertificate=true
```

**Option 2:** Use the **trustStore** connection string parameter.  If you use this option, then the **encrypt** property should be true and the **trustServerCertification** should be false. For example:

```
 jdbc:sqlserver://hostName:1433;databaseName=AdventureWorks;integratedSecurity=true;encrypt=true;trustServerCertificate=false;trustStore=storeName;trustStorePassword=storePassword
```

The **trustStore** property specifies the path (including filename) to the certificate trustStore file, which contains the list of certificates that the client trusts. 

**Further Reading**

Here are some articles describing how to use connection string properties that allow applications to use Secure Sockets Layer (SSL) encryption in a Java application for your reference:  
 <https://docs.microsoft.com/en-us/sql/connect/jdbc/connecting-with-ssl-encryption?view=sql-server-2017>  
 <https://docs.microsoft.com/en-us/sql/connect/jdbc/understanding-ssl-support?view=sql-server-2017>
