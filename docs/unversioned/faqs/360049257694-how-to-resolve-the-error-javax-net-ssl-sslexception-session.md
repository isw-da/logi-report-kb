---
title: "How to Resolve the Error \"javax.net.ssl.SSLException: Session has no PSK\""
id: 360049257694
section: "FAQs"
category: "Logi Report"
url: https://devnet.logianalytics.com/hc/en-us/articles/360049257694-How-to-Resolve-the-Error-javax-net-ssl-SSLException-Session-has-no-PSK
updated_at: 2023-06-05T22:15:39Z
---

# How to Resolve the Error "javax.net.ssl.SSLException: Session has no PSK"

### 

### Question:

After the customer upgrades Logi Report Server from JDK 1.8 to Open JDK 13, the error message below appears:

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/360074819993/mceclip0.png)'

The **error.log** file contains the following entries:

```
java.io.EOFException: SSL peer shut down incorrectly  
  
javax.net.ssl.SSLException: Session has no PSK
```

How do I resolve this problem?

### Answer:

Root Cause: Open JDK 13 uses TLS 1.3 by default, whereas JDK1.8 uses TLS 1.2.

To resolve this issue, add the below JVM option into the Logi Report Server Start batch file:

```
-Djdk.tls.client.protocols="TLSv1,TLSv1.1,TLSv1.2"
```
